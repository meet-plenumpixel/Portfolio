"""
initialize settings specific to the production environment.
If backend/Environ/Prod.env file exists.
"""

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


__all__ = [i for i in dir() if i.isupper()]