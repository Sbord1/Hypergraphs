import heapq


hypergraph_pathname="graphs/ipergrafi_pesati/prova.txt" # arbitrary strings


def hyp_load(hypergraph):
    hfile = open(hypergraph_pathname, encoding="utf8")
    first_row = hfile.readline()
    rows = hfile.readlines()
    hfile.close

    first_row = first_row[:-1] # elimina ultimo carattere \n (contiene nomi dei nodi)


    nodes = [[0, 0, [0], 0]]  # DUMMY NODE - makes visit easier
    node_dict = {0: 0}  # DUMMY NODE - makes visit easier

    nn = first_row.split(',') # , come separatore per la lista (lista con nomi dei nodi)

    i=0
    # print('nn: ',nn)
    for nid in nn:
        # print('node: ',nid)
        nodes.append([0,nid,[],9999])
        i+=1
        node_dict[nid] = i
    # print('nodes: ',nodes)
    # print('node_dict: ',node_dict)
    hyperarcs = [[0,0,[0],0,0]] # DUMMY HYPERARC - makes visit easier
    i=0
    for h in rows:
        i+=1
        # print('processing: ',h)
        source,target = h.split('>')
        target, weight = target.split()
        # print('source: ',source,' - target: ',target)
        ss = source.split(',') #lista con i nodi source
        # print('ss: ',ss)
        source_list = []

        for nid in ss:
            source_list.append(nid)
            nodes[node_dict[nid]][2].append(i)
        hyperarcs.append([0,i,source_list,target,weight])
    hypergraph[0] = nodes
    hypergraph[1] = hyperarcs
    hypergraph[2] = node_dict

def hyp_print(hypergraph):
    print('NODE_DICT [ID,NODE_no]:') # PRINT node dictionary
    i=0
    for nd in hypergraph[2]:
        if i>0:
            print(i,":",nd,":",hypergraph[2][nd])
        i+=1
    print('NODES [REACH-MARK,ID,ADJ-LIST, d[x]:') # PRINT node sequence
    i=0
    for n in hypergraph[0]:
        if i>0:
            print(i,":",n)
        i+=1
    print('HYPERARCS [REACH-MARK,ID,SOURCE,TARGET,WEIGHT]:') # PRINT hyperarcs
    i=0
    for h in hypergraph[1]:
        if i>0:
            print(i,':',h)
        i+=1

def hyp_unmark(hypergraph):
    for n in hypergraph[0]:
        n[0]=1 # RESET TO 1 = UNREACHABLE NODE
    for h in hypergraph[1]:
        h[0]=len(h[2]) # SCANNABILITY VALUE = |SOURCE|

def hyp_visit(hypergraph,source_set):
    hyp_unmark(hypergraph)
    nodes=hypergraph[0]
    hyperarcs=hypergraph[1]
    node_dict=hypergraph[2]
    priority_queue=[(0,0)]
    visited = []
    global childRoot
    childRoot = []# childRoot[y] contiene puntatore all'iperarco (x,y)
    d = [] # d[y] contiene distanza dal source a y

    for _ in range(len(node_dict)):
        childRoot.append(9999)
        d.append(9999)

    ### INITIAL MARKING, INITIAL QUEUE
    scannable= []
    for xi in source_set:
        nodes[node_dict[xi]][0]=0 #reachmark
        nodes[node_dict[xi]][3] = 0
        childRoot[node_dict[xi]]=0 #source
        d[node_dict[xi]] = 0 #source quindi distanza 0
        visited.append(nodes[node_dict[xi]][1])
        for h in nodes[node_dict[xi]][2]:
            hyperarcs[h][0]-=1 # DECREMENT SCANNABILITY VALU
            if hyperarcs[h][0]==0:
                scannable.append(h)
                heapq.heappush(priority_queue,(int(hyperarcs[h][4]),hyperarcs[h][1]))

    weight, hyperarcsID = heapq.heappop(priority_queue)  # tupla (0,0)

    #in scannable ci sono gli hyperarcs
    ### REACH & SCAN AS MUCH AS POSSIBLE
    while len(scannable)>0:



        if len(priority_queue)!=0: #se c'è qualcosa nella coda prendi id e peso iperarco
            weight, hyperarcsID = heapq.heappop(priority_queue)
            scannable.pop()

        #id nodo target dell'iperarco
        t=node_dict[hyperarcs[hyperarcsID][3]]

        # calcolo distanza
        distanza=0
        u=True # flag, se =False allora non conosciamo distanza
        for _ in range(len(hyperarcs[hyperarcsID][2])):
            x = d[node_dict[hyperarcs[hyperarcsID][2][_]]]
            if x!=9999 and u==True: # se conosciamo distanza aggiorna
                distanza+=x
            else:
                u=False
                distanza=-1
                break

        #se non stato visitato lo visito e cambio reachmark
        if nodes[t][0]!=0:
            nodes[t][0]=0
            visited.append(nodes[t][1])
        #aggiorno distanza del nodo
        if distanza!=-1:
            if d[t] > (weight+distanza): #aggiorno d con la distanza migliore
                d[t]= weight + distanza
                childRoot[t] = hyperarcsID

        for h in nodes[t][2]:
            hyperarcs[h][0]-=1# DECREMENT SCANNABILITY VALUE
            if hyperarcs[h][0] < 0: #so that we don't go in negative scannability
                hyperarcs[h][0] = 0
                continue # skip rest of for statement because it would add them to heap
            if hyperarcs[h][0]==0:
                scannable.append(h)
                heapq.heappush(priority_queue, (int(hyperarcs[h][4]), hyperarcs[h][1]))

    #scrivo distanza
    for i in range(len(d)):
        nodes[i][3]=d[i]



hypergraph = [[], [], []]

hyp_load(hypergraph)

hyp_print(hypergraph)

childRoot = []  # childRoot[y] contiene puntatore all'iperarco (x,y)
source_set = [0]

while True:
    num_nodes=len(hypergraph[0])
    source=input('Initial marking? (comma-separated node id): ')
    ss = source.split(',')
    # print('ss -->',ss,'<--')
    if len(ss[0])==0:
        print('No input. Exiting.')
        exit()
    source_set = []
    for xi in ss:
        # print('hypergraph[2].get(xi,\'0\'): ', hypergraph[2].get(xi,'0'))
        source_set.append(xi)
        if int(hypergraph[2].get(xi,'0'))==0:
            print('Non-existent identifiers. Exiting.')
            exit()
    # print('source_set: ',source_set)
    hyp_visit(hypergraph,source_set)
    hyp_print(hypergraph)


