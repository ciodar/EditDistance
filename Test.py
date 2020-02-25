from timeit import default_timer as timer
from EditDistance import findFromSet
from EditDistance import findFromNGram
from EditDistance import createSet
from EditDistance import createDictionary

def testRicercaEdit(set, daCercare):
    start = timer()
    findFromSet(set, daCercare)
    end = timer()
    print "\tTempo ricerca senza n-gram :", end-start

def testRicercaNGram(set, daCercare, n):
    print "ricerca ",n,"-gram"
    d = createDictionary(set, n)
    start = timer()
    findFromNGram(d, daCercare, n)
    end = timer()
    print "\tTempo ricerca", n,"- gram :", end-start



if __name__ == '__main__':

    f1 = open('280000parole.txt', 'r')
    f2 = open('660000parole.txt', 'r')

    parole_presenti = ["sommario","appello","idoneo","artificiale","algoritmo"]
    parole_assenti = ["agrolitmo","lorem","kruskal","dolor","prim"]

    print "[Test su lessico di 280000 parole]"
    set1 = createSet(f1)

    for parola1 in parole_presenti:
        print "Ricerca parola :", parola1
        testRicercaEdit(set1, parola1)

        testRicercaNGram(set1, parola1, 2)
        testRicercaNGram(set1, parola1, 3)
        testRicercaNGram(set1, parola1, 4)
    for parola2 in parole_assenti:
        print "Ricerca parola :",parola2
        testRicercaEdit(set1, parola2)

        testRicercaNGram(set1, parola2, 2)
        testRicercaNGram(set1, parola2, 3)
        testRicercaNGram(set1, parola2, 4)

    print "[Test su lessico di 660000 parole]"
    set2 = createSet(f2)
    for parola1 in parole_presenti:
        print "Ricerca parola :", parola1
        testRicercaEdit(set2, parola1)

        testRicercaNGram(set2, parola1, 2)
        testRicercaNGram(set2, parola1, 3)
        testRicercaNGram(set2, parola1, 4)
    for parola2 in parole_assenti:
        print "Ricerca parola :", parola2
        testRicercaEdit(set2, parola2)

        testRicercaNGram(set2, parola2, 2)
        testRicercaNGram(set2, parola2, 3)
        testRicercaNGram(set2, parola2, 4)
