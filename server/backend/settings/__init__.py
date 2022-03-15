"""
This module helps to manage environment settings.
"""

# import only ENV variables (uppercase variable)
from backend.settings.base_settings import *

# environment settings
if DEBUG:
  try:
    from .local_settings import *
  except ImportError:
    pass
else:
  from .prod_settings import *
