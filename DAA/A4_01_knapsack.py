# Practical 4: 0/1 Knapsack (Dynamic Programming)

# Practical 4: 0/1 Knapsack (Dynamic Programming)

def knapsack(weights, profits, capacity):
    n = len(weights)

    # Initialize DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]

            else:
                dp[i][w] = max(
                    dp[i - 1][w],
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]]
                )

    # Print DP Table
    print("\nDP Table:\n")

    print(f"{'Items/Capacity':<18}", end="")
    for w in range(capacity + 1):
        print(f"{w:<8}", end="")
    print()

    for i in range(n + 1):
        print(f"{i:<18}", end="")
        for w in range(capacity + 1):
            print(f"{dp[i][w]:<8}", end="")
        print()

    # Find selected items
    w = capacity
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weights[i - 1]

    selected_items.reverse()

    return dp[n][capacity], selected_items


# Main Program
weights = [3, 2, 4, 5, 1]
profits = [50, 40, 70, 80, 10]
capacity = 7

max_profit, items = knapsack(weights, profits, capacity)

print("\nMaximum Profit:", max_profit)
print("Selected Items:", items)