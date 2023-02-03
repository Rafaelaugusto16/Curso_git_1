import random
from random import randint
sorteios=[]
cont= 1
mega= [21,17,12]
while cont<=7:
    numero=random.choice(mega)
    if not numero in sorteios:
        sorteios.append(numero)
        cont= cont + 1
print(sorteios)