# A Private project by Walter
#
# Groove Coaster mobile encryption/decryption script

from Crypto.Cipher import AES

"""
These values were found in libtune.so
which is present in the .apk file of gc android
"""

# Found in: mtxc::ObbFile::getZipPassword()
# Used for: Decrypting the zip files containing audio and chart data
ZIP_PASSWORD = "eiprblFFv69R83J5"

# Found in: aesManager::initialize()
# Used for: Decrypting parameter bytes sent by client and possibly more
AES_CBC_KEY = b"oLxvgCJjMzYijWIldgKLpUx5qhUhguP1"

# Found in: aesManager::decryptCBC() and aesManager::encryptCBC()
# Used for: Decrypting parameter bytes sent by client and possibly more
AES_CBC_IV = b"6NrjyFU04IO9j9Yo"


# Decrypt AES encrypted data, takes in a string or ordinal list
def decryptAES(data, key=AES_CBC_KEY, iv=AES_CBC_IV):
    data = hexToString(data)
    return AES.new(key, AES.MODE_CBC, iv).decrypt(data).strip(" ")

# Encrypt data with AES, takes in a string
def encryptAES(data, key=AES_CBC_KEY, iv=AES_CBC_IV):
    # Add trailing spaces
    data += " "*(16 - len(data) % 16)
    encryptedData = AES.new(key, AES.MODE_CBC, iv).encrypt(data)
    return stringToHex(encryptedData)

# Decrypt PAK files
def decryptPAK():
    raise NotImplementedError

# Encrypt PAK files
def encryptPAK():
    raise NotImplementedError


########### Utilities ###########

# Converts string hex, e.g: "E62A9D" into a bytes list
def hexToString(hexStr):
    if len(hexStr) % 2 == 0:
        return "".join([chr(int(hexStr[i*2:(i*2)+2], 16))
                      for i in range(int(len(hexStr) / 2))])
    raise Exception("hexToString() got a non-divisible-by-2 string")

# Converts a string to string hex like "E62A9D"
def stringToHex(string):
    return "".join([format(ord(char), "02X")
                    for char in string
                    ]).upper()

