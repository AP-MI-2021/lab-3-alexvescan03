#proprietatea 2
def get_longest_all_primes(l):
    '''
    determina daca o lista este formata doar din nr palindroame
    :param l: lista de nr intregi
    :return: true daca are doar elem palindroame sau false in caz contrar
    '''
    for x in l:
        if x<2:
            print("Nu")
        else:
            for i in range(2,x//2 +1):
                if x % i == 0:
                    return False
        return True
def test_get_longest_all_primes():
    assert get_longest_all_primes([]) is True
    assert get_longest_all_primes([121,1000,333]) is False
    assert get_longest_all_primes([3,5,7]) is True
    assert get_longest_all_primes([121,333,444,23]) is False
def subsecventaMaxPrime(l):
    '''
    determina cea mai lunga subsecventa de nr palindroame
    :param l: lista de nr intregi
    :return: cea mai lunga subsecventa de nr palindroame
    '''
    subsecventaMax=[]
    for i in range(len(l)): # primul pas: i=0 j=1 si se verifica lista de la 0 la 1
        for j in range (i,len(l)): #verifica daca acea lista are toate elementele prime
            if get_longest_all_primes(l[i:j+1]) and len(l[i:j+1]) > len(subsecventaMax):
                subsecventaMax = l[i:j+1] # daca se gaseste o subsecventa cu toate nr prime se salveaza aici
    return subsecventaMax
def TestSubsecventaMaxPrime():
    assert subsecventaMaxPrime([]) == []
    assert subsecventaMaxPrime([11,13,333]) == [11,13]
    assert subsecventaMaxPrime([14,12,13,16,17,23]) == [17,23]
def printMenu():
    print("1.Citire date")
    print("2.Determinare cea mai lungă subsecvență cu proprietatea ")
    print("3.Iesire")
def citireDate():
    l = []
    listAsString = input("Dati lista")
    numbersAsString = listAsString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l
def main():
    TestSubsecventaMaxPrime()
    test_get_longest_all_primes()
    l=[]
    while True:
        printMenu()
        optiune = input("dati opriunea:")
        if optiune == "1":
            l=citireDate()
        elif optiune == "2":
            print(subsecventaMaxPrime(l))
        elif optiune == "3":
            break
        else:
            print("Optiune gresita")
main()