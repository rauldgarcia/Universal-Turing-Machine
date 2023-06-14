# xn+1= 450813704461563958982113775643437908
# xn*2= 10389728107
# un+1= 177642
# un*2= 1492923420919872026917547669

numeromaquina=450813704461563958982113775643437908
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

reglas=[]

while len(maquina)>0: #mientras maquina no este vacia convertir binario a reglas
    if maquina[0]==0:
        reglas.append(0)
        maquina.pop(0)
    elif maquina[0]==1 and maquina[1]==0:
        reglas.append(1)
        for i in range(2):
            maquina.pop(0)
    elif maquina[0]==1 and maquina[1]==1 and maquina[2]==0:
        reglas.append('R')
        for i in range(3):
            maquina.pop(0)
    elif maquina[0]==1 and maquina[1]==1 and maquina[2]==1 and maquina[3]==0:
        reglas.append('L')
        for i in range(4):
            maquina.pop(0)
    elif maquina[0]==1 and maquina[1]==1 and maquina[2]==1 and maquina[3]==1 and maquina[4]==0:
        reglas.append('STOP')
        for i in range(5):
            maquina.pop(0)
    else:
        print('yes')
        break

print(reglas)
print(maquina)

reglasderecha=[]

while len(reglas)>0: #separa las reglas en grupos
    if reglas[0]=='R' or reglas[0]=='L' or reglas[0]=='STOP':
        reglasaux=[]
        reglasaux.append(0)
        reglasaux.append(0)
        reglasaux.append(reglas[0])
        reglas.pop(0)
        reglasderecha.append(reglasaux)
    else:
        reglasaux=[]
        while reglas[0]!='R' and reglas[0]!='L' and reglas[0]!='STOP':
            reglasaux.append(reglas[0])
            reglas.pop(0)
        reglasaux.append(reglas[0])
        reglas.pop(0)
        if len(reglasaux)<3:
            reglasaux2=[0]
            reglasaux2.append(reglasaux[0])
            reglasaux2.append(reglasaux[1])
            reglasaux=reglasaux2
        reglasderecha.append(reglasaux)

print(reglasderecha)
print(reglas)