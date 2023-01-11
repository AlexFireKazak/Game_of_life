class Elevator:
    def __init__(self, all_et=5, now_et=3):
        self.all_et = all_et
        self.now_et = now_et

    def up(self):
        if self.now_et + 1 <= self.all_et:
            self.now_et += 1
            print(f"Лифт поднимается на {self.now_et} этаж")
        else:
            print("Лифт не может подняться выше")

    def down(self):
        if self.now_et - 1 >= 1:
            self.now_et -= 1
            print(f"Лифт опускается на {self.now_et} этаж")
        else:
            print("Лифт не может опуститься ниже")