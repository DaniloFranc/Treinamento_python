import numpy as np
import random


H = 0
N = int(input("Digite o tamanho da rede N: "))
PMT = int(input("Digite o numero de passos de Monte Carlo PMT: "))
PMD = int(input("Digite o numero de passos desprezados PMD: "))

NP = N * N
sigma = np.ones((N + 2, N + 2))

for i in range(1, N + 1):
    for jj in range(1, N + 1):
        sigma[i][jj] = 1

for i in range(1, N + 1):
    sigma[i][N + 1] = sigma[i][1]
    sigma[i][0] = sigma[i][N]
    sigma[N + 1][i] = sigma[1][i]
    sigma[0][i] = sigma[N][i]

M = NP
E = -2 * NP

with open("saida.dat", "w") as out:
    out.write("T E_media/NP C/NP M_media/NP X/NP\n")

    T = 0.01
    while T < 6:
        SE = 0
        SM = 0
        SE2 = 0
        SM2 = 0

        for PM in range(1, PMT + 1):
            for L in range(1, N + 1):
                for P in range(1, N + 1):
                    ranf = random.uniform(0, 1)

                    deltaM = -2 * sigma[L][P]
                    deltaE = -deltaM * (sigma[L - 1][P] + sigma[L][P + 1] + sigma[L + 1][P] + sigma[L][P - 1])

                    if deltaE <= 0:
                        sigma[L][P] = -sigma[L][P]
                        if L == 1:
                            sigma[N + 1][P] = sigma[L][P]
                        if L == N:
                            sigma[0][P] = sigma[L][P]
                        if P == 1:
                            sigma[L][N + 1] = sigma[L][P]
                        if P == N:
                            sigma[L][0] = sigma[L][P]
                    else:
                        PB = np.exp((-deltaE / T))

                        if PB >= ranf:
                            sigma[L][P] = -sigma[L][P]
                            if L == 1:
                                sigma[N + 1][P] = sigma[L][P]
                            if L == N:
                                sigma[0][P] = sigma[L][P]
                            if P == 1:
                                sigma[L][N + 1] = sigma[L][P]
                            if P == N:
                                sigma[L][0] = sigma[L][P]
                        else:
                            deltaE = 0
                            deltaM = 0

                    E = E + deltaE
                    M = M + deltaM

            if PM > PMD:
                SE = SE + E
                SM = SM + abs(M)
                SE2 = SE2 + E * E
                SM2 = SM2 + M * M

            E_media = SE / (PMT - PMD)
            C = (SE2 / (PMT - PMD) - SE * SE / (PMT - PMD) / (PMT - PMD)) / (T * T)
            M_media = SM / (PMT - PMD)
            X = (SM2 / (PMT - PMD) - SM * SM / (PMT - PMD) / (PMT - PMD)) / T

            out.write("%.2f %.5f %.5f %.5f %.5f\n" % (T, E_media / NP, C / NP, M_media / NP, X / NP))
            T = T + 0.01