#=========================================================
def cria_matriz(n: int) -> list:
	A = [[0] * n for i in range(n)]

	for i in range(len(A)): # Percorre as linhas
		A[i] = list(map(float, input().split()))

	return A

#=========================================================
def fatoracao_X_Y(X: list, Y: list) -> list:
    n = 1
    divisao_por_zero = False

    for z in range(len(X) - 1):
        if X[z][z] == 0:
            print("Divisao por zero.")
            divisao_por_zero = True
            break

        for j in range(n, len(X[0])):
            lambida = X[z][j] / X[z][z]
            Y[z][j] = lambida

            for i in range(z, len(X)):
                X[i][j] = X[i][j] - lambida * X[i][z]

        n += 1

    return X, Y, divisao_por_zero

#=========================================================
def fatoracao_Y(A: list, n: int) -> list:
	Y = [[0] * n for i in range(n)]
	for i in range(len(A)):
		for j in range(len(A[0])): # '1' na diag.principal
			if i == j:
				Y[i][j] = 1

			else:	
				Y[i][j] = A[i][j]
#--------
	n = 1
	for k in range(len(Y[0])):    # '0' abaixo da diagonal
		for l in range(n, len(Y)):
			Y[l][k] = 0

		n+= 1

	return Y

#=========================================================
def imprime_saida(X: list, Y: list):
	for lin in range(len(X)):
		for col in range(len(X[0])):
			print(f"{X[lin][col]:.2f}", end="\t")
		print()

	print()

	for l in range(len(Y)):
		for c in range(len(Y[0])):
			print(f"{Y[l][c]:.2f}", end="\t")
		print()

#=========================================================
def main():
    n = int(input())

    A = cria_matriz(n)
    Y = fatoracao_Y(A, n)
    A, B, divisao_por_zero = fatoracao_X_Y(A, Y)

    if divisao_por_zero == False:
        imprime_saida(A, B)

#=========================================================
main()