# Metodos Lista - Altera a lista

lista = [1, 2, "nikolas", True]

lista[0] = "python" # ["python", 2, "nikolas", True]
lista.append(6) # ["python", 2, "nikolas", True, 6]
lista.index(6) # 4
lista.insert(1, 10) # ["python", 10, 2, "nikolas", True, 6]
lista.pop(2) # ["python", 10, "nikolas", True, 6]
lista.remove(True) # ["python", 10, "nikolas", 6]
#ordenar elementos porem somente se tiver dados que podem ser ordenados
lista.sort() # ["python", 10, "nikolas", 6]