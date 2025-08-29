import os

from django.core.management.utils import get_random_secret_key


def secret_key_validator():
    if os.getenv("DJANGO_DEBUG") and os.getenv("DJANGO_SECRET_KEY"):
        return os.getenv("DJANGO_SECRET_KEY")
    elif os.getenv("DJANGO_DEBUG"):
        return get_random_secret_key()
    raise ValueError("DJANGO_SECRET_KEY environment variable not set")
