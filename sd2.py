class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # stores key -> value
        self.order = []  # maintains usage order (oldest at index 0)

    def get(self, key: int) -> int:
        """Retrieve item from cache and update usage order."""
        if key not in self.cache:
            print(f"❌ Miss: {key} not in cache")
            return -1  # key not found

        # Move key to the end (most recently used)
        self.order.remove(key)
        self.order.append(key)

        print(f"✅ Hit: {key} -> {self.cache[key]}")
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """Insert/update cache with LRU eviction."""
        if key in self.cache:
            # Update existing value
            self.cache[key] = value
            # Update order (move to end)
            self.order.remove(key)
            self.order.append(key)
            print(f"🔄 Update: {key} -> {value}")
        else:
            # If cache is full, evict least recently used (first item in order)
            if len(self.cache) >= self.capacity:
                lru_key = self.order.pop(0)
                del self.cache[lru_key]
                print(f"🗑️ Evicted LRU: {lru_key}")

            # Insert new key
            self.cache[key] = value
            self.order.append(key)
            print(f"➕ Insert: {key} -> {value}")

        def __repr__(self):
            """Show cache contents in usage order (LRU -> MRU)."""
            return "Cache: {" + ", ".join(f"{k}: {self.cache[k]}" for k in self.order) + "}"
    
    
    if __name__ == "__main__":
        lru = LRUCache(3)
    
        lru.put(1, "User1")
        lru.put(2, "User2")
        lru.put(3, "User3")
        print(lru)  # Cache: {1: User1, 2: User2, 3: User3}
    
        lru.get(2)  # Access User2 → moves it to most recent
        print(lru)  # Cache: {1: User1, 3: User3, 2: User2}
    
        lru.put(4, "User4")  # Cache is full → evicts LRU (User1)
        print(lru)  # Cache: {3: User3, 2: User2, 4: User4}
    
        lru.get(3)  # Access User3 → moves it to MRU
        print(lru)  # Cache: {2: User2, 4: User4, 3: User3}

