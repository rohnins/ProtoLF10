import unittest.mock as mock
import pytest
import ultrasensor

def test_update():
    """
    Test the update method of the SoundObserver class
    """
    with mock.patch('ultrasensor.pygame.mixer.music') as mock_music:
        # Create a SoundObserver instance
        observer = ultrasensor.SoundObserver()

        # Call the update method with a distance less than the threshold
        observer.update(ultrasensor.THRESHOLD_DISTANCE - 1)

        # Assert that a sound was played
        mock_music.load.assert_called_once()
        mock_music.play.assert_called_once()

        # Reset the mock
        mock_music.reset_mock()

        # Call the update method with a distance greater than the threshold
        observer.update(ultrasensor.THRESHOLD_DISTANCE + 1)

        # Assert that no sound was played
        mock_music.load.assert_not_called()
        mock_music.play.assert_not_called()