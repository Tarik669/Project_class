class Auto:
    def __init__(self, ks_s, max_h, nomer):
        self.ks_s = ks_s
        self.max_h = max_h
        self.nomer = nomer


a = Auto(4, 305, "BC777BK")

print(
    "Інформація про автомобіль",
    "Кількість сидінь:",
    a.ks_s,
    "Максимальна швидкість:",
    a.max_h,
    "Номера авто:",
    a.nomer,
    sep="\n",
)


class Bus:
    def __init__(self, ks_s1, max_h1, nomer1, marsh):
        self.ks_s1 = ks_s1
        self.max_h1 = max_h1
        self.nomer1 = nomer1
        self.marsh = marsh


b = Bus(28, 160, "ABOBUS", "29 Винники-Залізничий Вокзал")

print(
    "Інформація про автобус",
    "Кількість сидінь:",
    b.ks_s1,
    "Максимальна швидкість:",
    b.max_h1,
    "Номера автобуса:",
    b.nomer1,
    "Маршрут автобуса №",
    b.marsh,
    sep="\n",
)
