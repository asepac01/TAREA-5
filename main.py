class For:

    def __init__(self):
        pass

    def usoFor(self):
        nombre = "Daniel"
        dato = ["Daniel", 50, True]
        numeros = (2, 5.6, 4, 1)
        profesor = {"nombre": "Daniel", "edad": 50, "fac": "faci"}

        # for i in range(5):
        #     print("i: {}".format(i))
        
        # print("")
        # for i in range(2, 10):
        #     print("i: {}".format(i))
        
        # print("")
        # for i in range(4, 10, 2):
        #     print("i: {}".format(i), end="  ")

        # print("\n")
        # for i in range(12, 3, -3):
        #     print("i: {}".format(i), end="  ")

        # print("\n")
        # longitud = len(dato)
        # print(dato[0])
        # print(dato[1])
        # print(dato[2])
        # j = 0
        # while j < longitud:
        #     print("j:{}".format(j), dato[j], end="  ")
        #     j += 1
        # print("")
        # for i in range(longitud-1, -1, -1):
        #     print("i:{}".format(i), dato[i], end="  ")

        # print("")
        # for i, dato in enumerate(numeros):
        #     print("For:", i, dato)
        
        # print("")
        # for dato in numeros:
        #     print("Dato:", dato)
        
        # print("")
        # for dato in ['H', 'o', 'l', 'a', 'que', 'tal']:
        #     print("Dato:", dato)

        # print("")
        # print("Diccionario de notas.")
        # for key, value in profesor.items():
        #     print(key + ":" + str(value), end="  ")
        
        # print("\n")
        # for estudiante in lista_estudiantes:
        #     for llave, valor in estudiante.items():
        #         print(llave + ":" + str(valor), end="  ")

        # lista_notas = [(30, 40), [20, 40] ,(50, 40)]
        # acum = 0
        # longitud = 0
        # for notas in lista_notas:
        #     parcial = 0
        #     print(notas, end=" ")
        #     for nota in notas:
        #         longitud += 1
        #         acum += nota
        #         parcial += nota
        #     promedio_parcial = parcial/len(notas)
        #     print("Notas Parciales:{} - Promedio Parcial:{}".format(parcial, promedio_parcial))
        # promedio = acum/longitud
        # print("Total notas:{} - #Notas:{} - Promedio:{}".format(acum, longitud, promedio))

        # lista_estudiante = [{"nombre": "Erick", "final": 70}, {"nombre": "Yady", "final": 60}, {"nombre": "Danny", "final": 90}]
        # acum = 0
        # contador = 0
        # for estudiantes in lista_estudiante:
        #     print(estudiantes)
        #     for llave, valor in estudiantes.items():
        #         print(str(llave) + ":" + str(valor), end="")
        #         if llave == "final": acum += valor
        #         print("")
        #     contador += 1
        # print(acum/contador)

        # oracion = "Hola como estas"
        # vocales = []
        # for carro in oracion:
        #     if carro in ('a', 'e', 'i', 'o', 'u'):
        #         vocales.append(carro)
        # print(vocales)
        print([carro for carro in "Hola como estas" if carro in ('a', 'e', 'i', 'o', 'u')])


obj_for = For()
obj_for.usoFor()
