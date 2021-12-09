from random import randint
from os import system
from os import path
from miller_rabin import millerRabin, PowerMod
import base64

def input_directory(use = 'take info'):
    while True:
        directory = input('Input DIRECTORY: ')

        # create directory
        if not path.isdir(directory):
            if use == 'gen key':
                command = 'mkdir '+ directory 
                system(command)
                break
            else:
                print('error: file not found\n')
        else:
            break
            
    return directory


def take_message(type):
    while True:
        while True: 
            try:
                file_name = input('Input {} file (.txt): '. format(type))
                
                if file_name.split('.')[1] == 'txt':
                    break 
                else:
                    print('error: file not found')            
            except:
                print("error: invalid input (must contain '.txt')")

        if path.isfile(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                message = file.read()
                return message
        else: 
            print('error: file not found')    


def take_key(directory, type):   
    # while True:
    if type == "PUBLIC KEY":
        file_name = 'el_pub.txt' 
    else:
        file_name = 'el.txt' 

    if path.isfile(directory + '/' + file_name):
        with open(directory + '/' + file_name, 'r', encoding='utf-8') as file:
            key = file.readline().split()
            if file_name == 'el_pub.txt':
                alpha = int(key[0])
                beta = int(key[1])
                p = int(key[2])
                
                return alpha, beta, p
            else:
                a = int(key[0])
                p = int(key[1])
                
                return a, p
    else:
        print('error: file not found\n')


def generate_prime(exp_min, exp_max): #little Fermat
    n = randint(exp_min, exp_max)

    prime = 2**n + 1 

    while not millerRabin(prime):
        prime += 2

    return prime


def generate_key(directory): # generate public/ secrect key
    # pk: alpha, beta, p
    # beta = alpha^a mod p
    # --------------------------
    # sk: a, p

    print('Generating....')
    p = generate_prime(20, 25)

    while True:
        alpha = generate_prime(18, 23)
        if alpha < p:
            break

    # generate private key
    while True:
        a = generate_prime(10, 19)
        if a < alpha:
            break

    beta = PowerMod(alpha, a, p)

    # save public key in "el_pub.txt"
    with open(directory + '/el_pub.txt', 'w', encoding='utf-8') as file:
        file.write('{} {} {}'. format(alpha, beta, p))

    # save secrect key in "rsa.txt"  
    with open(directory + '/el.txt', 'w', encoding='utf-8') as file:
        file.write('{} {}'. format(a, p))

    print('\n > Generate key done!! <')



def encryption(plaintext, alpha, beta, p):
    # convert plaintext into ascii
    k = randint(1, p)
    C1 = []
    C2 = []

    for message_text in plaintext:
        for i in message_text:
            M = ord(i)
            c1 = PowerMod(alpha, k, p)
            c2 = ((M % p) * PowerMod(beta, k, p)) % p
            
            C1.append(str(c1))
            C2.append(str(c2))
    
    strC1 = " ".join(C1)
    strC2 = " ".join(C2)

    message = strC1 + '/' + strC2
    message_byte = message.encode('ascii')
    ciphertext = str(base64.b64encode(message_byte)).strip("b'")

    # write encrypt message into file 
    with open('encrypted.txt', 'w', encoding='utf-8') as encrypt_file:
        encrypt_file.write(ciphertext)

    print('\n   > Encrypt done!! <')



def decryption(ciphertext, a, p):
    plaintext = ''
    ciphertext = ciphertext.encode()
    message_bytes = base64.b64decode(ciphertext)
    message = message_bytes.decode('ascii')

    flag = True

    C = message.split('/')
    C1 = C[0].split(' ')
    C2 = C[1].split(' ')

    for i in range(len(C1)):
        c1 = int(C1[i])
        c2 = int(C2[i])
        M = ((c2 % p) * PowerMod(c1, p-1-a, p)) % p
        try:
            plaintext += chr(M)
        except:
            with open('decrypted.txt', 'w', encoding='utf-8') as decrypt_file:
                decrypt_file.write('NULL')
            print('\n    > Can not decrypted - due KEY !! <')
            flag = False
            break
        
    if flag == True:
        # write decrypt message into file 
        with open('decrypted.txt', 'w', encoding='utf-8') as decrypt_file:
            decrypt_file.write(plaintext)
        
        print('\n    > Decrypt done!! <')
    


def menu(os):
    if os == 'window':
        system('cls')
    else:
        system('clear')

    print('====================================================')
    print('==            INTRODUCE TO CRYPTOGRAPHY           ==')
    print('==                   Class: 19MMT                 ==')
    print('==________________________________________________==')
    print('== Name: Nguyen Thanh Quan | Name: Phung Anh Khoa ==')
    print('== Student ID: 19127525    | Student ID: 19127449 ==')
    print('====================================================')
    print('\nGroup exercise -- Main Menu\n')
    print('[1] Generate Elgamal key')
    print('[2] Encrypt plaintext')
    print('[3] Dencrypt ciphertext')
    print('[4] Exit\n')

    while True:
        try: 
            choice = int(input('Choice: '))
        except:
            choice = 5
            print('error: invalid input\n')
        if choice >= 1 and choice <= 4:
            return choice
    

if __name__ == '__main__':
    # get os windown or linux
    error = system('clear')
    if error == 1: 
        os = 'window'
    else:
        os = 'linux'

    while True:
        choice = menu(os)
        print('-----------------------------------')
        # 1: Generate key
        if choice == 1: 
            directory = input_directory('gen key')
            generate_key(directory)
            a = input("Press any key to continue")

        # 2: Encrypt plaintext
        elif choice == 2:
            plaintext = take_message('PLAIN TEXT')
            key_directory = input_directory()
            alpha, beta, p = take_key(key_directory, 'PUBLIC KEY')
            
            encryption(plaintext, alpha, beta, p)
            a = input("Press any key to continue")

        # 3: Decrypt ciphertext
        elif choice == 3:
            ciphertext = take_message('CIPHER TEXT')
            
            key_directory = input_directory()
            a, p = take_key(key_directory, 'SECRECT KEY')
            decryption(ciphertext, a, p)

            a = input("Press any key to continue")
        
        # 4: Exit
        else:
            break
