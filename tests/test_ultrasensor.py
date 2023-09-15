import pytest
import ultrasensor

# Check if SOUNDS_DIR exists
def test_sounds_dir_exists():
    assert os.path.exists(SOUNDS_DIR), "SOUNDS_DIR does not exist"


def test_subtraction():
    """
    Test that subtraction works correctly
    """
    assert 3 - 2 == 1

def test_multiplication():
    """
    Test that multiplication works correctly
    """
    assert 2 * 2 == 4

def test_division():
    """
    Test that division works correctly
    """
    assert 4 / 2 == 2