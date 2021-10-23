def  get_longest_all_primes(l):
    '''
    determina daca toate nr. dintr-o lista sunt prime
    :param l: lista de nr. intregi
    :return: True, daca toate nr. din l sunt prime sau False, in caz contrar
    '''
    for x in l:
        if x < 2:
            return False
        else:
            for i in range(2,x//2+1):
                if x % i == 0:
                    return False
    return True
def test_get_longest_all_primies():
    assert  get_longest_all_primes([]) is True
    assert get_longest_all_primes([1,2,3,3]) is False
    assert get_longest_all_primes([2,3,3]) is True
def SubsecventaMaxElementePrime(l):
    '''
    determina cea mai lunga subsecventa de nr. divizibile cu 10
    :param l: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. divizibile cu 10 din l
    '''
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if get_longest_all_primes(l[i:j+1]) and len(l[i:j+1]) > len(subsecventaMax):
                subsecventaMax = l[i:j+1]
    return subsecventaMax
def testSubsecventaMaxElementePrime():
    assert SubsecventaMaxElementePrime([]) == []
    assert SubsecventaMaxElementePalindroame([1,2,3,3]) == [2,3,3]
def get_longest_all_palindromes(l):
    '''
    determina daca toate nr. dintr-o lista sunt palindroame
    :param l: lista de nr. intregi
    :return: True, daca toate nr. din l sunt palindroame sau False, in caz contrar
    '''
    for x in l:
        cx=x
        inv = 0
        while cx!=0:
            inv = inv * 10 + cx %10
            cx = cx// 10
        if inv != x:
            return False
    return True

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([1, 2, 3]) is True
    assert get_longest_all_palindromes([13, 11, 10]) is False
    assert get_longest_all_palindromes([33, 11, 21, 55, 12]) is False
    assert get_longest_all_palindromes([]) is True

def SubsecventaMaxElementePalindroame(l):
    '''
    determina cea mai lunga subsecventa de nr. palindroame
    :param l: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. palindroame din l
    '''
    SubsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if get_longest_all_palindromes(l[i:j+1]) and len(l[i:j+1]) > len(SubsecventaMax):
                SubsecventaMax = l[i:j+1]
    return SubsecventaMax

def testSubsecventaMaxElementePalindroame():
    assert SubsecventaMaxElementePalindroame([11,12,13,15]) == [11]
    assert SubsecventaMaxElementePalindroame([11,33,22,12,13]) == [11,33,22]
    assert SubsecventaMaxElementePalindroame([11,12,33,22,45]) == [33,22]
    assert SubsecventaMaxElementePalindroame([]) == []

def printMenu():
    print("1. Citire lista")
    print("2. Afisare cea mai lunga subsecventa de palindroame")
    print("3. Afisare cea mai lunga subsecventa de numere cu cifre prime")
    print("4.Afisare cea mai lunga subsecventa de numere prime")
    print("5. Iesire")

def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numberAssString=givenString.split(",")
    for x in numberAssString:
        l.append(int(x))
    return l

def isPrime(x):
    if x<2:
        return False
    for i in range(2,x//2 +1):
        if x%i==0:
            return False
    return True
def get_longest_prime_digits(l):
    for n in l:
        while n!=0:
            cif=n%10
            n = n // 10
            if isPrime(cif) == False:
                return False
    return True

def test_get_longest_prime_digits():
    assert get_longest_prime_digits([2,3,11]) is False
    assert get_longest_prime_digits([1,11,13]) is False
    assert get_longest_prime_digits([121,33,74]) is False
    assert get_longest_prime_digits([3,5,7,]) is True
def SubsecventaMaxElementeCifrePrime(l):
    '''
    determina cea mai lunga subsecventa de nr. cu cifre prime
    :param l: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. cu cifre prime din l
    '''
    SubsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if get_longest_prime_digits(l[i:j + 1]) and len(l[i:j + 1]) > len(SubsecventaMax):
                SubsecventaMax = l[i:j + 1]
    return SubsecventaMax
def testSubsecventaMaxElementeCifrePrime():
    assert SubsecventaMaxElementeCifrePrime([33,35,75]) == [33,35,75]
    assert SubsecventaMaxElementeCifrePrime([10,12,8]) == []
    assert SubsecventaMaxElementeCifrePrime([]) == []
    assert SubsecventaMaxElementeCifrePrime([10,11,55,35]) == [55,35]
def main():
    test_get_longest_all_palindromes()
    testSubsecventaMaxElementePalindroame()
    test_get_longest_prime_digits()
    testSubsecventaMaxElementeCifrePrime()
    l = []
    while True:
        printMenu()
        optiune = int(input("Da-ti optiunea: "))
        if optiune == 1:
            l=citireLista()
        elif optiune == 2:
            print(SubsecventaMaxElementePalindroame(l))
        elif optiune == 3:
            print(SubsecventaMaxElementeCifrePrime(l))
        elif optiune == 4:
            print(SubsecventaMaxElementePrime(l))
        elif optiune == 5:
            break
        else:
            print("Optiune gresita, reincearca")
main()