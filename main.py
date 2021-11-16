

class Auto():
    def __init__(self, ks_s, max_h, nomer):
        self.ks_s = ks_s
        self.max_h = max_h
        self.nomer = nomer

a = Auto(4, 305, 'BC777BK')

print('Кількість сидінь:',a.ks_s, 'Максимальна швидкість:',a.max_h, 'Номера авто:', a.nomer, sep='\n')
