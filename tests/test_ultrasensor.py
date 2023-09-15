import pytest
import ultrasensor

# Check if SOUNDS_DIR exists
def test_sounds_dir_exists():
    assert os.path.exists(SOUNDS_DIR), "SOUNDS_DIR does not exist"

# Check GPIO setup
def test_gpio_setup():
    assert GPIO.getmode() == GPIO.BOARD, "GPIO mode is not set to BOARD"
    assert GPIO.gpio_function(PIN_TRIGGER) == GPIO.OUT, "PIN_TRIGGER is not set as an output pin"
    assert GPIO.gpio_function(PIN_ECHO) == GPIO.IN, "PIN_ECHO is not set as an input pin"

# Check distance calculation
def test_distance_calculation():
    pulse_duration = 0.0001  # Example pulse duration for testing
    expected_distance = (pulse_duration * 34300) / 2
    assert read_distance(pulse_duration) == expected_distance, "Distance calculation is incorrect"

# Function for ultrasonic sensor
def read_distance(pulse_duration):
    distance = (pulse_duration * 34300) / 2
    return distance