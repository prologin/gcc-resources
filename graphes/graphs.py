###################
#                 #
#   G R A P H S   #
#                 #
###################

from algopy import graph, graphmat, queue

def degrees (G):
    Din = [0] * G.order
    Dout = [0] * G.order
    for s in range (G.order):
        Dout[s] = len(G.adjlists[s])
        for adj in G.adjlists[s]:
            Din[adj] += 1
    return (Din, Dout)

def degreesMat (G):
    (din, dout) = (0, 0)
    for s in range (G.order):
        (din_s, dout_s) = (0, 0)
        for adj in range (G.order):
                dout_s += G.adj[s][adj]
                din_s += G.adj[adj][s]
        din = max (din, din_s)
        dout = max(dout, dout_s)
    return (din, dout)

#############
#   B F S   #
#############

def __bfs (G, src, p):
    q = queue.Queue()
    q.enqueue(src)
    p[src] = -1
    while not q.isempty():
        s = q.dequeue()
        for adj in G.adjlists[s]: #change if working with MatAdj
            if p[adj] == None:
                p[adj] = s
                q.enqueue(adj)

def __bfsMat (G, src, p):
    q = queue.Queue()
    q.enqueue(src)
    p[src] = -1
    while not q.isempty():
        s = q.dequeue()
        for adj in range (G.order): #
            if G.adj[s][adj]:       #
                if p[adj] == None:
                    p[adj] = s
                    q.enqueue(adj)

def bfs (G):
    p = [None] * G.order
    for s in range (G.order):
        if p[s] == None:
            __bfs (G, s, p)
    return p

#############
#   D F S   #
#############

def __dfs (G, s, M):
    M[s] = True
    for adj in G.adjlists[s]:
        if not M[adj]:
           __dfs (G, adj, M) 

def dfs (G):
    M = [False] * G.order
    for s in range (G.order):
        if not M[s]:
            __dfs (G, s, M)

###############################
#   A P P L I C A T I O N S   #
###############################

def __pathbfs (G, src, dst, p):
    q = queue.Queue()
    q.enqueue(src)
    p[src] = -1
    while not q.isempty():
        s = q.dequeue()
        for adj in G.adjlists[s]:
            if p[adj] == None:
                p[adj] = s
                if adj == dst:
                    return True
                q.enqueue(adj)
    return False

def pathbfs (G, src, dst):
    p = [None] * G.order
    path = []
    if __pathbfs(G, src, dst, p):
        while dst != -1:
            path.insert(0, dst)
            dst = p[dst]
    return path

def __pathdfs (G, src, dst, M, path):
    M[src] = True
    for adj in G.adjlists[s]:
        if not M[adj]:
            if adj == dst or __pathdfs(G, adj, dst, M, path):
                path.insert(0, adj)
                return True
    return False

def pathdfs (G, src, dst):
    M = [False] * G.order
    path = []
    if __pathdfs (G, src, dst, M, path):
        path.insert(0, src)
    return path

def __dfsForest(G, s, p):
    for adj in range(G.order):
        if G.adj[s][adj]:
            if p[adj] == None: # tree edge
                p[adj] = s     # vertices has to be marked here
                print(s, "->", adj)
                __dfsForest(G, adj, p)
            else:
                if adj != p[s]:
                    print(s, '->', adj, "back edge")  #unless adj -> s is a back edge!

def dfsForest(G):
    p = [None] * G.order
    for s in range(G.order):
        if p[s] == None:
            p[s] = -1
            __dfsForest(G, s, p)
    return p

def __DFS (G, s, p):
    for adj in G.adjlists[s]:
        if p[adj] == None:
            p[adj] = s
            __DFS (G, adj, p)
        else:
            if adj != p[s]
                print (s, ' -> ', )

'''
    Arc Avant : ne sert a rien
    Arc Retour : denote l'existence d'un circuit
    Arc Croise : utile ssi relie a un circuit passant par un ancetre du dit arc croise
'''

def __dfsDigraphPrefSuff (G, x, pref, suff, cpt):
    cpt += 1
    pref[x] = cpt
    for y in G.adjlists[x]:
        if pref[y] == 0 :
           cpt = __dfsDigraphPrefSuff (G, y, pref, suff, cpt)
        else :
            if pref[x] < pref[y]:
                print (x, ' -> ', y, ' (Forward)')
            elif suff[y] == 0 :
                print (x, ' -> ', y, ' (Back)')
            else :
                print (x, ' -> ', y, ' (Cross)')
    cpt += 1
    suff[s] = cpt
    return cpt

def dfsDigraphPrefSuff (G):
    pref = [0] * G.order
    suff = [0] * G.order 
    cpt = 0
    for s in range (G.order):
        if pref[s] == 0:
            cpt = __dfsDigraphPrefSuff (G, s, pref, suff, cpt)
    return (pref, suff)

#Components

def __components (G, x, pref, suff, cpt):
    cc[x] = nbrcc
    for y in G.adjlists[x]:
        if cc[y] == 0:
            __components (G, y, cc, nbrcc)

def components (G):
    '''
        Determine les composantes connexes en utilisant un parcours profondeur
    '''
    cc = [0] * G.order
    nbrcc = 0 
    for s in range (G.order):
        if pref[s] == 0:
            nbrcc += 1
            __components (G, s, cc, nbrcc)
    return (nbrcc, cc)

def isConnex (G):
    '''
        incrementer un cpt en dfs achque fois qu'on passe sur un sommet
        comparer dans la fonction d'appel si le cpt == G.order
    '''
    #TODO
    pass
    '''
    pour chaque adj de s :
        si adj non marque
            si s est rouge
                adj est bleu
            sinon
                adj est rouge
        sinon
            si adj est de meme couleur que s
            return False
    '''
    #TODO union find = tri evolutif
    # check file S4

#Bipartite

def __isBipartiteBFS (G, s, M):
    q = queue.Queue()
    q.enqueue(src)
    M[s] = -1
    while not q.isempty():
        s = q.dequeue()
        for adj in G.adjlists[s]:
            if M[adj] == 0:       
                M[adj] = -M[s]
                q.enqueue(adj)
            else:
                if M[adj] = M[s]:  
                    return False
    return True

def __isBipartiteDFS(G, s, M):
    for adj in G.adjlists:
        if M[adj] == 0:
            M[adj] = -M[s]
            if not __isBipartiteDFS(G, adj, M):
                return False
        else:
            if M[adj] == M[s]:
                return False
    return True

def isBipartiteBFS(G):
    M = [0] * G.order #0 = non marque / 1 = premier ensemble / -1 = second ensemble
    for s in range (G.order):
        if M[s] == 0:
            if not __isBipartiteBFS(G, s, M):
                return False
    return True

def isBipartiteDFS(G):
    M = [0] * G.order #0 = non marque / 1 = premier ensemble / -1 = second ensemble
    for s in range (G.order):
        if M[s] == 0:
            M[s] = 1
            if not __isBipartiteBFS(G, s, M):
                return False
    return True

#Acyclic : dfs

def __isAcyclic(G, s, M, suff):
    M[s] = True
    for adj in G.adjlists[s]:
        if not M[adj]:
            if not __isAcyclic(G, s, M, suff):
                return False
        else:
            if not suff[adj]:
                return False
    suff[adj] = True
    return True

def isAcyclic(G):
    M = [False] * G.order
    suff = [False] * G.order
    for s in range (G.order):
        if not M[s]:
            if not __isAcyclic(G, s, M, suff):
                return False
    return True

'''
    dans la theorie des graphes : arbre = graphe connexe sans cycle
'''

#Diameter : bfs

def __diameter(G, s):
    dist = [None] * G.order
    dist[s] = 0
    q = queue.Queue()
    q.enqueue(s)
    actual = 0
    while not q.isempty():
        s = q.dequeue()
        for adj in G.adjlists[s]:
            if dist[adj] == None:
                dist[adj] = dist[s]
                q.enqueue(adj)
    return (s, dist[s])

def diameter(G):
    (s, _) = __diameter(G, 0)
    (_, diam) = __diameter(G, s)
    return diam

'''
    Graphe de dependance :
        - ne contient pas de circuits
        - chaque tache depend de la precedente

    tant que G != vide
        choisir x de deg- = 0
        supprimer x de G

    Mq : suff[u] > suff[v]
    graphe sans circuit
    + parcours profondeur <=> pas d'arc retour
    = suff[u] > suff[v] CQFD

    solution tri topologique
    = ordre suffixe inverse du parcours profondeur
'''

#Topological Order : dfs

def dfsSuff (G, s, M, L):
    M[s] = True
    for adj in G.adjlists[s]:
        if not M[adj]:
           __dfs (G, adj, M, L)
    L.insert(0, s)

def topologicalOrder(G):
    M = [False] * G.order
    L = []
    for s in range (G.order):
        if not M[s]:
            dfsSuff(G, s, M, L)
    return L

###############
#   M A I N   #
###############

