import pickle
import zlib


class CryptoHandler:
    def __init__(self):
        pass

    @staticmethod
    def decode(elem):
        rs = pickle.loads(elem)
        return rs

    @staticmethod
    def decompress(element):
        rs = zlib.decompress(element)
        return rs

    @staticmethod
    def encode(element):
        rs = hash(element)
        return rs

    @staticmethod
    def compress(element):
        rs = zlib.compress(element)
        return rs
