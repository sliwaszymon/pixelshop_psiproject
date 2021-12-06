import hashlib

def generate_certificate_id(title, desc):
        return hashlib.md5(bytes(title + desc, 'utf-8'))