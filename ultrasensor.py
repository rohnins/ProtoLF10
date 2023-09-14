import RPi.GPIO as GPIO
import time
import random
import os
import pygame
import pytest

# Constants
PIN_TRIGGER = 7
PIN_ECHO = 11
THRESHOLD_DISTANCE_CM = 10.33
MAX_TIMEOUT = 1.0
SOUNDS_DIR = "/home/admin/Music"

# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)
pygame.mixer.init()

# Observer pattern
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
        if distance < THRESHOLD_DISTANCE_CM:
            self.play_random_sound()

    def play_random_sound(self):
        selected_sound = random.choice(self.sound_files)
        sound_path = os.path.join(SOUNDS_DIR, selected_sound)
        print(f"Playing sound: {selected_sound}")
        
        # Use pygame to play the selected sound
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
        if time.time() - start_time > MAX_TIMEOUT:
            return -1  # Timeout

    echo_start_time = time.time()
    while GPIO.input(PIN_ECHO) == 1:
        if time.time() - echo_start_time > MAX_TIMEOUT:
            return -1  # Timeout

    pulse_duration = time.time() - echo_start_time

    # Calculation for the distance in centimeters
    distance = (pulse_duration * 34300) / 2
    return distance

# Main loop
try:
    while True:
        distance = read_distance()
        print("Distance:", distance, "cm")
        sensor.notify_observers(distance)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()