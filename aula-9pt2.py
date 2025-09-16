# Questão 1 – Cadastro de números

lista = []
lista.append(10)
lista.append(20)
lista.append(30)
print(lista)
lista.insert(1, 15)
print(lista)

# Questão 2 – Removendo elementos

lista = [5, 10, 15, 20, 25]

print(lista)
lista.remove(10)
print(lista)
lista.pop()
print(lista)
lista.pop(0)

# Questão 3 – Trabalhando com ordenação

valores = [8, 3, 10, 1, 7]
print(valores)
print(sorted(valores))
valores.sort(reverse=True)
print(valores)
valores.reverse()
print(valores)

# Questão 4 – Notas dos alunos

notas = [7.5, 8.0, 6.5, 9.0, 5.5]
print(notas)
print(len(notas))
print(max(notas))
print(min(notas))
