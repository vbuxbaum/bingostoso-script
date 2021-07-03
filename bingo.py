from pprint import pprint
import random


participantes = ["bux", "sarah"]

cartelas = []
for nome in participantes:
    cartela = {
        nome: [
            [random.randint(1, 15) for _ in range(5)],
            [random.randint(16, 30) for _ in range(5)],
            [random.randint(31, 45) for _ in range(4)],
            [random.randint(46, 60) for _ in range(5)],
            [random.randint(61, 75) for _ in range(5)],
        ]
    }
    cartelas.append(cartela)


pprint(cartelas)
