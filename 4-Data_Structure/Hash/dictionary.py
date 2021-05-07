class Dictionary:
    def __init__(self, max_collision=3, initial_capacity=2):
        self.capacity = initial_capacity
        self.MAX_COLLISION = max_collision
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
        self.capacity *= 2
        self.collisions = 0
        tmp_table = self.table
        self.table = [[] for i in range(self.capacity)]
        for bucket in tmp_table:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self, key, value):
        """
        Insert a key and its value into the dictionary
        :param key: any
        :param value: any
        :return: None
        """
        index = hash(key) % self.capacity
        print('index = ', index)
        bucket = self.table[index]
        if len(self.table[index]) == 0:
            self.table[index].append((key, value))
        else:
            # If they key already exists, replace the value with the new one
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    bucket[i] = (key, value)
                    return
            bucket.append((key, value))
            self.collisions = max(self.collisions, len(bucket))
        if self.collisions > self.MAX_COLLISION:
            self.enlarge()

