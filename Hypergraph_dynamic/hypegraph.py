import heapq


hypergraph_pathname="/Users/Francesco/Desktop/Hypergraphs/Hypergraph_dynamic/graphs/ipergrafi_pesati/hga_plus.txt" # arbitrary strings
alphabet= "0ABCDEFGHIJKLMNOPQRSTUVWXYZ" # we are going to use it to add new nodes
hypergraph = [[], [], []]
hyperarcs_T = [] #lista iperarchi il cui source è raggiungibile
PQ=[] #priority queue utilizzata per improve_weight
global childRoot
childRoot = []  # childRoot[y] contiene puntatore all'iperarco (x,y)
global measure
measure='1' # by default this Gap the measure function
global source_set

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
        n[3]=9999
    for h in hypergraph[1]:
        h[0]=len(h[2]) # SCANNABILITY VALUE = |SOURCE|


def hyp_visit(hypergraph,source_set,measure):

    # Reset visit markers in the hypergraph
    hyp_unmark(hypergraph)

    nodes = hypergraph[0]
    hyperarcs = hypergraph[1]
    node_dict = hypergraph[2]

    # Initialize priority queue with a dummy value
    priority_queue = [(0, 0)]
    visited = []

    # Global variables
    global childRoot
    childRoot = []  # childRoot[y] contains a pointer to the hyperarc (x, y)
    d = []  # d[y] contains the distance from the source to y
    global hyperarcs_T
    hyperarcs_T = []  # List of hyperarcs whose source is reachable

    # Initialization of the distance and childRoot lists
    for _ in range(len(node_dict)):
        childRoot.append(9999)
        if measure=='2':
            d.append(0)
        else:
            d.append(9999)

    ### INITIAL MARKING, INITIAL QUEUE
    scannable= []
    for xi in source_set:
        # Set reachmark, initial distance, and childRoot for nodes in the source set
        nodes[node_dict[xi]][0]=0 #reachmark
        nodes[node_dict[xi]][3] = 0 # initial distance
        childRoot[node_dict[xi]]=0 # source
        d[node_dict[xi]] = 0  # source, so distance is 0
        visited.append(nodes[node_dict[xi]][1])

        # Update scannability and add hyperarcs to the priority queue
        for h in nodes[node_dict[xi]][2]:
            hyperarcs[h][0]-=1 # DECREMENT SCANNABILITY VALUE
            if hyperarcs[h][0]==0:
                hyperarcs_T.append(hyperarcs[h][1])
                scannable.append(h)
                heapq.heappush(priority_queue,(int(hyperarcs[h][4]),hyperarcs[h][1]))

    # Extract the first hyperarc from the priority queue
    weight, hyperarcsID = heapq.heappop(priority_queue)  # dummy tuple (0,0)

    # In scannable, there are hyperarcs ready for exploration
    ### REACH & SCAN AS MUCH AS POSSIBLE
    while len(scannable)>0:

        if len(priority_queue)!=0: # If there is something in the queue, get the hyperarc ID and weight
            weight, hyperarcsID = heapq.heappop(priority_queue)
            scannable.pop()

        # Target node ID of the hyperarc
        t=node_dict[hyperarcs[hyperarcsID][3]]

        # Calculate measure: GAP
        if measure=='1':

            misura=9999
            u=True # Flag, if False, then we don't know the distance
            for _ in range(len(hyperarcs[hyperarcsID][2])):
                x = d[node_dict[hyperarcs[hyperarcsID][2][_]]] # Distance from the source
                if x!=9999 and u==True: # If we know the distance, update
                    misura=min(misura,x)
                    misura = weight + misura
                else:
                    u=False
                    misura=-1
                    break

        # Calculate measure: RANK
        if measure=='2':

            misura=9999
            u=True # Flag, if False, then we don't know the distance
            for _ in range(len(hyperarcs[hyperarcsID][2])):
                x = d[node_dict[hyperarcs[hyperarcsID][2][_]]] # Distance from the source
                if x!=9999 and u==True: # If we know the distance, update
                    misura=min(misura,x)
                    misura = weight + misura
                else:
                    u=False
                    misura=-1
                    break

        # Calculate measure: TRAVERSAL-COST
        if measure=='3':

            misura = 0
            u = True  # Flag, if False, then we don't know the distance
            for _ in range(len(hyperarcs[hyperarcsID][2])):
                x = d[node_dict[hyperarcs[hyperarcsID][2][_]]]  # Distance from the source
                if x != 9999 and u == True:  # If we know the distance, update
                    calcolo = x + weight
                else:
                    u = False
                    misura = -1
                    break
                misura += calcolo

        # If the node has not been visited, mark it as visited and update reachmark
        if nodes[t][0]!=0:
            nodes[t][0]=0
            visited.append(nodes[t][1])

        # Update the distance of the node
        if misura!=-1:
            pre_d=d[t]

            # if d[t] < misura: #aggiorno d con la misura MASSIMA

            if measure=='1':
                # Update distance with the minimum measure (GAP)
                if d[t] > misura:
                    d[t]= misura
                    childRoot[t] = hyperarcsID

            if measure=='2':
                # Update distance with the maximum measure (RANK)
                if d[t] < misura:
                    d[t] = misura
                    childRoot[t] = hyperarcsID

            if measure=='3':
                # Update distance with the sum of measures (Traversal)
                if pre_d != 9999:
                    d[t] += misura
                    childRoot[t] = hyperarcsID
                else:
                    d[t] = misura

                if pre_d!=9999:
                    for i in nodes[t][2]:
                        scannable.append(i)
                        heapq.heappush(priority_queue, (int(hyperarcs[i][4]), hyperarcs[i][1]))

        # Update scannability and add hyperarcs to scannable for further exploration
        for h in nodes[t][2]:
            hyperarcs[h][0]-=1 # DECREMENT SCANNABILITY VALUE
            if hyperarcs[h][0] < 0: # To prevent negative scannability
                hyperarcs[h][0] = 0
                continue # skip rest of for statement because it would add them to heap
            if hyperarcs[h][0]==0:
                hyperarcs_T.append(hyperarcs[h][1])
                scannable.append(h)
                heapq.heappush(priority_queue, (int(hyperarcs[h][4]), hyperarcs[h][1]))

    # Update the effective distance for the nodes
    for i in range(len(d)):
        nodes[i][3]=d[i]

def improve_weight(hypergraph,id,measure):
    hyperarcs = hypergraph[1]
    nodes = hypergraph[0]
    node_dict = hypergraph[2]
    global PQ

    w = int(input("Assign a weight to this hyperarc: "))
    hyperarcs[id][4] = w



    # check if we can reach the node
    traversable=False
    for s in hyperarcs[id][2]:
        if nodes[node_dict[s]][3] != 9999:
            traversable=True
        else:
            traversable=False
    if traversable==True:
        hyperarcs_T.append(id)

    if hyperarcs[id][1] in hyperarcs_T:
        scan_hyperarc(hypergraph,id,measure)

    while len(PQ)>0:

        d,z = heapq.heappop(PQ) #extract minimum node with priority d

        # Check distance iteratively
        for i in nodes[z][2]:
            if hyperarcs[i][1] in hyperarcs_T:
                scan_hyperarc(hypergraph, i,measure)

def scan_hyperarc(hypergraph,id,measure):
    global PQ
    global childRoot
    global source_set
    nodes = hypergraph[0]
    hyperarcs = hypergraph[1]
    node_dict = hypergraph[2]
    w=int(hyperarcs[id][4]) #weight hyperarc

    t=node_dict[hyperarcs[id][3]] #target node
    pre_d=nodes[t][3] #distanza dal source del target node prima che cambiassi peso

    #controllo distanza del source dell'iperarco cambiato
    post_d=w

    for _ in range(len(hyperarcs[id][2])):
        x = nodes[node_dict[hyperarcs[id][2][_]]][3]
        post_d+=x

    # se cambiamo peso dell'iperarco associato al sottoalbero, devo ricalcolare
    if childRoot[t] == id:
        hyp_visit(hypergraph,source_set,measure)
        return

    # Rank
    if measure=='2':
        if post_d > pre_d:
            childRoot[t] = id
            nodes[t][3] = post_d
            heapq.heappush(PQ, (post_d, t))  # insert node t with priority post_d
    else:
        # Trasversal and Gap
        if post_d < pre_d:
            childRoot[t] = id
            nodes[t][3]=post_d
            heapq.heappush(PQ,(post_d,t)) #insert node t with priority post_d



def insert_hyperarc(hypergraph,measure):
    nodes = hypergraph[0]
    hyperarcs = hypergraph[1]
    node_dict = hypergraph[2]
    global childRoot

    source = input("Insert source (comma-separated node id): ").upper().split(',')
    target = input("Insert target id Node: ").upper()
    weight = input("Insert weight: ")
    assigned_source_node = []

    if len(target) != 1:
        print("Error: target length too big")
        return

    # create empty hyperarc, it will be filled later
    id_hyperarc = hyperarcs[-1][1] + 1
    hyperarcs.append([0, id_hyperarc, [], 0, weight])

    # check if nodes in source exist, otherwise create it/them
    for s in source:

        if s not in node_dict:
            id_node = max(node_dict.values()) + 1
            s = alphabet[id_node]
            node_dict[s] = id_node # create new node in dictionary
            nodes.append([0, s, [], 9999]) # create new node in nodes list

        # update hyperarc source_set
        hyperarcs[id_hyperarc][2].append(s)

        # update ADJ-LIST of source
        nodes[node_dict[s]][2].append(id_hyperarc)

        assigned_source_node.append(s)

    # check if target node exist, otherwise create it
    if target not in node_dict:
        id_node = max(node_dict.values()) + 1
        target = alphabet[id_node]
        node_dict[target] = id_node  # create new node in dictionary
        nodes.append([0, target,[], 9999])  # create new node in nodes list

    hyperarcs[id_hyperarc][3] = target

    print("Inserted hyperarc with source:",assigned_source_node)
    print("Inserted hyperarc with target:", target)

    # update childRoot
    number_new_nodes = len(node_dict)-len(childRoot)
    for i in range(number_new_nodes):
        childRoot.append(9999)

    # update distance from source
    scan_hyperarc(hypergraph, id_hyperarc,measure)

#------
    while len(PQ) > 0:

        d, z = heapq.heappop(PQ)  # extract minimum node with priority d
        # Check distance iteratively

        for i in nodes[z][2]:
                scan_hyperarc(hypergraph, i, measure)


def general_menu():
    print("Menu:")
    print("1. Enter initial marking")
    print("2. Display hypergraph information")
    print("3. Change hyperarc weight")
    print("4. Insert new hyperarc")
    print("5. Quit")
    print("")

def measure_menu():
    print("1. Gap")
    print("2. Rank")
    print("3. Traversal cost")
    print("4. Bottleneck")
    print("5. Threshold")
    print("")
# ---------------------------------------------------------------
# MAIN
hyp_load(hypergraph)

# Visit the first time
source = input('Initial marking? (comma-separated node id): ')
ss = source.split(',')

if len(ss[0]) == 0:
    print('No input. Exiting.')
    exit()

source_set = []

for xi in ss:
    source_set.append(xi)
    if int(hypergraph[2].get(xi, '0')) == 0:
        print('Non-existent identifiers. Exiting.')
        exit()

hyp_visit(hypergraph, source_set, '1')
hyp_print(hypergraph)

while True:
    print(measure)
    general_menu()
    choice = input("Enter your choice: ")

    # Ask which measure function to use
    if choice == "1":
        measure_menu()

        measure = input("Enter your measure: ")

        # User wants to enter initial marking
        source = input('Initial marking? (comma-separated node id): ')
        ss = source.split(',')

        if len(ss[0]) == 0:
            print('No input. Exiting.')
            exit()

        source_set = []
        for xi in ss:
            source_set.append(xi)
            if int(hypergraph[2].get(xi, '0')) == 0:
                print('Non-existent identifiers. Exiting.')
                exit()

        if measure == "1":
            # User choose Gap measure function
            hyp_visit(hypergraph, source_set, measure)
            hyp_print(hypergraph)
            print("")

        elif measure == "2":
            # User choose Rank measure function
            hyp_visit(hypergraph, source_set, measure)
            hyp_print(hypergraph)
            print("")

        elif measure == "3":
            # User choose Traversal measure function
            hyp_visit(hypergraph, source_set, measure)
            hyp_print(hypergraph)
            print("")

    elif choice == "2":
        # User wants to display hypergraph information
        hyp_print(hypergraph)

    elif choice == "3":
        # User wants to change hyperarc weight
        id = int(input("Insert hyperarc id: "))

        # Check that id exists
        if id < len(hypergraph[1]) and id > 0:
            improve_weight(hypergraph, id,measure)
            hyp_print(hypergraph)
        else:
            print("id not found")

    elif choice == "4":
        # User wants to insert new hyperarc
        insert_hyperarc(hypergraph,measure)
        hyp_print(hypergraph)

    elif choice == "5":
        print("Exiting.")
        break

    else:
        print("Invalid choice. Please select a valid option.")

