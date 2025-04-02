import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ...existing code...

STATIC_URL = '/static/'  # Make sure this has a trailing slash
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'analyzer', 'static'),  # Corrected path
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ...existing code...
