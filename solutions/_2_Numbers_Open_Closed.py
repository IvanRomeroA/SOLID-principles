class Numbers:
    @staticmethod
    def compare_two_numbers(a: int, b: int) -> int:
        return max(a, b)

    def compare_three_numbers(self, a: int, b: int, c: int) -> int:
        bigger = self.compare_two_numbers(a, b)
        bigger = self.compare_two_numbers(bigger, c)
        return bigger
