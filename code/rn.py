# крч эта прога выдаёт график зависимости среднего значения очков игрального кубика от кол-ва бросков
from random import randint
import matplotlib.pyplot as plt
import numpy as np


class Die:
    def __init__(self, count):
        self.count = count

    def random_score(self):
        return randint(1, 6)

    def randoming(self):
        z = 0
        summa = 0
        while z <= self.count:
            summa += randint(1, 6)
            z += 1
        return summa / self.count


x = np.linspace(1, 5001, 5000)
i = 0
y = []
for i in range(1, 5001):
    ThisClass = Die(i)
    y.append(ThisClass.randoming())
plt.plot(x, y)
plt.show()
JustDie = Die(1000)
print(JustDie.random_score())
