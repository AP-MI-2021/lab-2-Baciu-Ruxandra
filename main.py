
def get_symbol(str):
    if str=="0000":
        return '0'
    if str=="0001":
        return '1'
    if str=="0010":
        return '2'
    if str=="0011":
        return '3'
    if str=="0100":
        return '4'
    if str=="0101":
        return '5'
    if str=="0110":
        return '6'
    if str=="0111":
        return '7'
    if str=="1000":
        return '8'
    if str=="1001":
        return '9'
    if str=="1010":
        return 'A'
    if str=="0011":
        return 'B'
    if str=="1100":
        return 'C'
    if str=="1101":
        return 'D'
    if str=="1110":
        return 'E'
    if str=="1111":
        return 'F'


def get_base_16_from_2(n):
    newstr=""
    if len(n)/4!=float(len(n)//4):
        while len(n)/4!=float(len(n)//4):
            n='0'+n
    while len(n)!=0:
        temp=get_symbol(n[-4:])
        newstr=str(temp)+newstr
        n=n[:-4]
    return newstr


def test_get_base_16_from_2():
    assert get_base_16_from_2("100010011101")=="89D"
    assert get_base_16_from_2("11011110111")=="6F7"
test_get_base_16_from_2()



def get_n_choose_k(n,k):
    x = 1
    for i in range(n - k + 1, n + 1):
        x *= i
    y = 1
    for i in range(2, k + 1):
        y *= i
    return x / y

def test_get_n_choose_k():
    assert get_n_choose_k(123,123)==1
    assert get_n_choose_k(12,5)==792
    assert get_n_choose_k(10,1)==10
test_get_n_choose_k()


def is_prime(n):
  if n==2:
     return True
  if n<2:
     return False
  if n%2==0:
      return False
  for i in range(3,n//2+1,2):
      if n%i==0:
         return False
  return True


def get_largest_prime_below(n):
    if n==2:
        return "Nu exista un numar prim mai mic decat numarul introdus!"
    if n<2:
        return "Introduceti o valoare mai mare decat 2!"
    n=n-1
    while is_prime(n) is False:
        n-=1
    return n

def test_get_largest_prime_below():
    assert get_largest_prime_below(14)==13
    assert get_largest_prime_below(21)==19
    assert get_largest_prime_below(3)==2
test_get_largest_prime_below()


def print_meniu():
    print("1. Transformă un număr dat din baza 2 în baza 16. ")
    print("2. Calculează combinări de n luate câte k")
    print("3. Găsește ultimul număr prim mai mic decât un număr dat.")
    print("x. Iesire")

def main():

  while True:
    print_meniu()
    option = input('Alegeti o optiune: ')
    if option == '1':
        n=str(input('Introduceti numaul in baza 2 pe care doriti sa il transformati in baza 16: ') )
        print('Numarul dat se scrie in baza 16: ',get_base_16_from_2(n),'\n')
    elif option == '2':
        n=int(input('Combinari de: '))
        k=int(input('luate cate : '))
        print('Rezultatul  este: ')
        print(get_n_choose_k(n,k))
    elif option=='3':
        n=int(input("Introduceti numarul: "))
        print("Raspuns: ")
        print(get_largest_prime_below(n))
    elif option == 'x':
        break
    else:
        print('Optiune invalida, reincearca!')




if __name__ == '__main__':
  main()
