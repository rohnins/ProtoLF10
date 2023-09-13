# tests/test_integration.py
import pytest
from ultrasensor import Subject, SoundObserver, read_distance

@pytest.fixture
def setup_components():
    # Initialize the components for testing
    sensor = Subject()
    sound_observer = SoundObserver()
    sensor.add_observer(sound_observer)
    return sensor, sound_observer

def test_integration_sensor_sound(setup_components, mocker):
    sensor, sound_observer = setup_components

    # Mock the read_distance function to return specific values for testing
    mocker.patch('your_project_module.read_distance', side_effect=[20, 25, 35])

    # Test interaction between components with distance changes
    # Ensure that play_random_sound is called when distance < threshold
    sensor.notify_observers(read_distance())
    sound_observer.play_random_sound.assert_called_once()

    # Reset the call count for play_random_sound
    sound_observer.play_random_sound.reset_mock()

    # Test interaction when distance is above the threshold
    sensor.notify_observers(read_distance())
    sound_observer.play_random_sound.assert_not_called()

    # Test interaction when distance goes below the threshold again
    sensor.notify_observers(read_distance())
    sound_observer.play_random_sound.assert_called_once()
