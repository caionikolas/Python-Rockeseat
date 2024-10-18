nome = "Nikolas"

# Metodos strings, nenhuma altera o valor
nome.upper() # "NIKOLAS"
nome.lower() # "nikolas"
nome[0] # "N"
nome.count("a") # 1
nome.find("a") # 5
nome.encode() # b"Nikolas"
nome.encode().decode() # "Nikolas"
nome.replace("a", "u") # "Nikolus"
"-".join(nome) # "N-i-k-o-l-a-s"

nome_completo = "Caio Nikolas"
nome.split(" ") # ["Caio", "Nikolas"]

teste = " palavras "
nome.strip(" ") # "palavras"
nome.rstrip(" ") # "palavras "

nome.startswith("Ni") # True
nome.startswith("Ca") # False

"Ni" in nome # True
"ko" in nome # True
"Ca" in nome # False

"Ni" not in nome # False
"ko" not in nome # False
"Ca" not in nome # True
