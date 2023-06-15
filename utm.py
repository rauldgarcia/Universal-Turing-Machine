# xn+1=450813704461563958982113775643437908
# xn*2=10389728107
# un+1=177642
# un*2=1492923420919872026917547669

numeromaquina=1492923420919872026917547669
cadena=[0,1,1,1,0,0,0,0,0,0]
binario=bin(numeromaquina).replace("0b","")

maquina=[] #maquina vacia y se agrega cada elemento R 110
maquina.append(1)
maquina.append(1)
maquina.append(0)

for elemento in range(len(binario)):
    maquina.append(int(binario[elemento]))

maquina.append(1) #se agrega la R final 110
maquina.append(1)
maquina.append(0)

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


reglasderecha=[]

while len(reglas)>0: #separa las reglas en grupos
    if reglas[0]=='R' or reglas[0]=='L' or reglas[0]=='STOP': #si la cabeza de la lista solo es instruccion agrega 00
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

largotabla=int(len(reglasderecha)/2)

tabla=[[k for k in range(6)]for l in range(largotabla)] #crea una tabla, cada renglon sera un estado de la maquina

cont=0
for regla in range(len(reglasderecha)): #se ingresan reglas en tabla
    if regla%2==0:
        if len(reglasderecha[regla])<4:
            auxiliar=reglasderecha[regla]
            tabla[cont][0]=auxiliar[0]
            tabla[cont][1]=auxiliar[1]
            tabla[cont][2]=auxiliar[2]
        else:
            auxiliar=reglasderecha[regla]
            tabla[cont][1]=auxiliar[-2]
            tabla[cont][2]=auxiliar[-1]
            auxiliar.pop(-1)
            auxiliar.pop(-1)
            auxiliar=[str(numero) for numero in auxiliar]
            auxiliar="".join(auxiliar)
            auxiliar=int(auxiliar,2)
            tabla[cont][0]=auxiliar
    else:
        if len(reglasderecha[regla])<4:
            auxiliar=reglasderecha[regla]
            tabla[cont][3]=auxiliar[0]
            tabla[cont][4]=auxiliar[1]
            tabla[cont][5]=auxiliar[2]
        else:
            auxiliar=reglasderecha[regla]
            tabla[cont][4]=auxiliar[-2]
            tabla[cont][5]=auxiliar[-1]
            auxiliar.pop(-1)
            auxiliar.pop(-1)
            auxiliar=[str(numero) for numero in auxiliar]
            auxiliar="".join(auxiliar)
            auxiliar=int(auxiliar,2)
            tabla[cont][3]=auxiliar
        cont+=1 
    
print()
print(tabla)
print(cadena)

estado=0
casilla=0
#casillanueva=0
while estado!='STOP':
    #print(cadena)
    #print("estoy en estado ",estado)
    #print("leyendo la casilla ",casilla," que contiene ",cadena[casilla])
    if cadena[casilla]==0:
        cadena[casilla]=tabla[estado][1]
        if tabla[estado][2]=='R':
            casilla+=1    
        elif tabla[estado][2]=='L':
            casilla-=1    
        elif tabla[estado][2]=='STOP':
            break
        else:
            print('yes')
        estado=tabla[estado][0]   
    else:
        cadena[casilla]=tabla[estado][4]
        if tabla[estado][5]=='R':
            casilla+=1
        elif tabla[estado][5]=='L':
            casilla-=1
        elif tabla[estado][5]=='STOP':
            break
        else:
            print('yes')
        estado=tabla[estado][3]
    

print()    
print(cadena)