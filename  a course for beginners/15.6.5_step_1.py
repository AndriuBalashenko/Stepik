# В саду 88_n
#   фруктовых деревьев, из них 32_n  яблони,
#   22_n груши, 16_n слив и 17_n вишен. В какой системе счисления посчитаны деревья?
#
# Примечание. Переведите числа из n-ой системы счисления в десятичную и составьте уравнение.

print(*[n for n in range(100) if 3 * n + 2 + 2 * n + 2 + n + 6 + n + 7 == 8 + 8 * n])