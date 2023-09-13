# tests/test_sound_observer.py
import pytest
from ultrasensor import SoundObserver

def test_sound_observer_play_sound(mocker):
    # Use a mocking library like pytest-mock or unittest.mock to mock the sound playback
    # Mock the play_random_sound method and assert that it's called when distance < threshold
    sound_observer = SoundObserver()
    mocker.patch.object(sound_observer, 'play_random_sound', return_value=None)

    # Test when distance is below the threshold
    sound_observer.update(25)
    sound_observer.play_random_sound.assert_called_once()

    # Test when distance is above the threshold
    sound_observer.update(35)
    sound_observer.play_random_sound.assert_not_called()
