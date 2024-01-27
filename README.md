Computabilidad 

Proyecto Final 

Máquina Universal de Turing

Raúl Daniel García Ramón

rauld.garcia95@gmail.com

# Introducción

La máquina universal de Turing es una máquina de Turing a la cual se le ingresan en la cinta las instrucciones codificadas en 0's y 1's de una máquina de Turing arbitraria, de manera que la máquina universal de Turing imite el comportamiento de dicha máquina.

Para obtener la lista de instrucciones codificadas en 0's y 1's primero se tiene que tener las reglas de la máquina de Turing a simular, por ejemplo la máquina XN+1 tiene las siguientes reglas: 

$_{0} 0 \rightarrow \text{ } _{0} 0R \text{, } _{0} 1 \rightarrow _{1} 1R ,$

$_{1} 0 \rightarrow \text{ } _{0} 0R \text{, } _{1} 1 \rightarrow _{10} 1R , $

$_{10} 0 \rightarrow \text{ } _{11} 0L \text{, } _{10} 1 \rightarrow _{10} 1R , $

$_{11} 0 \rightarrow \text{ } _{0} 1STOP \text{, } _{11} 1 \rightarrow _{100} 0L , $

$_{100} 0 \rightarrow \text{ } _{101} 1L \text{, } _{100} 1 \rightarrow _{100} 1L , $

$_{101} 0 \rightarrow \text{ } _{110} 0R \text{, } _{101} 1 \rightarrow _{10} 1R , $

$_{110} 0 \rightarrow \text{ } _{0} 0R \text{, } _{110} 1 \rightarrow _{111} 1R , $

$_{111} 0 \rightarrow \text{ } _{11} 1R \text{, } _{111} 1 \rightarrow _{111} 0R .$


Si se quitan la parte derecha de cada regla, además de las flechas y las comas se obtiene lo siguiente: 


$\text{ } _{0} 0R \text{ } _{1} 1R \text{ }$ 

$\text{ } _{0} 0R \text{ } _{10} 1R \text{ }$ 

$\text{ } _{11} 0L \text{ } _{10} 1R \text{ }$ 

$\text{ } _{0} 1STOP \text{ } _{100} 0L \text{ }$

$\text{ } _{101} 1L \text{ } _{100} 1L \text{ }$ 

$\text{ } _{110} 0R \text{ } _{10} 1R \text{ }$ 

$\text{ } _{0} 0R \text{ } _{111} 1R \text{ }$

$\text{ } _{11} 1R \text{ } _{111} 0R $


A continuación se eliminan los $00$ y se reemplaza cada $01$ por simplemente $1$ obteniendo lo siguiente: 


$R _{1} 1R $ 

$R _{10} 1R $

$_{11} 0L _{10} 1R$ 

$1STOP _{100} 0L$ 

$_{101} 1L _{100} 1L$ 

$_{110} 0R _{10} 1R$  

$R _{111} 1R $

$_{11} 1R _{111} 0R $


Posteriormente, se utiliza la codificación de la tabla para obtener la cadena binaria:

11010101101101001011010100111010010110101111010000111010010101110100010111010100011010010110110101010101101010101101010100110


Finalmente, se elimina el $110$ inicial y final de la cadena binaria, ya que es común para todas las máquinas de Turing: 

10101101101001011010100111010010110101111010000111010010101110100010111010100011010010110110101010101101010101101010100


Y al convertir esa cadena binaria a decimal estándar se obtiene el siguiente número de máquina de Turing: $450813704461563958982113775643437908$

| Código | Regla |
| - | - |
| 0 | para 0 |
| 1 | para 1 |
| 110 | para R |
| 1110 | para L |
| 11110 | para STOP |

# Implementación
Ahora la cuestión es: a partir de un número en decimal obtener las reglas para ese número de máquina de Turing e imitar su comportamiento para una cadena específica y ver si se obtiene el resultado esperado. Para realizar esto se tienen que realizar los pasos anteriores en sentido contrario:

* Tener el número en decimal
* Convertirlo a binario
* Agregar él $110$ al inicio y al final del número binario
* Convertir el número binario a reglas de acuerdo a la tabla \ref{Reglas}
* Agregar los $00$ faltantes y sustituir los $1$ por $01$

Una vez que se tienen las reglas de la máquina de Turing a imitar, hay que realizar la simulación, en esta situación se propone utilizar una tabla que guarde todas las reglas de $nx6$, donde n es el número de estados, de manera que cada renglón sea un estado de la máquina, mientras que las primeras tres columnas serán para cuando lea un $0$ y las otras tres para cuando lea un $1$, cada columna cumplirá una función especifica como se muestra a continuación en la tabla \ref{ejemplotabla}:

| 0 | 0 | 0 | 1 | 1 | 1 |
| - | - | - | - | - | - |
| Estado al que se movera | Signo a escribir en la cinta | Regla (R, L o Stop) | Estado al que se movera | Signo a escribir en la cinta | Regla (R, L o Stop) |

Ahora se mostrará esto con un ejemplo con la propia máquina XN+1, su número en decimal es 450813704461563958982113775643437908, se convierte a binario y se obtiene lo siguiente: 

10101101101001011010100111010010110101111010000111010010101110100010111010100011010010110110101010101101010101101010100 

Se agregan el $110$ inicial y final y se convierte en lista para manejo más sencillo en el código:

1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0 

Se convierte en reglas de acuerdo a tabla: 

'R', 1, 1, 'R', 'R', 1, 0, 1, 'R', 1, 1, 0, 'L', 1, 0, 1, 'R', 1, 'STOP', 1, 0, 0, 0, 'L', 1, 0, 1, 1, 'L', 1, 0, 0, 1, 'L', 1, 1, 0, 0, 'R', 1, 0, 1, 'R', 'R', 1, 1, 1, 1, 'R', 1, 1, 1, 'R', 1, 1, 1, 0, 'R' 

Se agrupan las reglas, se agregan los $00$ y se sustituyen los $1$ por $01$ donde sea necesario: 

$[[0, 0, 'R'], [1, 1, 'R'], [0, 0, 'R'], [1, 0, 1, 'R'], $ 

$[1, 1, 0, 'L'], [1, 0, 1, 'R'], [0, 1, 'STOP'], [1, 0, 0, 0, 'L'], $ 

$[1, 0, 1, 1, 'L'], [1, 0, 0, 1, 'L'], [1, 1, 0, 0, 'R'], [1, 0, 1, 'R'], $ 

$[0, 0, 'R'], [1, 1, 1, 1, 'R'], [1, 1, 1, 'R'], [1, 1, 1, 0, 'R']]$ 

A continuación se obtiene la tabla:

| 0 | 0 | 0 | 1 | 1 | 1 |
| - | - | - | - | - | - |
| 0 | 0 | R | 1 | 1 | R |
| 0 | 0 | R | 2 | 1 | R |
| 3 | 0 | L | 2 | 1 | R |
| 0 | 1 | STOP | 4 | 0 | L |
| 5 | 1 | L | 4 | 1 | L |
| 6 | 0 | R | 2 | 1 | R |
| 0 | 0 | R | 7 | 1 | R |
| 3 | 1 | R | 1 | 0 | R |


Finalmente con la tabla se puede computar el comportamiento de la máquina de Turing, solamente indicando el renglón (estado) en el que se encuentra y que es lo que se está leyendo en la cadena.

# Experimentos
Ahora se verán unos experimentos con diferentes máquinas de Turing para ver que su comportamiento sea el esperado, primero se probara la máquina UN+1, la cual recibe un número en unario y le agrega un $1$:

Ingrese el número de la maquina de Turing en decimal:177642

Ingrese la cadena a computar con el siguiente formato ejemplo 0111000000: 0111000

Tabla de reglas:

[[0, 0, 'R', 1, 1, 'R'], 

[0, 1, 'STOP', 1, 1, 'R']]


Cadena original a computar: [0, 1, 1, 1, 0, 0, 0]

Cadena resultante: [0, 1, 1, 1, 1, 0, 0]


Como se puede si le agrega un $1$ justo donde estaba el primer $0$ después de la cadena de 1's. Ahora se probará el UN*2 el cual duplica el número unario que se le da:

Ingrese el número de la maquina de Turing en decimal: 1492923420919872026917547669
Ingrese la cadena a computar con el siguiente formato ejemplo 0111000000: 011100000

Tabla de reglas:

[[0, 0, 'R', 1, 0, 'R'], 

[2, 1, 'L', 1, 1, 'R'], 

[3, 0, 'R', 4, 0, 'R'], 

[0, 1, 'STOP', 3, 1, 'R'], 

[5, 1, 'L', 4, 1, 'R'], 

[2, 1, 'L', 5, 1, 'L']]

Cadena original a computar: [0, 1, 1, 1, 0, 0, 0, 0, 0]

Cadena resultante: [0, 0, 1, 1, 1, 1, 1, 1, 0]

Como se ve el número de 1's si se duplicó en la cadena resultante con respecto a la cadena original. Ahora se probará la máquina XN+1, a la cual se le ingresa un número en binario expandido con un 110 al final y le agrega un 1:

Ingrese el número de la maquina de Turing en decimal: 450813704461563958982113775643437908
Ingrese la cadena a computar con el siguiente formato ejemplo 0111000000: 10010110

Tabla de reglas:

[[0, 0, 'R', 1, 1, 'R'], 

[0, 0, 'R', 2, 1, 'R'], 

[3, 0, 'L', 2, 1, 'R'], 

[0, 1, 'STOP', 4, 0, 'L'], 

[5, 1, 'L', 4, 1, 'L'], 

[6, 0, 'R', 2, 1, 'R'], 

[0, 0, 'R', 7, 1, 'R'], 

[3, 1, 'R', 7, 0, 'R']]

Cadena original a computar: [1, 0, 0, 1, 0, 1, 1, 0]

Cadena resultante: [1, 0, 1, 0, 0, 1, 1, 0]


La cadena que se ingresó es 10010110 que en binario normal es 101 que en decimal es 5, y el resultado en binario expandido es 10100110 que en binario normal es 110 y en decimal es 6, de manera que si le está sumando un 1 al número ingresado. Ahora se probará la máquina XN+2 que igual recibe un valor en binario expandido con un 110 al final:

Ingrese el número de la maquina de Turing en decimal: 10389728107
Ingrese la cadena a computar con el siguiente formato ejemplo 0111000000: 1001011000

Tabla de reglas:

[[0, 0, 'R', 1, 0, 'R'], 

[0, 1, 'R', 2, 0, 'R'], 

[3, 1, 'R', 0, 0, 'R'], 

[0, 1, 'STOP', 0, 0, 'R']]

Cadena original a computar: [1, 0, 0, 1, 0, 1, 1, 0, 0, 0]

Cadena resultante: [0, 1, 0, 0, 1, 0, 0, 1, 1, 0]

Se ingresó el número en binario expandido 1001011000 que es 101 en binario normal que es el 5 en decimal, y se recibió 0100100110 en binario expandido, que es 01010 en binario normal que es a su vez 10 en decimal, por lo que efectivamente si duplica el valor ingresado.

# Conclusión
Después de realizar algunas pruebas con diferentes máquinas de Turing se puede observar que efectivamente el algoritmo funciona de la manera deseada, sin embargo, esto solo sucederá si se le ingresa la cadena de la manera correcta para esa máquina específica, ya que si se le ingresa por ejemplo un número en unario a una máquina que trabaja con el número en binario expandido, lo más seguro es que la cadena resultante no sea la esperada. Finalmente, lo mismo sucedería si no se le ingresan los suficientes 0's a la derecha para que pueda realizar el cómputo completo, ya que como se recordara la cinta en teoría tendría que ser infinita.
