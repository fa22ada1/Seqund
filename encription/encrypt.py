from cryptography.fernet import Fernet

def callKey():
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    return fernet

def encrypt(flpath):
    fernet=callKey()
    with open(flpath, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(flpath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    return

def decrypt(flpath):
    fernet=callKey()
    with open(flpath, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(flpath, 'wb') as dec_file:
        dec_file.write(decrypted)
    return