def check_magic(magic):
    if magic != 779314790:
        return False
    return True

def check_version(version):
    supported = ('\x00', '\x00', '\x00', '\x01')
    i = 0
    for item in version:
        if version[i] != supported[i]:
            return False
        i += 1
    return True

def check_sff(stream):
    return True
