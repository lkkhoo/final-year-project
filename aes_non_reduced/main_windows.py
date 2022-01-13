from Crypto.Cipher import AES
from PIL import Image
import os
# from Crypto.Util.Padding import pad, unpad
from secrets import token_bytes

key = token_bytes(16)


def pad(data):
    padSize = 16 - len(data) % 16
    return data + b"\x00" * (16 - len(data) % 16), padSize


def convert_to_RGB(data):
    r, g, b = tuple(map(lambda d: [data[i] for i in range(0, len(data)) if i % 3 == d], [0, 1, 2]))
    pixels = tuple(zip(r, g, b))
    return pixels


# This way of encryption is to show the pattern in the cipher text of ecb mode
def ctrEncryptedPattern(filename, outputFileName, format):
    # Opens image and converts it to RGB format for PIL
    im = Image.open(filename)
    data = im.convert("RGB").tobytes()

    # Since we will pad the data to satisfy AES's multiple-of-16 requirement, we will store the original data length and "unpad" it later.
    original = len(data)

    # Encrypts using desired AES mode (we'll set it to ECB by default)
    data, padSize = pad(data)
    new = convert_to_RGB(aes_ctr_encrypt(key, data)[:original])

    # Create a new PIL Image object and save the old image data into the new image.
    im2 = Image.new(im.mode, im.size)
    im2.putdata(new)

    # Save image
    if format == "jpg" or format == "JPG":
        format = "JPEG"
    im2.save(outputFileName, format)


def aes_ctr_encrypt(key, data, mode=AES.MODE_CTR):
    nonce = token_bytes(8)
    aes = AES.new(key, mode, nonce=nonce)
    new_data = aes.encrypt(data)
    return new_data


# Read the images bytes
def openImage(path):
    image = open(path, 'rb')
    data = image.read()
    image.close()
    return data


# Save the encrypted or decrypted image
def saveImage(path="./images_encrypted/", name="", data=""):
    newImage = open(path + name, 'wb')
    newImage.write(data)
    newImage.close


# Encrypting the image with ecb
def ecbEncrypt(msg, path, name):
    cipher = AES.new(key, AES.MODE_ECB)
    data, padSize = pad(msg)
    cipherText = cipher.encrypt(data)

    saveImage(path, name, cipherText)

    return cipherText, padSize


# Decrypting the imsge with ecb
def ecbDecrypt(msg, path, name, padSize):
    plain = AES.new(key, AES.MODE_ECB)
    plainText = plain.decrypt(msg)
    saveImage(path, name, plainText[:-padSize])
    return plainText


# Encrypting the image with cbc
def cbcEncrypt(msg, path, name):
    iv = token_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data, padSize = pad(msg)
    cipherText = cipher.encrypt(data)
    saveImage(path, name, cipherText)
    return cipherText, iv, padSize


# Decrypting the image with cbc
def cbcDecrypt(msg, iv, path, name, padSize):
    plain = AES.new(key, AES.MODE_CBC, iv)
    plainText = plain.decrypt(msg)
    saveImage(path, name, plainText[:-padSize])
    return plainText


# Encrypting the image with ctr
def ctrEncrypt(msg, path, name):
    nonce = token_bytes(8)
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    data, padSize = pad(msg)
    cipherText = cipher.encrypt(data)
    saveImage(path, name, cipherText)
    return cipherText, padSize, nonce


# Decrypting the image with ctr
def ctrDecrypt(msg, path, name, padSize, nonce):
    plain = AES.new(key, AES.MODE_CTR, nonce=nonce)
    plainText = plain.decrypt(msg)
    saveImage(path, name, plainText[:-padSize])
    return plainText


def encryptAndDecryptWithAllModes(path):
    imageData = openImage(path)
    name = path.split('.')
    saveEncryptionPath = os.getcwd() + "\\images_encrypted\\"
    encryptedName = name[0].split('\\')[-1] + '_encrypted.' + name[-1]

    ctrEncryptedPattern(path, saveEncryptionPath + "ctr_pattern_" + encryptedName, name[-1])
    ecbCipherText, ecbPadSize = ecbEncrypt(imageData, saveEncryptionPath, "ecb" + encryptedName)
    cbcCipherText, iv, cbcPadSize = cbcEncrypt(imageData, saveEncryptionPath, "cbc" + encryptedName)
    ctrCipherText, ctrPadSize, nonce = ctrEncrypt(imageData, saveEncryptionPath, "ctr" + encryptedName)

    saveDecryptonPath = os.getcwd() + "\\images_decrypted\\"
    decryptedName = name[0].split('\\')[-1] + '_decrypted.' + name[-1]
    ecbDecrypt(ecbCipherText, saveDecryptonPath, "ecb" + decryptedName, ecbPadSize)
    cbcDecrypt(cbcCipherText, iv, saveDecryptonPath, "cbc" + decryptedName, cbcPadSize)
    ctrDecrypt(ctrCipherText, saveDecryptonPath, "ctr" + decryptedName, ctrPadSize, nonce)


path = input("Enter the path of your image: ")

encryptAndDecryptWithAllModes(path)
