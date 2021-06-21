class For:

    def __init__(self):
        pass

    def usoFor(self):
        nombre = "Daniel"
        dato = ["Daniel", 50, True]
        numeros = (2, 5.6, 4, 1)
        profesor = {"nombre": "Daniel", "edad": 50, "fac": "faci"}
        lista_notas = [(30, 40), [20, 40] ,(50, 40)]
        lista_estudiantes = [{"nombre": "Erick", "final": 70}, {"nombre": "Yady", "final": 60}, {"nombre": "Danny", "final": 90}]

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


obj_for = For()
obj_for.usoFor()
