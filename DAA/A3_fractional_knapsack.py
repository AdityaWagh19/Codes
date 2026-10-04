# Practical 3: Fractional Knapsack

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight


items = []

while True:
    print("\n=== Fractional Knapsack Menu ===")
    print("1. Enter items")
    print("2. Solve Fractional Knapsack")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        items.clear()
        n = int(input("Enter number of items: "))

        for i in range(n):
            value = int(input(f"Item {i+1} value: "))
            weight = int(input(f"Item {i+1} weight: "))
            items.append(Item(value, weight))

    elif choice == 2:
        if len(items) == 0:
            print("Please enter items first!")
            continue

        capacity = int(input("Enter knapsack capacity: "))

        # Sort by value/weight ratio (descending)
        items.sort(key=lambda x: x.ratio, reverse=True)

        total_value = 0
        remaining = capacity

        print("\nItems taken:")

        for item in items:
            if remaining == 0:
                break

            if item.weight <= remaining:
                print(f"Value={item.value}, Weight={item.weight} -> Full")
                total_value += item.value
                remaining -= item.weight
            else:
                fraction = remaining / item.weight
                print(f"Value={item.value}, Weight={item.weight} -> {fraction*100:.2f}%")
                total_value += item.value * fraction
                remaining = 0

        print(f"\nMaximum Total Value = {total_value:.2f}")

    elif choice == 3:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice!")
