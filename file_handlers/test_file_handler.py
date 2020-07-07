import pytest 
from .fits_handler import FITSHandler
import numpy as np
from astropy.io import fits

class Image:
    def __init__(self, imageArr):
        self.data = imageArr

image =  Image(np.array([[1,2,3],
                        [4,5,6],
                        [7,8,9]]))

class MockHDUList():
    def __getitem__(self, key):
        if key == "Image":
            return self.image
        return None
    def __init__(self):
        self.image = image
    def close(self):
        return

def test_handler(monkeypatch):
    def mock_open(path):
        return MockHDUList()
    def mock_close():
        return

    monkeypatch.setattr(fits, 'open', mock_open)

    testFits = FITSHandler('/mordor/mount/doom')
    array = testFits()

    assert np.array_equal(image.data, array)


