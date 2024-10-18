# Metodos dicionarios

dicionario = {
  "nome": "Caio",
  "sobrenome": "nikolas",
  "cidade": "Teresina",
  "ano": 2024
}

dicionario["nome"] # "Caio"

del dicionario["sobrenome"] 

# dicionario = {
#   "nome": "Caio",
#   "cidade": "Teresina",
#   "ano": 2024
# }

#nao é lista direta
dicionario.keys() #dict_keys(["nome", "sobrenome", "cidade", "ano"])

# é lista direta
list(dicionario.keys()) # ["nome", "sobrenome", "cidade", "ano"]

dicionario.values() # dict_values(["Caio", "Nikolas", "Teresina", 2024])

list(dicionario.values()) # ["Caio", "Nikolas", "Teresina", 2024]

dicionario.items() 
# dict_items( [ 
# ("nome", "Caio"), 
# ("sobrenome", "Nikolas"), 
# ("cidade", "Teresina"),
# ("ano", 2024),
# ])


 