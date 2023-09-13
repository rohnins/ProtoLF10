#!/home/admin
#init
import RPi.GPIO as GPIO
import time
import random
import os
import pygame
import pytest

# Constants
PIN_TRIGGER = 7
PIN_ECHO = 11
# for the distance, everything below the number triggers a sound to happen. Make sure to adjust this number. I selected 10cm for testing.
THRESHOLD_DISTANCE = 10.33 # Our determined distance for idle, any change in that distance gives a reaction
SOUNDS_DIR = "/home/admin/Music" # The path on our rasp, where all MP3 files are located, we just select the music folder.

# initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)
pygame.mixer.init()

# designpattern observer
class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, distance):
        for observer in self.observers:
            observer.update(distance)

class SoundObserver:
    def __init__(self):
        self.sound_files = os.listdir(SOUNDS_DIR)

    def update(self, distance):
        if distance < THRESHOLD_DISTANCE:
            self.play_random_sound()

    def play_random_sound(self):
        selected_sound = random.choice(self.sound_files)
        sound_path = os.path.join(SOUNDS_DIR, selected_sound)
        print(f"Playing sound: {selected_sound}")
        # now we use pygame to play the selected sound
        
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
 
 # Create instances of the Subject and SoundObserver
sensor = Subject()
sound_observer = SoundObserver()
sensor.add_observer(sound_observer)

# Functions for ultrasonic sensor
def read_distance():
      # Send a pulse to trigger the sensor
    GPIO.output(PIN_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, False)

    # Wait for the echo to return
    start_time = time.time()
    while GPIO.input(PIN_ECHO) == 0:
        if time.time() - start_time > 1.0:
            return -1  # Timeout

    echo_start_time = time.time()
    while GPIO.input(PIN_ECHO) == 1:
        if time.time() - echo_start_time > 1.0:
            return -1  # Timeout

    pulse_duration = time.time() - echo_start_time

    # Calculate distance in centimeters
    distance = (pulse_duration * 34300) / 2
    return distance

# Main loop
try:
    while True:
        distance = read_distance()
        print ("Distance:",distance,"cm") #this is just for testing to measure the distance. If everything is settled, just comment this out.
        sensor.notify_observers(distance)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()       



""" #old file, for reference. if we need to measure the exact distance in our container.

#!/home/admin
#init
import RPi.GPIO as GPIO
import time
import random
import os
import pygame


try:
      GPIO.setmode(GPIO.BOARD)

      PIN_TRIGGER = 7
      PIN_ECHO = 11

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      print ("Waiting for sensor to settle")

      time.sleep(2)

      print ("Calculating distance")

      GPIO.output(PIN_TRIGGER, GPIO.HIGH)

      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
      while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

      pulse_duration = pulse_end_time - pulse_start_time
      distance = round(pulse_duration * 17150, 2)
      print ("Distance:",distance,"cm")

finally:
      GPIO.cleanup()
"""