import hashlib

def sha256(text: str) -> bytes:
    return hashlib.sha256(text.encode()).digest()
