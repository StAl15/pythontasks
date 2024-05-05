import json
import shutil
import os
from json import JSONDecodeError

import ijson

from kvstorage.utils.crypto_handler.CryptoHandler import CryptoHandler


class FileHandler():
    def __init__(self):
        self.crypto_handler = CryptoHandler()

    def read_json(self, filename):
        with open(filename) as f:
            try:
                content = json.load(f)
                return content
            except JSONDecodeError as e:
                print(f'Incorrect json file {filename}')
            except FileNotFoundError as e:
                print("File not found")

    def read_key(self, filename, key):
        with open(filename) as f:
            data = ijson.items(f, key)
            jsons = [i for i in data]
            return self.crypto_handler.decompress_and_decode(jsons[0])

    def write_file(self, filename, data):
        with open(filename, 'w+') as f:
            try:
                status = f.write(data)
                if status:
                    print(f"Successfully added data")
                else:
                    print(f"Something went wrong")
            except JSONDecodeError as e:
                print(f'Incorrect json file {filename}')

    def drop_file(self, filename):
        try:
            os.remove(filename)
            return True
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

    def drop_all(self, dirname):
        try:
            shutil.rmtree(dirname)
            return True
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
            return False

    def create_file(self, filename):
        with open(filename, 'w') as f:
            f.write(json.dumps({}))
        return True
