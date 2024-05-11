class HashTable:
    def __init__(self, size=1009):
        self.size = size
        self.buckets = [None] * size
        self.values = []

    def put(self, key, value):
        index = self._compute_index(key)
        if self.buckets[index] is None:
            self.buckets[index] = [key]
            self.values.append((key, value))
        else:
            for i, k in enumerate(self.buckets[index]):
                if k == key:
                    self.values[i] = (k, value)
                    return
            self.buckets[index].append(key)
            self.values.append((key, value))

    def get(self, key):
        index = self._compute_index(key)
        for i, k in enumerate(self.buckets[index]):
            print(i, k)
            if k == key:
                return self.values[i][1]
        return None

    def _compute_index(self, key):
        return abs(hash(key)) % self.size

    def remove(self, key):
        index = self._compute_index(key)
        for i, k in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]
                del self.values[i]
                break

    def contains(self, key):
        index = self._compute_index(key)
        for k in self.buckets[index]:
            if k == key:
                return True
        return False

    def __repr__(self):
        return f"HashTable(buckets={[self.buckets]}, values={self.values})"


# Пример использования
# ht = HashTable()
# ht.put("hello", "world")
# ht.put("elloh", "dlrow")
# ht.put("1231231", "aaaaaaa")
#
#
# print(ht.get("hello"))  # должно вывести "world"
# print(ht.get("elloh"))  # должно вывести "dlrow"
# print(ht.get("1231231"))  # должно вывести "dlrow"

# print(ht)  # должно вывести HashTable(buckets=[['hello']], values=[('hello', 'world')])
# print(hash('123') % 100)
# print(hash("helli") % 100)
