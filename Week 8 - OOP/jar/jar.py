class Jar:
    def __init__(self, capacity=12):
        # Check if capacity is positive integer
        if isinstance(capacity, int) and capacity > 0:
                self._capacity = capacity
                self._cookies = 0
        else:
            raise ValueError("Jar Capacity must be positive integer")


    def __str__(self):
          return "🍪" * self._cookies


    def deposit(self, added_cookies):
        # Check if added_cookies is positive integer
        if not isinstance(added_cookies, int) or added_cookies < 0:
            raise ValueError("Invalid Cookies Number")
        # Check Cookies + Added cookies < Capacity
        if (self._cookies + added_cookies) > self._capacity:
            raise ValueError("Cookies exceed Jar capacity 🫗")

        # Deposit cookies in jar
        self._cookies += added_cookies


    def withdraw(self, removed_cookies):
        # Check if removed_cookies is positive integer
        if not isinstance(removed_cookies, int) or removed_cookies < 0:
            raise ValueError("Invalid Cookies Number")
        # Check Cookies - Removed cookies < Capacity
        if (self._cookies - removed_cookies) < 0:
            raise ValueError("No more cookies left 🥺")

        # Withdraw cookies from jar
        self._cookies -= removed_cookies


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies



def main():
    mostafa_jar = Jar()
    print(mostafa_jar)
    mostafa_jar.deposit(10)
    mostafa_jar.withdraw(5)
    print(mostafa_jar)


if __name__ == "__main__"
    main()


