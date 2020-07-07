import area_detector_handlers
import numpy as np
from astropy.io import fits

class FITSHandler(area_detector_handlers.HandlerBase):
    specs = {"FITS"} | area_detector_handlers.HandlerBase.specs

    def __init__(self, path):
        self.__file_name = path
    
    def __call__(self):
        hdul = fits.open(self.__file_name)
        arr = hdul['Images'].data
        hdul.close()
        return arr
