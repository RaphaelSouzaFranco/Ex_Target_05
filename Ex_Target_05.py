
# String de exemplo (solicitada ao usuário)
string = input("Digite o texto que deseja inverter:")

# Inicializa uma nova string vazia
string_invertida = ""

# Percorre a string original de trás para frente e constrói a nova string invertida
for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

# Exibir o resultado
print("String original:", string)
print("String invertida:", string_invertida)