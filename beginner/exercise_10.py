# Currency

pesos = int(input("What do you have left in pesos? " ))
pesos_convert = pesos * 0.05

soles = int(input("What do you have left in soles? " ))
soles_convert = soles * 0.28

reais = int(input("What do you have left in reasis? " ))
reais_convert = reais * 0.17

usd = pesos_convert + soles_convert + reais_convert
print(usd)
