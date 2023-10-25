def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def encode(password):
    lista = []
    for i in password:
        num = int(i) + 3
        lista.append(num)

    stringa = ''
    for i in range(0, len(lista)):
        stringa += str(lista[i])

    return stringa

def main():
    x = 1
    while x == 1:
        menu()
        print()
        user_input = int(input('Please enter an option:'))
        if user_input == 1:
            passw = input('Please enter the password to encode:')
            encoded_passw = encode(passw)
            print('Your password has been encoded and stored!')
        if user_input == 2:
            print('eep')



if __name__ == '__main__':
    main()
