"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    df = open("data.csv", "r").readlines() #Se hace lectura de la data
    df = [z.replace("\n", "") for z in df] #Retiramos el retorno de carro
    df = [z.split("\t") for z in df] #Separamos
    Col2 = [z[1] for z in df[0:]] #Capturamos la columna 2

    suma = 0
    for i in Col2:
        suma = suma + int(i)

    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    df = open("data.csv", "r").readlines() #Se hace lectura de la data
    df = [z.replace("\n", "") for z in df] #Retiramos el retorno de carro
    df = [z.split("\t") for z in df] #Separamos

    Col1 = [z[0] for z in df[0:]]

    from collections import Counter

    tuples_list = Counter(Col1)
    tuples_list = dict(tuples_list)
    ordenada = sorted(tuples_list.items())

    return ordenada


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    df = open("data.csv", "r").readlines() #Se hace lectura de la data
    df = [z.replace("\n", "") for z in df] #Retiramos el retorno de carro
    df = [z.split("\t") for z in df]

    ListA = [z for z in df if z[0] == "A"]
    ListB = [z for z in df if z[0] == "B"]
    ListC = [z for z in df if z[0] == "C"]
    ListD = [z for z in df if z[0] == "D"]
    ListE = [z for z in df if z[0] == "E"]

    Col2A = [z[1] for z in ListA[0:]]
    Col2B = [z[1] for z in ListB[0:]]
    Col2C = [z[1] for z in ListC[0:]]
    Col2D = [z[1] for z in ListD[0:]]
    Col2E = [z[1] for z in ListE[0:]]

    sumaA = 0
    sumaB = 0
    sumaC = 0
    sumaD = 0
    sumaE = 0

    for i in Col2A:
        sumaA = sumaA + int(i)
        
    for i in Col2B:
        sumaB = sumaB + int(i)

    for i in Col2C:
        sumaC = sumaC + int(i)

    for i in Col2D:
        sumaD = sumaD + int(i)
        
    for i in Col2E:
        sumaE = sumaE + int(i)

    List_ordenada = [('A', sumaA), ('B', sumaB), ('C', sumaC), ('D', sumaD), ('E', sumaE)]

    return List_ordenada


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    df = open("data.csv", "r").readlines() #Se hace lectura de la data
    df = [z.replace("\n", "") for z in df] #Retiramos el retorno de carro
    df = [z.split("\t") for z in df] #Separamos
    Col3_mes = [z[2].split("-")[1] for z in df[0:]]
    from collections import Counter

    tuples_list = Counter(Col3_mes)
    tuples_list = dict(tuples_list)
    ordenada = sorted(tuples_list.items())

    return ordenada


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    df = open("data.csv", "r").readlines() #Se hace lectura de la data
    df = [z.replace("\n", "") for z in df] #Retiramos el retorno de carro
    df = [z.split("\t") for z in df]

    Col1 = [z[0] for z in df[0:]]#Se extrae la columna 1

    ListA = [z for z in df if z[0] == "A"]
    ListB = [z for z in df if z[0] == "B"]
    ListC = [z for z in df if z[0] == "C"]
    ListD = [z for z in df if z[0] == "D"]
    ListE = [z for z in df if z[0] == "E"]

    ListA_ = [z[1] for z in ListA] #Se extrae la columna 2 del segmento que le pertenece a A
    ListB_ = [z[1] for z in ListB]
    ListC_ = [z[1] for z in ListC]
    ListD_ = [z[1] for z in ListD]
    ListE_ = [z[1] for z in ListE]

    lista_p5 = []

    for i in Col1:
        if i == 'A':
            minimo = min(ListA_)
            maximo = max(ListA_)
        elif i == 'B':
            minimo = min(ListB_)
            maximo = max(ListB_)
        elif i == 'C':
            minimo = min(ListC_)
            maximo = max(ListC_)
        elif i == 'D':
            minimo = min(ListD_)
            maximo = max(ListD_)
        else:
            minimo = min(ListE_)
            maximo = max(ListE_)
        
        tupla = (i, int(maximo), int(minimo))
        
        lista_p5.append(tupla)
        
    unique_list = list(set(lista_p5))
    unique_list.sort(key = lambda x: x[0], reverse=False)
    tuple(unique_list)

    return unique_list


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    df = open("data.csv", "r").readlines() #Se hace lectura de la data
    df = [z.replace("\n", "") for z in df] #Retiramos el retorno de carro
    df = [z.split("\t") for z in df] #Separamos
    Col2 = [z[1] for z in df[0:]] #Capturamos la columna 2

    List0 = [z for z in df if z[1] == '0']
    List1 = [z for z in df if z[1] == "1"]
    List2 = [z for z in df if z[1] == "2"]
    List3 = [z for z in df if z[1] == "3"]
    List4 = [z for z in df if z[1] == "4"]
    List5 = [z for z in df if z[1] == "5"]
    List6 = [z for z in df if z[1] == "6"]
    List7 = [z for z in df if z[1] == "7"]
    List8 = [z for z in df if z[1] == "8"]
    List9 = [z for z in df if z[1] == "9"]

    Col1_X = []
    lista_final = []

    for i in Col2:
        if i == '0':
            Col1_X = [z[0] for z in List0[0:]]
        elif i == '1':
            Col1_X = [z[0] for z in List1[0:]]
        elif i == '2':
            Col1_X = [z[0] for z in List2[0:]]
        elif i == '3':
            Col1_X = [z[0] for z in List3[0:]]
        elif i == '4':
            Col1_X = [z[0] for z in List4[0:]]
        elif i == '5':
            Col1_X = [z[0] for z in List5[0:]]
        elif i == '6':
            Col1_X = [z[0] for z in List6[0:]]
        elif i == '7':
            Col1_X = [z[0] for z in List7[0:]]
        elif i == '8':
            Col1_X = [z[0] for z in List8[0:]]
        else:
            Col1_X = [z[0] for z in List9[0:]]

        lista_veces = (int(i), Col1_X)
        lista_final.append(lista_veces)
        
        
    lista_final.sort(key = lambda x: x[0], reverse=False)

    unique_list = [] 

    for x in lista_final: 
        if x not in unique_list:
            unique_list.append(x)

    return unique_list 


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    df = open("data.csv", "r").readlines() #Se hace lectura de la data
    df = [z.replace("\n", "") for z in df] #Retiramos el retorno de carro
    df = [z.split("\t") for z in df] #Separamos
    Col2 = [z[1] for z in df[0:]] #Capturamos la columna 2

    List0 = [z for z in df if z[1] == '0']
    List1 = [z for z in df if z[1] == "1"]
    List2 = [z for z in df if z[1] == "2"]
    List3 = [z for z in df if z[1] == "3"]
    List4 = [z for z in df if z[1] == "4"]
    List5 = [z for z in df if z[1] == "5"]
    List6 = [z for z in df if z[1] == "6"]
    List7 = [z for z in df if z[1] == "7"]
    List8 = [z for z in df if z[1] == "8"]
    List9 = [z for z in df if z[1] == "9"]

    Col1_X = []
    lista_final = []

    for i in Col2:
        if i == '0':
            Col1_X = [z[0] for z in List0[0:]]
        elif i == '1':
            Col1_X = [z[0] for z in List1[0:]]
        elif i == '2':
            Col1_X = [z[0] for z in List2[0:]]
        elif i == '3':
            Col1_X = [z[0] for z in List3[0:]]
        elif i == '4':
            Col1_X = [z[0] for z in List4[0:]]
        elif i == '5':
            Col1_X = [z[0] for z in List5[0:]]
        elif i == '6':
            Col1_X = [z[0] for z in List6[0:]]
        elif i == '7':
            Col1_X = [z[0] for z in List7[0:]]
        elif i == '8':
            Col1_X = [z[0] for z in List8[0:]]
        else:
            Col1_X = [z[0] for z in List9[0:]]

        lista_veces = (int(i), Col1_X)
        lista_final.append(lista_veces)
        
        
    lista_final.sort(key = lambda x: x[0], reverse=False)

    unique_list = [] 

    for x in lista_final: 
        if x not in unique_list:
            unique_list.append(x)

    letrasU = []
    for i in unique_list:
        letras = set(i[1])
        ordenada = sorted(letras)
        tupla = (i[0], list(ordenada))
        letrasU.append(tupla)

    return letrasU


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    df = open("data.csv", "r").readlines() #Se hace lectura de la data
    df = [z.replace("\n", "") for z in df] #Retiramos el retorno de carro
    df = [z.split("\t") for z in df]

    Col5 = [z[4] for z in df[0:]]
    Col5_split = [z.split(",") for z in Col5]

    list_values = []
    list_keys = []

    for i in Col5_split:
        for x in i:
            keys = (x[0:3])
            values = (x[4:])
            list_values.append(values)
            list_keys.append(keys)

    from collections import Counter

    tuples_list = Counter(list_keys) #Tipo de dato Counter
    tuples_list = dict(sorted(tuples_list.items())) #Se convierte en diccionario
    

    return tuples_list


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    df = open("data.csv", "r").readlines() #Se hace lectura de la data
    df = [z.replace("\n", "") for z in df] #Retiramos el retorno de carro
    df = [z.split("\t") for z in df]

    lista_p10 = []

    for i in df:
        Columna1 = i[0]
        Columna4 = i[3].split(",")
        Columna5 = i[4].split(",")
        tupla = (Columna1, len(Columna4), len(Columna5))
        lista_p10.append(tupla)

    return lista_p10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    df = open("data.csv", "r").readlines() #Se hace lectura de la data
    df = [z.replace("\n", "") for z in df] #Retiramos el retorno de carro
    df = [z.split("\t") for z in df] #Separamos

    list_11 = []

    Cols = [row[1:4:2] for row in df[0:]]
    for i in Cols:
        Columna4 = i[1].split(",")
        for x in Columna4:
            tupla = (i[0],x)
            list_11.append(tupla) 

    valA = []
    letA = []
    valB = []
    letB = []
    valC = []
    letC = []
    valD = []
    letD = []
    valE = []
    letE = []
    valF = []
    letF = []
    valG = []
    letG = []

    for j in list_11:
        if j[1] == 'a':
            valA.append(j[0])
            letA.append(j[1])
        elif j[1] == 'b':
            valB.append(j[0])
            letB.append(j[1])
        elif j[1] == 'c':
            valC.append(j[0])
            letC.append(j[1])
        elif j[1] == 'd':
            valD.append(j[0])
            letD.append(j[1])
        elif j[1] == 'e':
            valE.append(j[0])
            letE.append(j[1])
        elif j[1] == 'f':
            valF.append(j[0])
            letF.append(j[1])
        else:
            valG.append(j[0])
            letG.append(j[1])

    sumaA = 0
    for i in valA:
        sumaA = sumaA + int(i)

    sumaB = 0
    for i in valB:
        sumaB = sumaB + int(i)

    sumaC = 0
    for i in valC:
        sumaC = sumaC + int(i)

    sumaD = 0
    for i in valD:
        sumaD = sumaD + int(i)

    sumaE = 0
    for i in valE:
        sumaE = sumaE + int(i)

    sumaF = 0
    for i in valF:
        sumaF = sumaF + int(i)

    sumaG = 0
    for i in valG:
        sumaG = sumaG + int(i)

    List_ordenada = [(letA[1], sumaA), (letB[1], sumaB), (letC[1], sumaC), (letD[1], sumaD), (letE[1], sumaE), (letF[1], sumaF), 
                    (letG[1], sumaG)]

    result = {}
    for letra, suma in List_ordenada:
        if letra in result.keys():
            result[letra].append(suma)
        else:
            result[letra] = suma



    return result


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    df = open("data.csv", "r").readlines() #Se hace lectura de la data
    df = [z.replace("\n", "") for z in df] #Retiramos el retorno de carro
    df = [z.split("\t") for z in df] #Separamos

    Cols = [row[0:5:4] for row in df[0:]]

    list_12 = []
    list_12_2 = []
    for i in Cols:
        Columna5 = i[1].split(",")
        tupla = (i[0],Columna5)
        list_12.append(tupla)
    list_12

    for x in list_12:
        for z in x[1]:
            tupla12 = (x[0], z[4:])
            list_12_2.append(tupla12) 

    result = {}
    for letra, valor in list_12_2:
        valor = int(valor)
    #     print(valor)
        if letra in result.keys():
            result[letra].append(valor)
        else:
            result[letra] = [valor]
            
    result = [(key, sum(valor)) for key, valor in result.items()]
    result = sorted(result)
    result = dict(result)
    return result
