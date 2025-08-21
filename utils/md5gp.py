import hashlib
def md5_zc(c):
    h=hashlib.md5(c.encode()).hexdigest()
    return h
