class Auto:
    def __init__(self, ks_s, max_h, nomer):
        self.ks_s = ks_s
        self.max_h = max_h
        self.nomer = nomer

    def print_info(self):
        return (
            f" Кількість сидінь: {self.ks_s}"
            f" Макс. Швидкість: {self.max_h}"
            f" Номер: {self.nomer}"
        )


class Bus(Auto):
    def __init__(self, ks_s, mah_h, nomer, marsh):
        super().__init__(ks_s, mah_h, nomer)
        self.marsh = marsh

    def print_info(self):

        auto_print_info = super(Bus, self).print_info()
        return f"{auto_print_info}" f" Маршрут: {self.marsh}"


auto = Auto(4, 320, "BC777BK")
print(auto.print_info())
bus = Bus(28, 160, "ШКОЛЯРИК", "№29 Винники-Залізничний завод")
print(bus.print_info())
