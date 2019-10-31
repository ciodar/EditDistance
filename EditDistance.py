cost = [4,5,1,2,3]
#cost = {"copy":1}

def edit_distance(x,y):
    m = len(x)
    n = len(y)
    c =  [[0 for j in range(n+1)] for i in range(m+1)]
    op = [["0" for j in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        c[i][0] = i * cost[0]
        op[i][0] = "delete"
    for j in range(n+1):
        c[0][j] = j * cost[1]
        op[0][j] = "insert"
    for i in range(1,m+1):
        for j in range(1,n+1):
            c[i][j] = 10000
            #Se xi e yj sono uguali -> copy
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + cost[2]
                op[i][j] = "copy"
            #Se xi e yi sono diversi e il costo -> replace
            if x[i-1] != y[j-1] and c[i-1][j-1] + cost[3] < c[i][j]:
                c[i][j] = c[i-1][j-1] + cost[3]
                op[i][j] = "replace"
            #Se xi e yi sono diversi e xi-1 = yi e yi-1 = xi -> twiddle
            if i >= 2 and j >=2 and x[i-1] == y[j-2] and x[i-2] == y[j-1] and c[i-2][j-2] + cost[4] < c[i][j]:
                c[i][j] = c[i-2][j-2] + cost[4]
                op[i][j] = "twiddle"
            #Se xi e yi sono diversi -> delete
            if c[i-1][j] + cost[0] < c[i][j]:
                c[i][j] = c[i-1][j] + cost[0]
                op[i][j] = "delete"
            #SE xi e yi sono diversi -> insert
            if c[i][j-1] + cost[1] < c[i][j]:
                c[i][j] = c[i][j-1] + cost[1]
                op[i][j] = "insert"
    #print c
    return c,op

def createSet(file):
    s = set()
    for linea in file:
        parola = linea.replace("\n", "")
        s.add(parola)
    return s

def createDictionary(set, n):
    d = {}
    for parola in set:
        nGrams = n_grams(parola, n)
        for nGram in nGrams :
            if d.has_key(nGram):
                d[nGram].add(parola)
            else :
                d[nGram] = {parola}
    return d

def findFromSet(set, daCercare):
    print "Cerco in set :", daCercare
    min = 100000
    if len(set) != 0:
        for parola in set:
            dist,op = distance(daCercare, parola)
            if dist < min :
                min = dist
                vicina = parola
        if min == 0 :
            #print "Parola trovata!"
            return True
    #print "Parola non trovata!"
    print "Parola piu' vicina :" , vicina , " - distanza :" , min
    op_sequence(op,len(vicina),len(parola))
    return False

def findFromNGram(d, daCercare, n):
    #print "Cerco con n-gram :", daCercare
    s = set()
    nGrams = n_grams(daCercare, n)
    for nGram in nGrams :
        if d.has_key(nGram):
            #print "D ha", nGram
            #print d[nGram]
            s = s.union(d[nGram])
    #print s
    findFromSet(s, daCercare)

def n_grams(parola , n):
    output = []
    for i in range(len(parola) - n + 1):
        output.append(parola[i:i + n])
    return output

def distance(x, y):
    list,op = edit_distance(x, y)
    return list[-1][-1],op

def op_sequence(op,i,j):
    if i==0 and j==0:
        return
    if op[i][j] =="copy" or op[i][j]=="replace":
        k=i-1
        l=j-1
    elif op[i][j] == "twiddle":
        k=i-2
        l=j-2
    elif op[i][j] == "delete":
        k=i-1
        l=j
    else:
        k=i
        l=j-1
    op_sequence(op,k,l)
    print op[i][j]

'''
if __name__ == '__main__':

    #nome = input('Inserisci la parola: ')
    p = open('prova.txt', 'r')
    f = open('280000parole.txt', 'r')


    set = createSet(f)
    print "Set : ", set

    findFromSet(set ,"casa")

    d = createDictionary(set,2)
    print "Dizionario : ", d

    findFromNGram(d, "trasformare", 2)

'''


