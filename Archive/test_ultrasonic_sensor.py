# tests/test_ultrasonic_sensor.py
import pytest
from ultrasensor import read_distance

def test_read_distance_valid():
    # Simulate a valid distance reading (e.g., 20 cm)
    distance = read_distance()
    assert distance >= 0

def test_read_distance_timeout():
    # Simulate a timeout condition (no echo signal)
    # Ensure that the function returns -1 for timeout
    distance = read_distance()
    assert distance == -1
