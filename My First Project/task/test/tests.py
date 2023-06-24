from hstest import StageTest, TestedProgram, CheckResult, dynamic_test


# Bubblegum: $2
# Toffee: $0.2
# Ice cream: $5
# Milk chocolate: $4
# Doughnut: $2.5
# Pancake: $3.2


class PrintFirstProject(StageTest):
    @dynamic_test()
    def test_first_project(self):
        pr = TestedProgram()

        output = pr.start().lower().strip()
        output_length = len(list(filter(None, output.splitlines())))
        if not output:
            return CheckResult.wrong("Your program didn't print any output.")
        elif output_length != 7:
            return CheckResult.wrong(f'Your program should output 7 lines, '
                                     f'but {output_length} lines were found.')

        if 'prices' not in output.lower():
            return CheckResult.wrong("Your program didn't print the 'Prices:' line")
        elif 'bubblegum' not in output.lower():
            return CheckResult.wrong("Your program should print the 'Bubblegum' as an item")
        elif 'toffee' not in output.lower():
            return CheckResult.wrong("Your program should print the 'Toffee' as an item")
        elif 'ice cream' not in output.lower():
            return CheckResult.wrong("Your program should print the 'Ice Cream' as an item")
        elif 'milk chocolate' not in output.lower():
            return CheckResult.wrong("Your program should print the 'Milk chocolate' as an item")
        elif 'doughnut' not in output.lower():
            return CheckResult.wrong("Your program should print the 'Doughnut' as an item")
        elif 'pancake' not in output.lower():
            return CheckResult.wrong("Your program should print the 'Pancake' as an item")
        elif '2' not in output.lower():
            return CheckResult.wrong("Incorrect price for Bubblegum")
        elif '0.2' not in output.lower():
            return CheckResult.wrong("Incorrect price for Toffee")
        elif '5' not in output.lower():
            return CheckResult.wrong("Incorrect price for Ice cream")
        elif '4' not in output.lower():
            return CheckResult.wrong("Incorrect price for Milk chocolate")
        elif '2.5' not in output.lower():
            return CheckResult.wrong("Incorrect price for Doughnut")
        elif '3.2' not in output.lower():
            return CheckResult.wrong("Incorrect price for Pancake")
        else:
            return CheckResult.correct()


if __name__ == '__main__':
    PrintFirstProject().run_tests()