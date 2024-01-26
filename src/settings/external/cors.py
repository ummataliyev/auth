"""
cors headers configuration, allows your resource
to be accessed on other domains
"""
from src.settings import default


default.INSTALLED_APPS.append("corsheaders")

default.MIDDLEWARE.extend([
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware"
])

CORS_ALLOW_ALL_ORIGINS = default.env.bool("CORS_ALLOW_ALL_ORIGINS", False)

if CORS_ALLOW_ALL_ORIGINS is False:
    CORS_ALLOWED_ORIGINS = default.env.list("CORS_ALLOWED_ORIGINS", default=[
        "http://localhost:8080"
    ])
