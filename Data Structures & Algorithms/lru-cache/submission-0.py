class LRUCache:

    def __init__(self, capacity: int):
        self.key_value = {}
        self.freq_key = defaultdict(int)
        self.queue = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.key_value:
            self.queue.append(key)
            self.freq_key[key] += 1
            return self.key_value[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        # print(f"put {key}, {value}")
        if key not in self.key_value and len(self.key_value) == self.capacity:
            # print(self.queue)
            while self.queue and self.freq_key[self.queue[0]]>1:
                self.freq_key[self.queue[0]] -= 1
                self.queue.popleft()
                # print(self.queue)
                # print(self.freq_key)
            if self.queue:
                key_to_remove = self.queue[0]
                # print(key_to_remove)
                del self.key_value[key_to_remove]
                self.freq_key[key_to_remove] -= 1
                self.queue.popleft()
        
        self.key_value[key] = value
        self.queue.append(key)
        self.freq_key[key] += 1
        

        


        
        

        
