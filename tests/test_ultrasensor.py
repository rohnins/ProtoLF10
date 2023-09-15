import pytest
import ultrasensor

# Check if SOUNDS_DIR exists
def test_sounds_dir_exists():
    assert os.path.exists(SOUNDS_DIR), "SOUNDS_DIR does not exist"

# Check distance calculation
def test_distance_calculation():
    pulse_duration = 0.0001  # Example pulse duration for testing
    expected_distance = (pulse_duration * 34300) / 2
    assert read_distance(pulse_duration) == expected_distance, "Distance calculation is incorrect"
