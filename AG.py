import random
import math
import operator

taxa_mutacao = 0.01
n_pop = 500
cross_rate = 0.9
repeticoes = 500
ponto_de_parada = 40
class Ponto_de_entrega:
    def __init__(self,x,y,name):
        self.name = name
        self.x = x
        self.y = y

    def distancia_calculo(self,ponto_de_entrega):
        distancia_x = abs(self.x - ponto_de_entrega.x)
        distancia_y = abs(self.y - ponto_de_entrega.y)
        distancia = math.sqrt(abs((distancia_x**2)+(distancia_y**2)))
        return distancia


class Individuo:
    def __init__(self,rota):
        self.rota = rota
        self.distancia = 0
        self.fitness = 0.0

    def distancia_da_rota(self):
        if self.distancia == 0:
            distancia_caminho = 0
            for i in range(0,len(self.rota)):
                origem = self.rota[i]
                destino = None
                if i + 1 < len(self.rota):
                    destino = self.rota[i+1]
                else:
                    destino = self.rota[0]
                distancia_caminho += origem.distancia_calculo(destino)
            self.distancia = distancia_caminho
        return self.distancia

    def fitness_rota(self):
        if self.fitness == 0:
            self.fitness = 1/float(self.distancia_da_rota())
        return self.fitness

def crirar_rota(lista_pontos):
    rota = random.sample(lista_pontos,len(lista_pontos))
    return rota

def pop_inicial(tam_pop,lista_pontos):
    populacao = []

    for i in range(0,tam_pop):
        populacao.append(crirar_rota(lista_pontos))
    return populacao

def pontuacao_rotas(populacao):
    resultado_fitness = {}
    for i in range(0,len(populacao)):
        resultado_fitness[i] = Individuo(populacao[i]).fitness_rota()
    return sorted(resultado_fitness.items(), key = operator.itemgetter(1), reverse = True)#tirar o sort

def selecao(pop,lista_fitness):
    fit = []
    for i in range(len(pop)):
        fit.append(None)
    for i in range(len(lista_fitness)):
        fit[lista_fitness[i][0]] = lista_fitness[i][1]
    two_best = []
    for i in range(2):
        best = None
        for i in range(3):
            ind = random.choice(fit)
            if best == None or best < ind:
                best = ind
        best = pop[fit.index(best)]
        two_best.append(best)
    return two_best

def mutacao(gene):
    for i in gene:
        chance = random.random()
        if chance < taxa_mutacao:
            mutagenico = gene.index(i)
            if mutagenico == len(gene)-1:
                mutagenico2 = gene[0]
                gene[0] = gene[mutagenico]
                gene[mutagenico] = mutagenico2
            else:
                mutagenico2 = gene[mutagenico+1]
                gene[mutagenico+1] = gene[mutagenico]
                gene[mutagenico] = mutagenico2
    return gene

def crossover(pai1,pai2):
    if random.random() < cross_rate:
        filho = []
        filho_p1 = []
        filho_p2 = []

        gen_a = int(random.random() * len(pai1))
        gen_b = int(random.random() * len(pai2))

        comeco = min(gen_a,gen_b)
        fim = max(gen_a,gen_b)

        for i in range(comeco,fim):
            filho_p1.append(pai1[i])

        filho_p2 = [x for x in pai2 if x not in filho_p1]

        filho = filho_p1 + filho_p2
        return mutacao(filho)
    else: return pai1

entrada = [x for x in input().split()]

quantidade_de_pontos = entrada.index(entrada[-3])/3
contador = 0
lista_de_entregas = []
while contador <= quantidade_de_pontos:
    entrada[0] = Ponto_de_entrega(float(entrada[1]),float(entrada[2]),int(entrada[0]))
    lista_de_entregas.append(entrada[0])
    del(entrada[0:3])
    contador += 1

pop_init = pop_inicial(n_pop,lista_de_entregas)

ptr = pontuacao_rotas(pop_init)
menor_distancia = 1/ptr[0][1]
n_teve_melhora = 0
for k in range(repeticoes):
    selected = [selecao(pop_init,ptr) for _ in range(n_pop)]
    prox_gen = list()
    for i in range(n_pop):
        hold = list()
        p1,p2 = selected[i][0],selected[i][1]
        for c in crossover(p1,p2):
            hold.append(c)
        prox_gen.append(hold)
    pop_init = prox_gen
    ptr = pontuacao_rotas(pop_init)
    menor_distancia2 = 1/ptr[0][1]
    if menor_distancia <= menor_distancia2:
        n_teve_melhora += 1
        if n_teve_melhora == ponto_de_parada:
            break
    if menor_distancia > menor_distancia2:
        menor_distancia = menor_distancia2
        n_teve_melhora = 0

print(f'Distancia total: {menor_distancia}')
bestri = ptr[0][0]
bestr = pop_init[bestri]
nomes = []

for i in bestr:
    nomes.append(str(i.name))

print('Rota: '+ ' '.join(nomes))
