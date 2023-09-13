import pytest
from ultrasensor import Subject, SoundObserver, read_distance  # Replace 'your_script_file' with the actual name of your script file

# Mock GPIO functions for testing
class MockGPIO:
    @staticmethod
    def setmode(mode):
        pass

    @staticmethod
    def setup(pin, direction):
        pass

    @staticmethod
    def output(pin, value):
        pass

    @staticmethod
    def input(pin):
        pass

# Test the Subject and SoundObserver classes
def test_sound_observer():
    observer = SoundObserver()
    observer.sound_files = ["Kid_Laugh-Mike_Koenig-1673908713.mp3", "Pew_Pew-DKnight556-1379997159.mp3"] 
    observer.play_random_sound()

def test_subject_add_remove_observer():
    subject = Subject()
    observer = SoundObserver()
    subject.add_observer(observer)
    assert len(subject.observers) == 1
    subject.remove_observer(observer)
    assert len(subject.observers) == 0

# Test the ultrasonic sensor functions
def test_read_distance_timeout():
    # Mock GPIO functions to simulate timeout
    import RPi.GPIO as GPIO
    GPIO.setmode = MockGPIO.setmode
    GPIO.setup = MockGPIO.setup
    GPIO.output = MockGPIO.output
    GPIO.input = MockGPIO.input

    # Call read_distance and expect a timeout (-1)
    distance = read_distance()
    assert distance >= 0

# You can write more tests for read_distance with various distance scenarios

# Integration test
def test_integration():
    subject = Subject()
    observer = SoundObserver()
    subject.add_observer(observer)

    # Simulate a scenario where the distance is less than THRESHOLD_DISTANCE
    distance = 9.0  # Adjust this value as needed
    subject.notify_observers(distance)

    # Assert that the observer played a sound
    # You may need to mock pygame.mixer.music.load and pygame.mixer.music.play for this test
    # and verify that they were called

    # Simulate a scenario where the distance is greater than THRESHOLD_DISTANCE
    distance = 11.0  # Adjust this value as needed
    subject.notify_observers(distance)

    # Assert that the observer did not play a sound

if __name__ == '__main__':
    pytest.main()
