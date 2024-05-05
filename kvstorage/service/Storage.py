import json

from kvstorage.utils.crypto_handler.CryptoHandler import CryptoHandler
from kvstorage.utils.file_handler.FileHandler import FileHandler


class Storage():
    def __init__(self):
        self.file_handler = FileHandler()
        self.crypto_handler = CryptoHandler()

    def create_store(self, table):
        self.file_handler.create_file(f'data_store/{table}.json')
        print(f"Succesfully create {table}")
        return True

    def get_store(self, table):
        try:
            data = self.file_handler.read_json(f'data_store/{table}.json')
            print(data)
            return data
        except FileNotFoundError as e:
            print(f'{table} is not exists')

    def get_value_from_store(self, table, key):
        try:
            data = self.file_handler.read_key(f'data_store/{table}.json', key)
            print(self.crypto_handler.decompress_and_decode(data))
            return data
        except KeyError as e:
            print(f"Key {key} is not exists")
            return None

    def set_value_to_store(self, table, key, value):
        try:
            data = self.get_store(table)
            data[key] = self.crypto_handler.encode_and_compress(value)
            print(data[key])
            self.file_handler.write_file(f'data_store/{table}.json', json.dumps(data))
            print(f"Succesfully write in {table} with [{key}]={value}")
            return True
        except FileNotFoundError as e:
            print(f"{table} does not exists")
            return False

    def drop_store(self, table):
        try:
            status = self.file_handler.drop_file(f'data_store/{table}.json')
            if status: print(f"Succesfully dropped")
        except FileNotFoundError as e:
            return False
        return True

    def drop_all_stores(self):
        status = self.file_handler.drop_all('data_store')
        if status: print(f"Succesfully dropped all")
        return True
