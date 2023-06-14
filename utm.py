# xn+1= 450813704461563958982113775643437908
# xn*2= 10389728107
# un+1= 177642
# un*2= 1492923420919872026917547669

numeromaquina=177642
binario=bin(numeromaquina).replace("0b","")
print(binario)

maquina=[] #maquina vacia y se agrega cada elemento R 110
maquina.append(1)
maquina.append(1)
maquina.append(0)

for elemento in range(len(binario)):
    maquina.append(int(binario[elemento]))

maquina.append(1)
maquina.append(1)
maquina.append(0)

print(maquina)