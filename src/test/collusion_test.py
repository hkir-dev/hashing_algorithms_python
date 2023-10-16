import unittest
import string
import random
import zlib
import binascii
import datetime


class HashingTests(unittest.TestCase):
    def test_collusion(self):
        barcodes = list()
        for i in range(100000):
            barcodes.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=100)))

        print(barcodes[0])
        print(barcodes[1])
        print(barcodes[2])
        print(barcodes[3])

        hashes = set()
        conflict_count = 0
        for barcode in barcodes:
            bhash = zlib.crc32(str.encode(barcode))
            if bhash in hashes:
                conflict_count += 1
            else:
                hashes.add(bhash)

        print("Conflict count: {}".format(conflict_count))

    def test_lib_performance(self):
        barcodes = list()
        for i in range(100000):
            barcodes.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=100)))

        start = datetime.datetime.now()
        for barcode in barcodes:
            zlib.crc32(str.encode(barcode))
        end = datetime.datetime.now()
        duration = end - start

        print("Zlib: {}".format(duration.microseconds))

        start = datetime.datetime.now()
        for barcode in barcodes:
            binascii.crc32(str.encode(barcode))
        end = datetime.datetime.now()
        duration = end - start

        print("binascii: {}".format(duration.microseconds))

