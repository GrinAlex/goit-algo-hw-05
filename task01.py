class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            temp_list = []
            temp_key = None
            temp_value = None
            for pair in self.table[key_hash]:
                if pair[0] != key:
                    temp_list.append([pair[0], pair[1]])
                else:
                    temp_key, temp_value = pair[0], pair[1]
            self.table[key_hash] = temp_list
            return [temp_key, temp_value]   # return deleted key, value from HashTable
        return None


# Тестуємо нашу хеш-таблицю:
# H = HashTable(5)
# H.insert("apple1", 10)
# H.insert("orange1", 20)
# H.insert("banana1", 30)
# H.insert("apple2", 50)
# H.insert("orange2", 60)
# H.insert("banana2", 70)

# print(H.table)

# H.delete("banana2")
# print(H.table)
