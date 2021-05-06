class Dictionary:
    def __init__(self, max_collision_ratio=0.7, initial_capacity=10):
        self.capacity = initial_capacity
        self.max_collision_ration = max_collision_ratio
        self.collisions = 0
        self.table = [[] for i in range(self.capacity)]

    def __getitem__(self, key):
        index = hash(key) % self.capacity
        bucket = self.table[index]
        for tuple_ in bucket:
            if tuple_[0] == key:
                return tuple_[1]
        raise KeyError

    def enlarge(self):
        pass

    def insert(self, key, value):
        """
        Insert a key and its value into the dictionary
        :param key: any
        :param value: any
        :return: None
        """
        index = hash(key) % self.capacity
        bucket = self.table[index]
        if len(bucket) == 0:
            bucket.append((key, value))
        else:
            self.collisions += 1
            # If they key already exists, replace the value with the new one
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    bucket[i] = (key, value)
                    break


