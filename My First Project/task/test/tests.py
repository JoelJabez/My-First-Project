from hstest import StageTest, TestedProgram, CheckResult, dynamic_test

# Bubblegum: $202.0
# Toffee: $118.0
# Ice cream: $2250.0
# Milk chocolate: $1680.0
# Doughnut: $1075.0
# Pancake: $80.0
#
# Income: $5405.0


class PrintFirstProject(StageTest):
    @dynamic_test()
    def test_first_project(self):
        pr = TestedProgram()

        output = pr.start().lower().strip()
        output_length = len(list(filter(None, output.splitlines())))
        if not output:
            return CheckResult.wrong("Your program didn't print any output.")
        elif output_length != 8:
            return CheckResult.wrong(f'Your program should output 8 lines, '
                                     f'but {output_length} lines were found.')

        if 'earned' not in output.lower():
            return CheckResult.wrong("Your program didn't print the 'Earned amount' line")
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
        elif 'income' not in output.lower():
            return CheckResult.wrong("Your program should print the income on a separate line")
        elif '202' not in output.lower():
            return CheckResult.wrong("Incorrect earned amount for Bubblegum")
        elif '118' not in output.lower():
            return CheckResult.wrong("Incorrect earned amount for Toffee")
        elif '2250' not in output.lower():
            return CheckResult.wrong("Incorrect earned amount for Ice Cream")
        elif '1680' not in output.lower():
            return CheckResult.wrong("Incorrect earned amount for Milk chocolate")
        elif '1075' not in output.lower():
            return CheckResult.wrong("Incorrect earned amount for Doughnut")
        elif '80' not in output.lower():
            return CheckResult.wrong("Incorrect earned amount for Pancake")
        elif '5405' not in output.lower():
            return CheckResult.wrong("Incorrect total income!")
        else:
            return CheckResult.correct()


if __name__ == '__main__':
    PrintFirstProject().run_tests()
