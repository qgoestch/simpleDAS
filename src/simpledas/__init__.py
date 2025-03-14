from .simpleDASreader import *
from . import h5pydict
import importlib.metadata

__all__ = ['simpleDASreader', 'h5pydict']

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"

try:
    __author__ = importlib.metadata.metadata(__name__)["Author-email"]
except (importlib.metadata.PackageNotFoundError, KeyError):
    __author__ = "Ole Henrik Waagaard"