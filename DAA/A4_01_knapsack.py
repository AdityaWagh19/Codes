# Practical 4: 0/1 Knapsack (Dynamic Programming)

def build_knapsack_dp(values, weights, n, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp


def print_dp_table(dp, n, capacity):
    print("\nDP Table:")
    print("   ", end="")
    for w in range(capacity + 1):
        print(f"{w:4}", end="")
    print()

    for i in range(n + 1):
        print(f"{i:2} ", end="")
        for w in range(capacity + 1):
            print(f"{dp[i][w]:4}", end="")
        print()


values = []
weights = []
n = 0

while True:
    print("\n=== 0/1 Knapsack Menu ===")
    print("1. Enter Items")
    print("2. Solve 0/1 Knapsack")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of items: "))
        values = []
        weights = []

        for i in range(n):
            value = int(input(f"Item {i+1} value: "))
            weight = int(input(f"Item {i+1} weight: "))
            values.append(value)
            weights.append(weight)

    elif choice == 2:
        if n == 0:
            print("Please enter items first!")
            continue

        capacity = int(input("Enter knapsack capacity: "))

        dp = build_knapsack_dp(values, weights, n, capacity)
        print_dp_table(dp, n, capacity)

        print("\nMaximum value that can be put in knapsack:",
              dp[n][capacity])

    elif choice == 3:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice!")
