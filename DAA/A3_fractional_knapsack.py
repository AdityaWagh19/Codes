# Practical 3: Fractional Knapsack

class Knapsack:
    def fractional_knapsack(self, capacity, items):
        items.sort(key=lambda x: x[0] / x[1], reverse=True)

        total_value = 0

        for value, weight in items:
            if capacity == 0:
                break

            if weight <= capacity:
                total_value += value
                capacity -= weight
            else:
                total_value += value * (capacity / weight)
                capacity = 0

        return total_value


def main():
    n = int(input("Enter number of items: "))

    items = []
    for i in range(n):
        value = int(input("Enter value: "))
        weight = int(input("Enter weight: "))
        items.append((value, weight))

    capacity = int(input("Enter capacity: "))

    obj = Knapsack()
    print("Maximum value:", obj.fractional_knapsack(capacity, items))


main()
