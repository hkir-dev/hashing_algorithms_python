import binascii
import zlib
import uuid
import base64
import hashlib

text = "akhjsdfjl, akuendc, hiuahhas"
text_bytes = str.encode(text)

crc32_hash = binascii.crc32(text_bytes)

print("binascii CRC32: {}".format(crc32_hash))

print("Zlib CRC32: {}".format(zlib.crc32(text_bytes)))

print("CRC32 Hex: {}".format(hex(crc32_hash)))

print("CRC32 Hex str: {}".format('%x' % crc32_hash))

print("Zlib adler32: {}".format(zlib.adler32(text_bytes)))

print("Zlib adler32 hex: {}".format('%x' % zlib.adler32(text_bytes)))

uuid = str(uuid.uuid3(uuid.NAMESPACE_URL, text))

print("UUID: {}".format(uuid))

print("UUID base64: {}".format(base64.b64encode(str.encode(uuid))))

print("##### 64 bit hashing algorithms ######")

blake_hasher = hashlib.blake2b(text_bytes, digest_size=5)
print("Blake2b bytes: {}".format(blake_hasher.digest()))

blake_hex = blake_hasher.hexdigest()
print("Blake2b Hex: {}  ({})".format(blake_hex, len(blake_hex)))

blake_base64 = str(base64.urlsafe_b64encode(blake_hasher.digest()), 'UTF-8')
print("Blake2b base64: {} ({})".format(blake_base64, len(blake_base64)))



# OUT:
# binascii CRC32: 2510416923
# Zlib CRC32: 2510416923
# CRC32 Hex: 0x95a1ec1b
# CRC32 Hex str: 95a1ec1b
# Zlib adler32: 2546535024
# Zlib adler32 hex: 97c90a70





