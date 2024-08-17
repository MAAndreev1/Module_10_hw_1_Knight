from threading import Thread
import time


class Knight(Thread):
    enemy = 100
    days = 0

    def __init__(self, name, power):
        self.name_knight = name
        self.power_knight = power
        super().__init__()

    def run(self):
        print(f'{self.name_knight}, на нас напали!')
        while not self.enemy == 0 and not self.enemy < 0:
            self.days += 1
            if self.power_knight > self.enemy:
                self.enemy = 0
            else:
                self.enemy -= self.power_knight
            print(f'{self.name_knight} сражается {self.days} день(дня)..., осталось {self.enemy} воинов.')
            time.sleep(1)
        print(f'{self.name_knight} одержал победу спустя {self.days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

Knights = [first_knight, second_knight]

for i in Knights:
    i.start()

for i in Knights:
    i.join()

print('Все битвы закончились!')
