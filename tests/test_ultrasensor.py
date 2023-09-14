import unittest.mock as mock
import pytest
import ultrasensor

def test_read_distance():
    """
    Test the read_distance function from ultrasensor
    """
    with mock.patch('ultrasensor.RPi.GPIO') as mock_gpio:
        # Set up the mock
        mock_gpio.input.side_effect = [0, 1, 0]
        mock_gpio.time.time.side_effect = [0, 0.00001, 0.00002]

        # Call the function
        distance = ultrasensor.read_distance()

        # Assert the expected behavior
        assert distance == pytest.approx(0.343, rel=1e-3)