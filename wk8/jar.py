class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        return("🍪" * self.size)


    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Deposit cannot be greater than capacity")
        else:
            self.size += n


    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Withdraw cannot be greater than deposit")
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Number is negative")
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size=0):
        if size < 0:
            raise ValueError("Size cannot be negative")
        else:
            self._size = size


def main():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(1)
    print(jar)


if __name__ == "__main__":
    main()
