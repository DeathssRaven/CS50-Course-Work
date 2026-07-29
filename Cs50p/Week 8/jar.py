class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        if self.capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        added_cookies = self.size + n
        if added_cookies > self.capacity:
            raise ValueError("Cannot deposit more cookies than the jar's capacity")
        self.size = added_cookies
        return self.size

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Size must be a non-negative integer")
        self._size = size


def main():
    jar = Jar()
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(2)
    print(jar)


if __name__ == "__main__":
    main()
