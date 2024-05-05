import unittest

from kvstorage.service.Storage import Storage


class TestStorage(unittest.TestCase):
    def setUp(self):
        self.storage = Storage()

    def test_create_store(self):
        self.assertEqual(True, self.storage.create_store("test"))

    def test_get_store(self):
        self.assertEqual(self.storage.get_store("test"), True)

    def test_get_value_from_store(self):
        self.assertEqual(self.storage.get_value_from_store("test", "not exist key"), None)

    def test_set_value_to_store(self):
        self.assertEqual(self.storage.set_value_to_store("test", "test_key", 1), True)

    def test_get_value_from_store_exist_key(self):
        self.assertEqual(self.storage.get_value_from_store("test", "test_key"), 1)

    def test_drop_store(self):
        self.assertEqual(self.storage.drop_store("test"), True)

    def test_drop_store_not_exist(self):
        self.assertEqual(self.storage.drop_store("test"), False)


if __name__ == '__main__':
    unittest.main()
