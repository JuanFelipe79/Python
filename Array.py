alunos = [
    {"nome": "Ana", "notas": [8, 7, 9]},
    {"nome": "João", "notas": [6, 5, 7]},
    {"nome": "Maria", "notas": [9, 8, 10]}
]

def calcular_media(notas):
    return sum(notas) / len(notas)

for aluno in alunos:
    nome = aluno["nome"]
    notas = aluno["notas"]
    media = calcular_media(notas)
    print(f"Aluno: {nome}, Notas: {notas}, Média: {media}")
