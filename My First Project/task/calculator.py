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

    staff_expenses = int(input("Staff expenses: "))
    other_expenses = int(input("Other expenses: "))

    net_income = income - (staff_expenses + other_expenses)
    print(f"Net income: ${net_income}")


main()
