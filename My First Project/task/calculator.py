def main():
    items = {"Bubblegum": 202, "Toffee": 118,
             "Ice cream": 2250, "Milk chocolate": 1680,
             "Doughnut": 1075, "Pancake": 80}

    income = 0.0
    print("Earned amount:")
    for item in items:
        print(f"{item}: ${items[item]}")
        income += items[item]

    print(f"\nIncome: ${income}")


main()
