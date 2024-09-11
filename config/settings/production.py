from .base import *  # noqa

DEBUG = False
SECRET_KEY = os.getenv("SECRET_KEY")

STATIC_ROOT = os.path.join(BASE_DIR, "../", "static")

ALLOWED_HOSTS = ["devmasters.uz", "api.devmasters.uz"]


USE_X_FORWARDED_HOST = True
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


CORS_ALLOWED_ORIGINS = [
    "http://localhost",
    "https://devmasters.uz",
    "https://api.devmasters.uz",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = "*"
