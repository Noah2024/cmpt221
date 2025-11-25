import bcrypt

def rmWhitespace(str):
    return str.strip()

def encrypt(rawPswd):
    bytes = rawPswd.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash.decode('utf-8') 

def compareHash(userPswd, hash):
    userBytes = userPswd.encode('utf-8')
    hash = hash.encode('utf-8')
    result = bcrypt.checkpw(userBytes, hash)
    return result