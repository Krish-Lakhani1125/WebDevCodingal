class Expression:
    def __init__(self, num1, num2, num3):

        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def calculate_addition(self):

        total_sum = self.num1 + self.num2 + self.num3
        print(f"The sum of {self.num1}, {self.num2}, and {self.num3} is: {total_sum}")


expression1 = Expression(10, 20, 30)

print("Calculation for expression1:")
expression1.calculate_addition()

print("-" * 20)

expression2 = Expression(1.5, 2.75, 5.0)

print("Calculation for expression2:")
expression2.calculate_addition()
