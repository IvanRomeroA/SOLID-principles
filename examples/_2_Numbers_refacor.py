# "Refactorización"
# Agregando una extensión para validar ahora 3 números.
class Numbers:
    @staticmethod
    def compare_two_or_three_numbers(a: int, b: int, c: int = None) -> int:
        bigger = b
        if a > bigger:
            bigger = a
        return max(c, bigger)
