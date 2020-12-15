import math
import random


T = [[0 for stvari in range(5)] for row in range(2)]
def matrika(m,n):
    return [[0 for stvari in range(m)] for row in range(n)] #funkcija, ki naredi ničelno matriko (m) X (n)


def t(i,j):
        if i == 0:
            if j <= 0:
                return 0
            else:
                return float('inf')
        else: 
            for i in range(5):
                for j in range(5):
                    yield i+j
print(t(4,5))
print(matrika(2,3))


def stej_resitve1(teze,C, epsilon):
    n = len(teze)
    Q = (1 + epsilon / (n + 1))
    s = math.ceil(n * math.log(2,Q))
    T = [[0 for stvari in range(s)] for row in range(n)]
    for j in range(1,s):
        T[0][j] = float('inf')
    for i in range(1,n + 1):
        for j in range(s + 1):
            for k in range(j+1):
                vse_mozne_resitve =[]
                alpha = Q **(-k)
                if math.floor(j + math.log(alpha,Q)) < 0:
                    T[i-1][math.floor(j + math.log(alpha,Q))] = 0
                if math.floor(j + math.log(1-alpha,Q)) < 0:
                    T[i-1][math.floor(j + math.log(1-alpha,Q))] = 0
                vse_mozne_resitve.append(max(T[i-1][math.floor(j + math.log(alpha,Q))],T[i-1][math.floor(j + math.log(1 - alpha,Q))+teze[i]]))
        T[i][j] = min(vse_mozne_resitve)        
    for j in range(s,-1,-1):
        if T[n][j] <= C:
            resitve = T[n][j]
        else:
            pass
    return Q **(resitve+1)
#ne gre s seznami, ker je drugi argument lahko negativen in poruši vso stvar

print(min(max(T)))


def stej_resitve2(teze,C, epsilon):
    n = len(teze)
    Q = (1 + epsilon / (n + 1))
    s = math.ceil(n * math.log(2,Q))
    def T(i,j):
        if i == 0:
            if j >= 0:
                return 0
            else:
                return float('inf')
        if j == 0:
            return 0
        else:     
            vrednosti = []
            for k in range(j,0,-1):
                alpha = Q ** (-k)
                if math.floor(j + math.log(alpha,Q)) < 0:
                    prva_vrednost = 0
                if math.floor(j + math.log(1-alpha,Q)) < 0:
                    druga_vrednost = 0
                else:
                    prva_vrednost = T(i-1,math.floor(j + math.log(alpha,Q)))
                    druga_vrednost = T(i-1,math.floor(j + math.log(1 - alpha,Q))) +teze[i-1]
                    vrednosti.append(max(prva_vrednost,druga_vrednost))
            return min(vrednosti)  
    for j in range(s,-1,-1):
        if T(n,j) <= C:
            resitve = T(n,j)
            break
        else:
            pass
    return Q **(resitve+1)

print(stej_resitve2([1], 4, 0.005))
