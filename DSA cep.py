import matplotlib.pyplot as plt
class Doubly_LL:
    def __init__(self, data) -> None:
        self.prev = None
        self.next = None
        self.data = data

    def insert_after_head(self, node):
        node.next = self.next
        node.prev = self
        self.next.prev = node
        self.next = node

    def delete_node(self, node_ad):
        if node_ad.prev:
            node_ad.prev.next = node_ad.next
        if node_ad.next:
            node_ad.next.prev = node_ad.prev
        node_ad.prev = None
        node_ad.next = None
        return node_ad.data


class LRU:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.head = Doubly_LL((-1, -1))
        self.tail = Doubly_LL((-1, -1))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = {}
        self.count = 0
        self.total_accesses = 0
        self.miss_count = 0
        self.cumulative_accesses = 0
        self.cumulative_misses = 0
        self.miss_rates = []

    def put(self, key, value):
        self.total_accesses += 1
        self.cumulative_accesses += 1  # Increment cumulative accesses

        if key in self.dic:
            # Cache hit: Update value and move to the front
            node_ad = self.dic[key]
            node_ad.data = (key, value)
            self.head.delete_node(node_ad)
            self.head.insert_after_head(node_ad)
        else:
            # Cache miss
            self.miss_count += 1
            self.cumulative_misses += 1  # Increment cumulative misses

            if self.count == self.capacity:
                # Remove the least recently used item if the cache is full
                lru_key = self.tail.prev.data[0]
                self.tail.delete_node(self.tail.prev)
                del self.dic[lru_key]
                self.count -= 1

            # Add the new node to the front
            new_node = Doubly_LL((key, value))
            self.head.insert_after_head(new_node)
            self.dic[key] = new_node
            self.count += 1

        current_miss_rate = self.miss_rate()
        self.miss_rates.append(current_miss_rate)

    def get(self, key):
        self.total_accesses += 1
        self.cumulative_accesses += 1  # Increment cumulative accesses

        if key not in self.dic:
            self.miss_count += 1
            self.cumulative_misses += 1  # Increment cumulative misses
            return -1

        # Cache hit: Move the accessed node to the front
        node_ad = self.dic[key]
        self.head.delete_node(node_ad)
        self.head.insert_after_head(node_ad)
        return node_ad.data[1]

    def miss_rate(self):
        """Calculates the miss rate for the current run."""
        if self.total_accesses == 0:
            return 0.0
        return (self.miss_count / self.total_accesses)*100

    def cumulative_miss_rate(self):
        """Calculates the cumulative miss rate across all runs."""
        if self.cumulative_accesses == 0:
            return 0.0
        return self.cumulative_misses / self.cumulative_accesses

    def plot_miss_rate(self):
        """Plot the miss rate over time using matplotlib."""
        plt.plot(self.miss_rates, label="Miss Rate")
        plt.xlabel('Operations')
        plt.ylabel('Miss Rate')
        plt.title('Miss Rate Over Time')
        plt.legend()
        plt.show()

    def print_LRU(self):
        a = self.head.next
        while a != self.tail:
            print(a.data, end=" <-> ")
            a = a.next
        print("END")


    
# l=LRU(2)
# l.put(1,1)
# l.put(2,2)
# l.print_LRU()
# print(l.get(1))
# l.print_LRU()
# l.put(3,3)
# l.print_LRU()
# print(l.get(2))
# l.put(4, 4)
# l.print_LRU()
# print(l.get(1))
# print(l.get(3))
# print(l.get(4))
#
#
# l.plot_miss_rate()


# Create an LRU Cache with capacity 50
capacity = 50
lru_cache = LRU(capacity)

# # Fill the cache with keys 0-49 and values 0-49
for i in range(50):
    lru_cache.put(i, i)
print("Final LRU Cache State:")
lru_cache.print_LRU()
print("Final Miss Rate:", lru_cache.miss_rate())
#



# Retrieve the odd-numbered keys from the cache
#
for i in range(1, 50, 2):
    lru_cache.get(i)
print("Final LRU Cache State:")
lru_cache.print_LRU()
print("Final Miss Rate:", lru_cache.miss_rate())




# Fill the cache with prime number keys (0-100) and their values


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [i for i in range(101) if is_prime(i)]

for prime in prime_numbers:
    lru_cache.put(prime, prime)

# Print the LRU cache content
print("Final LRU Cache State:")
lru_cache.print_LRU()

# Compute and print the final miss rate
print("\nFinal Miss Rate:", lru_cache.miss_rate())

# # Plot the miss rate over time
lru_cache.plot_miss_rate()





























