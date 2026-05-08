class Counter:
    _instance = None  # Holds the single instance

    def __new__(cls):
        if cls._instance is None:
            print("Creating the instance...")
            cls._instance = super().__new__(cls)
            cls._instance.count = 0
        return cls._instance

    def increment(self):
        self.count += 1


# --- Demo ---

a = Counter()
b = Counter()

print(f"a is b: {a is b}")  # True — same object!

a.increment()
a.increment()
b.increment()

print(f"a.count: {a.count}")  # 3
print(f"b.count: {b.count}")  # 3 — because a and b are the same instance
