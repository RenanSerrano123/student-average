def calcular_media_alunos(matriz):
    for i in range(len(matriz)):
        soma_notas = sum(matriz[i])
        media = soma_notas / len(matriz[i])
        matriz[i].append(media)
def main():
    L = int(input())
    C = int(input())
    matriz = []
    for i in range(L):
        linha = list(map(int, input().split()))
        matriz.append(linha)
    calcular_media_alunos(matriz)
    for linha in matriz:
        print(" ".join(f"{nota:.2f}" for nota in linha))
main()