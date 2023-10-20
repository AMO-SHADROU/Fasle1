def hanoi(n, source, auxiliary, destination):
    if n > 0:
        # انتقال n-1 مهره از میله اولیه به میله کمکی با استفاده از میله نهایی به عنوان میله کمکی
        hanoi(n - 1, source, destination, auxiliary)

        # چاپ حرکت لازم برای انتقال مهره n از میله اولیه به میله نهایی
        print(f"انتقال مهره {n} از میله {source} به میله {destination}")

        # انتقال n-1 مهره از میله کمکی به میله نهایی با استفاده از میله اولیه به عنوان میله کمکی
        hanoi(n - 1, auxiliary, source, destination)