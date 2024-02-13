from django.conf import settings


def get_static(path: str) -> str:
    return settings.BASE_DIR / 'static' / path
