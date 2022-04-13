num_linhas, num_colunas = [int(i) for i in input().split()]
tabuleiro = [None] * num_linhas
for linha in range(num_linhas):
    tabuleiro[linha] = input().split()


def distancia(x1, y1, x2, y2):
    dis = abs(x2 -x1) + abs(y2 - y1)
    return dis
    
lista = []

def permutar_tudo(iter):
    if len(iter) == 0:
        return []
    elif len(iter) == 1:
        return [iter]
    else:
        lista = []
        for i in range(len(iter)):
            x = iter[i]
            xs = iter[:i] + iter[i+1:]
            for p in permutar_tudo(xs):
                lista.append([x] + p)
        return lista


def ant_atual_prox(my_list):
    ant, atual, prox = None, iter(my_list), iter(my_list)
    next(prox, None)

    while True:
        try:
            if ant:
                yield next(ant), next(atual), next(prox, None)
            else:
                yield None, next(atual), next(prox, None)
                ant = iter(my_list)
        except StopIteration:
            break


for i in tabuleiro:
    for coluna in i:
        if coluna == 'R':
            vertice = [coluna,tabuleiro.index(i), i.index(coluna)]
            lista.insert(0,vertice)
        elif coluna != "0":
            vertice = [coluna,tabuleiro.index(i), i.index(coluna)]
            lista.append(vertice)

lista.append(['r', lista[0][1],lista[0][2]])
    
menor_distancia = 1000
menor_caminho = []
distancia_total = 0


for L in range(len(lista),len(lista)+1):
    for subset in permutar_tudo(lista):
        if subset[0][0] == 'R' and subset[-1][0] == 'r':
            for previous, item, nxt in ant_atual_prox(subset):
                if (subset.index(item) == (len(subset)-1)):
                    if distancia_total < menor_distancia:
                        menor_caminho = subset
                        menor_distancia = distancia_total
                    distancia_total = 0
                else:
                    distancia_total += distancia(item[1], item[2], nxt[1],nxt[2])      

resposta = []
for i in menor_caminho:
    for k in i:
        if type(k) is str:
            resposta.append(k)

print(''.join(resposta[1:-1]), menor_distancia)
