import unittest
import string
import random
import zlib
import binascii
import datetime
import hashlib
import base64


class HashingTests(unittest.TestCase):
    def test_collusion(self):
        barcodes = list()
        for i in range(100000000):
            barcodes.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=100)))

        print(barcodes[0])
        print(barcodes[1])
        print(barcodes[2])
        print(barcodes[3])

        hashes = set()
        lens = set()
        conflict_count = 0
        for barcode in barcodes:
            bhash = '%x' % zlib.crc32(str.encode(barcode))
            if bhash in hashes:
                conflict_count += 1
            else:
                hashes.add(bhash)
            if len(bhash) not in lens:
                lens.add(len(bhash))

        print("Conflict count crc32: {}".format(conflict_count))
        print("Hash lengths: {}".format(lens))

        hashes = set()
        lens = set()
        conflict_count = 0
        for barcode in barcodes:
            blake_hasher = hashlib.blake2b(str.encode(barcode), digest_size=6)
            # bhash = base64.urlsafe_b64encode(blake_hasher.digest())
            bhash = blake_hasher.hexdigest()
            if bhash in hashes:
                conflict_count += 1
            else:
                hashes.add(bhash)
            if len(bhash) not in lens:
                lens.add(len(bhash))

        print("Conflict count blake2b: {}".format(conflict_count))
        print("Hash lengths: {}".format(lens))

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

        start = datetime.datetime.now()
        for barcode in barcodes:
            hashlib.blake2b(str.encode(barcode), digest_size=5).digest()
        end = datetime.datetime.now()
        duration = end - start

        print("blake2b: {}".format(duration.microseconds))

