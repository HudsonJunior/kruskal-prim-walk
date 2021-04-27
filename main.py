# Trabalho elaborado pelo discente Hudson Rogerio Proenca Junior  R.A: 108756

import random
import math

peso = 0
extremo1 = 0
extremo2 = 1
key = 0
qtd_arv = 500

def bfs(adj,s):
    dist = []
    cor = []

    for i in range(len(adj)):
        cor.append("Branco")
        dist.append(-1)

    cor[s] = "Cinza"
    dist[s] = 0
    Q = []
    Q.append(s)
    i = 0
    while i < len(Q):
        u = Q[i]
        i = i+1 
        for v in adj[u]:
            if cor[v] == "Branco":
                dist[v] = dist[u] + 1
                cor[v] = "Cinza"
                Q.append(v)
        cor[u] = "Preto"
    return dist

def maior_dist(dist):
    maior = max(dist)
    for i in range(len(dist)):
        if dist[i] == maior:
            return (maior,i)


def diametro(adj):
    dist = bfs(adj,0)
    maior,verticeA = maior_dist(dist)
    dist = bfs(adj,verticeA)
    maior,verticeB = maior_dist(dist)
    return maior

def diametro_medio(soma):
    return soma/qtd_arv


def eh_arvore(adj,arestas):
    if arestas != len(adj) -1:
        return False
    s = 0
    dist = bfs(adj,s)
    return (-1 not in dist)

def make_set(p,rank,x):
    p[x] = x
    rank[x] = 0

def link(p,rank,x,y):
    if rank[x] >= rank[y]:
        p[y] = x

    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] = rank[y]+1

def find_set(p,x):
    if x != p[x]:
        p[x] = find_set(p,p[x])
    return p[x]

def union(p,rank,x,y):
    link(p,rank,find_set(p,x),find_set(p,y))

def adicionar_aresta(adj,u,v):
	adj[u].append(v)
	adj[v].append(u)

def mst_kruskal(adj,w):
    A = []
    p = []
    rank = []
    for i in range(len(adj)):
        p.append(0)
        rank.append(0)

    
    for v in range(len(adj)):
        make_set(p,rank,v)

    w.sort(key = lambda x:x[peso])

    for (pesoo,aresta) in w:
        if find_set(p,aresta[extremo1]) != find_set(p,aresta[extremo2]):     
            A.append((aresta))
            adicionar_aresta(adj,aresta[extremo1],aresta[extremo2])
            union(p,rank,aresta[extremo1],aresta[extremo2])

    return A


def mst_prim(adj,w,r):
    chave = []
    pai = []
    Q = []
    adj2 = []
    visitado = []
    for u in range(len(adj)):
        chave.append(math.inf)
        pai.append(-1)
        Q.append(u)
        adj2.append([])
        visitado.append(False)
    chave[r] = 0

    while Q != []:
        u = min(Q,key = lambda x:chave[x])
        Q.remove(u)
        visitado[u] = True

        if pai[u] != -1:
            adicionar_aresta(adj2,pai[u],u)

        for v in adj[u]:
            if not visitado[v] and w[u][v] < chave[v]:
                pai[v] = u
                chave[v] = w[u][v]          
    return adj2

def random_tree_prim(n):
    adj = []

    for i in range(n):
        adj.append([])

    w = [[0] * n for i in range(len(adj))]
    for i in range(len(adj)):
        for j in range(i+1,len(adj)):
            peso = random.random()
            w[i][j] = peso
            w[j][i] = peso
            adicionar_aresta(adj,i,j)
    
    s = 0
    A = mst_prim(adj,w,s)

    return (A,len(A)-1)

def randon_tree_random_walk(n):
    adj = [[] for i in range(n)]
    arestas = 0
    visitado = []
    for u in range(n):
        visitado.append(False)
    u = random.randint(0,n-1)
    visitado[u] = True

    while arestas < n-1:
        v = random.randint(0,n-1)
        if not(visitado[v]):
            arestas = arestas+1
            visitado[v] = True
            adicionar_aresta(adj,u,v)
           # adj[v].append(u)
            #adj[u].append(v)
        u = v
    return (adj,arestas)


def random_tree_kruskal(n):
    adj = [[] for i in range(n)]
    arestas = []
    w = []

    for i in range(len(adj)):
        for j in range(i+1,len(adj)):
                w.append((random.random(),(i,j)));

    A = mst_kruskal(adj,w)

    return (adj,len(A))


adj = [[1,2],[0],[0,3],[2]]

#        ( 0 ) - - - - - ( 1 )
#          '
#          '
#        ( 2 ) - - - - - ( 3 )

adj1 =[[2,3],[2],[0,1],[0,4],[3,5],[4]]

#        ( 0 ) - - - - - ( 2 ) - - - - ( 1 )
#          '
#          '
#          '
#        ( 3 )
#          '
#          '
#        ( 4 ) - - - - - -( 5 )

adj2 =[[2,4],[2],[0,1],[5],[6,5,0],[4,3],[4]]

#        ( 0 ) - - - - - ( 2 ) - - - - ( 1 )    
#          '
#          '
#          '
#        ( 4 )
#       ´      `
#     ´          `
#  ( 5 )         ( 6 )
#    '
#    '
#  ( 3 )

adj3 = [[1],[0,2],[1,3,4],[2],[2,5],[4]]

#        ( 0 ) - - - - - ( 1 ) - - - - ( 2 )   
#                                     ´      `
#                                   ´          `
#                                ( 4 )         ( 3 )
#                                  '
#                                  '
#                                  '
#                                ( 5 )

adj4 = [[1,3],[0,2],[1],[0,4],[3,5],[4,6],[5,7],[6]]

#     ( 1 ) - - - - ( 0 )         ( 5 ) - - - - ( 6 )
#       '             '             '             '
#       '             '             '             '
#       '             '             '             '
#     ( 2 )         ( 3 ) - - - - ( 4 )         ( 7 )



dist = bfs(adj,0)
assert dist[1] == 1
assert dist[2] == 1
assert dist[3] == 2

dist = bfs(adj1,0)
assert dist[1] == 2
assert dist[2] == 1
assert dist[3] == 1
assert dist[4] == 2
assert dist[5] == 3

dist = bfs(adj2,0)
assert dist[1] == 2 
assert dist[2] == 1
assert dist[3] == 3
assert dist[4] == 1
assert dist[5] == 2
assert dist[6] == 2

dist = bfs(adj3,0)
assert dist[1] == 1
assert dist[2] == 2
assert dist[3] == 3
assert dist[4] == 3
assert dist[5] == 4 

dist = bfs(adj4,0)
assert dist[1] == 1
assert dist[2] == 2
assert dist[3] == 1
assert dist[4] == 2
assert dist[5] == 3
assert dist[6] == 4
assert dist[7] == 5


diam = diametro(adj)
assert diam == 3

diam = diametro(adj1)
assert diam == 5

diam = diametro(adj2)
assert diam == 5

diam = diametro(adj3)
assert diam == 4

diam = diametro(adj4)
assert diam == 7


adj = [[] for i in range(9)]
a,b,c,d,e,f,g,h,i = range(9)

w = [(4,(a,b)),(8,(b,c)),(2,(c,i)),(8,(a,h)),(1,(h,g)),(6,(i,g)),(7,(i,h)),(2,(g,f)),(7,(c,d)),(4,(c,f)),(9,(d,e)),(10,(e,f)),(14,(d,f)),(11,(b,h))]
mst_kruskal(adj,w)

assert adj[0][0] == 1


assert adj[1][0] == 0
assert adj[1][1] == 2

assert adj[2][0] == 8
assert adj[2][1] == 5
assert adj[2][2] == 3
assert adj[2][3] == 1

assert adj[3][0] == 2
assert adj[3][1] == 4

assert adj[4][0] == 3

assert adj[5][0] == 6
assert adj[5][1] == 2

assert adj[6][0] == 7
assert adj[6][1] == 5

assert adj[7][0] == 6

assert adj[8][0] == 2

x = 10
y = 12
p = [0 for i in range(15)]
rank = [0 for i in range(15)]

make_set(p,rank,x)
make_set(p,rank,y)

assert rank[x] == 0
assert p[x] == x

assert rank[y] == 0
assert p[y] == y


P = find_set(p,10)
assert P == 10
P = find_set(p,12)
assert P == 12

union(p,rank,x,y)
assert p[y] == x





adj = [[] for i in range(9)]
u = 5
v = 8
adicionar_aresta(adj,u,v)
assert adj[u][0] == v
assert adj[v][0] == u

w = [[0] * 9 for i in range(9)]
a,b,c,d,e,f,g,h,i = range(9)
w[a][b] = 4
w[a][h] = 8
w[b][a] = 4
w[b][c] = 8
w[b][h] = 11
w[c][b] = 8
w[c][d] = 7
w[c][f] = 4
w[c][i] = 2
w[d][c] = 7
w[d][e] = 9
w[d][f] = 14
w[e][d] = 9
w[e][f] = 10
w[f][c] = 4
w[f][d] = 14
w[f][e] = 10
w[f][g] = 2
w[g][f] = 2
w[g][h] = 1
w[g][i] = 6
w[h][a] = 8
w[h][g] = 1
w[h][i] = 7
w[i][c] = 2
w[i][g] = 6
w[i][h] = 7

adj = [[b,h],[a,h,c],[b,i,d,f],[c,e,f],[d,f],[c,d,e,g],[h,f,i],[a,g,i],[c,h,g]]
adj2 = mst_prim(adj,w,0)

assert adj2[a][0] == b
assert adj2[b][0] == a
assert adj2[b][1] == c
assert adj2[c][0] == b
assert adj2[c][1] == i
assert adj2[c][2] == f
assert adj2[c][3] == d
assert adj2[d][0] == c
assert adj2[d][1] == e
assert adj2[e][0] == d
assert adj2[f][0] == c
assert adj2[f][1] == g
assert adj2[g][0] == f
assert adj2[g][1] == h
assert adj2[h][0] == g
assert adj2[i][0] == c



print("-RandomKruskal\n-RandomPrim\n-RandomWalk")
alg_arvore = input()
arq_arvore = open(alg_arvore + ".txt",'w')

for n in range(250,2250,250):
    soma = 0
    for i in range(500):
        if(alg_arvore == "RandomKruskal"):
        	adj,qtd_arestas = random_tree_kruskal(n)

        elif(alg_arvore == "RandomPrim"):
        	adj,qtd_arestas = random_tree_prim(n)

        elif(alg_arvore == "RandomWalk"):
        	adj,qtd_arestas = randon_tree_random_walk(n)
        
        else:
        	print("Algoritmo inválido!")
        	break;

        assert eh_arvore(adj,qtd_arestas)

        diam = diametro(adj)
        soma += diam

    media = diametro_medio(soma)
    string = str(n) + ' ' + str(media) + '\n'
    arq_arvore.writelines(string)

arq_arvore.close()
