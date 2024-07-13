import hashlib


def hash_url(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()[:8]

