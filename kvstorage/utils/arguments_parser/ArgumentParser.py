import argparse
import sys

from kvstorage.service.Storage import Storage


class ArgumentParser():
    def __init__(self):
        self.storage_handler = Storage()
        self.parser = argparse.ArgumentParser()
        self.subparsers = self.parser.add_subparsers()

        self.add_set_value_parser()
        self.add_create_table()
        self.add_get_value_parser()
        self.add_drop_table()
        self.add_drop_all()
        self.add_exit()
        self.add_get_table_parser()

    def add_get_table_parser(self):
        parser_get = self.subparsers.add_parser('get_table')
        parser_get.add_argument('--table', required=True)
        parser_get.set_defaults(func=self.storage_handler.get_store)

    def add_get_value_parser(self):
        parser_get = self.subparsers.add_parser('get_value')
        parser_get.add_argument('--key', required=True)
        parser_get.add_argument('--table', required=True)
        parser_get.set_defaults(func=self.storage_handler.get_value_from_store)

    def add_set_value_parser(self):
        parser_get = self.subparsers.add_parser('set')
        parser_get.add_argument('--key', required=True)
        parser_get.add_argument('--value', required=True)
        parser_get.add_argument('--table', required=True)
        parser_get.set_defaults(func=self.storage_handler.set_value_to_store)

    def add_create_table(self):
        parser_get = self.subparsers.add_parser('create_table')
        parser_get.add_argument('--table', required=True)
        parser_get.set_defaults(func=self.storage_handler.create_store)

    def add_drop_table(self):
        parser_get = self.subparsers.add_parser('drop_table')
        parser_get.add_argument('--table', required=True)
        parser_get.set_defaults(func=self.storage_handler.drop_store)

    def add_drop_all(self):
        parser_get = self.subparsers.add_parser('drop_all')
        parser_get.set_defaults(func=self.storage_handler.drop_all_stores)

    def add_exit(self):
        parser_get = self.subparsers.add_parser('exit')
        parser_get.set_defaults(func=lambda: sys.exit())

    def read_args(self):
        args = self.parser.parse_args()
        return args
