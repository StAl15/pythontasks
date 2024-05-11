from abc import ABC, abstractmethod


class AbstractStorageManager(ABC):
    @abstractmethod
    def create_store(self, table_name):
        pass

    @abstractmethod
    def drop_store(self, table_name):
        pass

    @abstractmethod
    def read_store(self, table_name):
        pass
