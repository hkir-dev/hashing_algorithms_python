import binascii
import zlib

text = "akhjsdfjl, akuendc, hiuahhas"
text_bytes = str.encode(text)

crc32_hash = binascii.crc32(text_bytes)

print("binascii CRC32: {}".format(crc32_hash))

print("Zlib CRC32: {}".format(zlib.crc32(text_bytes)))

print("CRC32 Hex: {}".format(hex(crc32_hash)))

print("CRC32 Hex str: {}".format('%x' % crc32_hash))

print("Zlib adler32: {}".format(zlib.adler32(text_bytes)))

print("Zlib adler32 hex: {}".format('%x' % zlib.adler32(text_bytes)))


# OUT:
# binascii CRC32: 2510416923
# Zlib CRC32: 2510416923
# CRC32 Hex: 0x95a1ec1b
# CRC32 Hex str: 95a1ec1b
# Zlib adler32: 2546535024
# Zlib adler32 hex: 97c90a70
