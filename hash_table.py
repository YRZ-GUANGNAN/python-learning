class HashTable:
    def __init__(self):
        self.size = 10

        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        """把 key 转成一个 0~9 的下标"""

        return hash(key) % self.size

    def put(self, key, value):
        """存入"""
        i = self._hash(key)
        bucket = self.buckets[i]


        for index, (k, v) in enumerate(bucket):
            if k == key:

                bucket[index] = (key, value)
                return


        bucket.append((key, value))

    def get(self, key):
        """取出，没有返回 None"""
        i = self._hash(key)
        bucket = self.buckets[i]


        for k, v in bucket:
            if k == key:
                return v


        return None



if __name__ == "__main__":
    h = HashTable()
    h.put("name", "小明")
    h.put("age", 20)
    h.put("city", "湛江")

    print(h.get("name"))
    print(h.get("age"))
    print(h.get("xxx"))