import linecache
import os

from kvstorage.entities.AbstractStorage import AbstractStorage


class Storage(AbstractStorage):
    def __init__(self, table_name=""):
        if os.path.exists(f'data_store/{table_name}.txt'):
            with open(f'data_store/{table_name}.txt', 'br+') as f:
                self.size = len(f.readlines())
        else:
            my_file = open(f"data_store/{table_name}.txt", "w+")
            my_file.write("")
            my_file.close()
            self.size = 0
        self.table_name = table_name

    async def remove(self, key):
        with open(f'data_store/{self.table_name}.txt', 'bw+') as f:
            f.seek(self._compute_index(key))
            f.write(b"")
            self.size -= 1

    async def set(self, key, value):
        with open(f'data_store/{self.table_name}.txt', 'bw+') as f:
            f.seek(self._compute_index(key))
            f.write(f'{key} {value}'.encode())
            self.size += 1

    def _compute_index(self, key):
        rs_key = sum([ord(i) for i in str(key)])
        rs = rs_key % (self.size + 1)
        print(rs, key, rs_key)
        return rs

    async def get(self, key):
        index = self._compute_index(key)
        value = linecache.getline(f'data_store/{self.table_name}.txt', index)
        return value if value else None
