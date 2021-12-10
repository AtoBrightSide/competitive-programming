def solution():
    n, m, a = input("").split(" ")
    n, m, a = int(n), int(m), int(a)
    return (m // a + (1 if m % a != 0 else 0)) * (
        n // a + (1 if n % a != 0 else 0)) if n * m > a * a else 1


print(solution())