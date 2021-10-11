#proprietatea 1 (cu numerele palindroame)
def get_longest_all_palindromes(l):
    '''
    determina daca o lista este formata doar din nr palindroame
    :param l: lista de nr intregi
    :return: true daca are doar elem palindroame sau false in caz contrar
    '''
    for x in l:
        cx = x
        inv = 0
        while cx > 0:
            inv = inv*10 + cx % 10
            cx = cx // 10
        if inv == x:
            return False
    return True
def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([]) is True
    assert get_longest_all_palindromes([121,1000,333]) is False
    assert get_longest_all_palindromes([121,333,444]) is True
    assert get_longest_all_palindromes([121,333,444,21]) is False
def subsecventaMaxPalindrome(l):
    '''
    determina cea mai lunga subsecventa de nr palindroame
    :param l: lista de nr intregi
    :return: cea mai lunga subsecventa de nr palindroame
    '''
    subsecventaMax=[]
    for i in range(len(l)): # primul pas: i=0 j=1 si se verifica lista de la 0 la 1
        for j in range (i,len(l)): #verifica daca acea lista are toate elementele palindroame
            if get_longest_all_palindromes(l[i:j+1]) and len(l[i:j+1]) > len(subsecventaMax):
                subsecventaMax = l[i:j+1] # daca se gaseste o subsecventa cu toate nr palindroame se salveaza aici
    return subsecventaMax
def TestSubsecventaMaxPalindrome():
    assert subsecventaMaxPalindrome([]) == []
    assert subsecventaMaxPalindrome([100,121,333]) == [121,333]
    assert subsecventaMaxPalindrome([121,100,333,444]) == [333,444]

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([]) is True
    assert get_longest_all_palindromes([121,100]) is False
    assert get_longest_all_palindromes([121,222,333]) is True
    assert get_longest_all_palindromes([10,11]) is False

def printMenu():
    print("1.Citire date")
    print("2.Determinare cea mai lungă subsecvență cu proprietatea 1.")
    print("3.Determinare cea mai lunga subsecventa cu proprietatea 2.")
    print("3.Iesire")
def citireDate():
    l = []
    listAsString = input("Dati lista")
    numbersAsString = listAsString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l
def main():
    TestSubsecventaMaxPalindrome()
    test_get_longest_all_palindromes()
    testSubsecventaMax2()
    test_get_longest_arithmetic_progression()
    l=[]
    while True:
        printMenu()
        optiune = input("dati opriunea:")
        if optiune == "1":
            l=citireDate()
        elif optiune == "2":
            print(subsecventaMaxPalindrome(l))
        elif optiune == "3":
            print(subsecventaMaxPare(l))
        elif optiune == "4":
            break
        else:
            print("Optiune gresita")
main()
#proprietatea 2 (cu numerele pare)
def get_longest_arithmetic_progression(l):
    '''
    determina daca o lista este formata doar din elemente pare
    :param l: lista de nr intregi
    :return:  true daca are doar elemente pare,false in celalalt caz
    '''
    for x in l:
        if x % 2 == 0:
            return True
        return False
def test_get_longest_arithmetic_progression():
    assert get_longest_arithmetic_progression([]) is True
    assert get_longest_arithmetic_progression([12,14,16]) is True
    assert get_longest_arithmetic_progression([11,12,15]) is False
    assert  get_longest_arithmetic_progression([11,13,15,17] is False)
def subsecventaMaxPare():
    subsecventaMax2 == []
    for i in range(len(l)): # primul pas: i=0 j=1 si se verifica lista de la 0 la 1
        for j in range (i,len(l)): #verifica daca acea lista are toate elementele palindroame
            if get_longest_arithmetic_progression(l[i:j+1]) and len(l[i:j+1]) > len(subsecventaMax2):
                subsecventaMax2 = l[i:j+1] # daca se gaseste o subsecventa cu toate nr palindroame se salveaza aici
    return subsecventaMax2
def testSubsecventaMax2
    assert  subsecventaMaxPare([12,14,16]) == [12,14,16]
    assert  subsecventaMaxPare([8,11,14,18]) == [14,18]
    assert  subsecventaMaxPare([]) == []