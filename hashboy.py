import hashlib
from datetime import datetime
import time

# This is a basic password/hash cracker made for educational purposes. 
# Version 1.0

def intro(): # This is just for aesthetic 

    print('{:^80}'.format('*======================*'))
    print('{:^80}'.format('|        Hashboy       |'))
    print('{:^80}'.format('|         v1.0         |'))
    print('{:^80}'.format('*======================*'))
    print('\n{:^80}'.format('Created By Valentin Cain'))
    print('{:^80}'.format('2022'))

    time.sleep(1)
    print('\n')
    print('\n')
    print('\n')
  

intro()



while True: # To load wordlist, need to work on this to make sure more file types can be read
    try:
        list = input('Enter Wordlist Path: ')
        with open (list, 'r') as rlist:
            olist = rlist.read()
            rlist.close()
            break
    except:
        print('Error: Cannot Load File')
        continue        



while True: 

    input_val = ('1','2','3','4','5','6','7','8','9') # to restrict any input other than what is available in hash_type
    hash_type = input('Select Algorithm:\n 1) MD4\n 2) MD5\n 3) SHA1\n 4) SHA224\n 5) SHA256\n 6) SHA384\n 7) SHA512\n 8) WHIRLPOOL\n 9) RIPEMD160\n \nSelection:')
    
    if hash_type not in input_val:
        print('\nError: Invalid Entry\n')
    else:
        break
    



hinput = input('Enter Hash: ') # input for hash


start=datetime.now() # to give a final count of the search time, look below for where it is called. This is the beginning of the timer.


def md5_hash():
    try:

        for word in olist.split():
            digest = hashlib.md5(word.encode()).hexdigest()
            

            if digest == hinput:
                flag=1
                print('Password: ' + word)
                if flag==1:
                    break
    except:
        pass

def sha256_hash():
    try:

        for word in olist.split():
            digest = hashlib.sha256(word.encode()).hexdigest()
            

            if digest == hinput:
                flag=1
                print('Password: ' + word)
                if flag==1:
                    break
    except:
        pass

def sha1_hash():
    try:

        for word in olist.split():
            digest = hashlib.sha1(word.encode()).hexdigest()
            

            if digest == hinput:
                flag=1
                print('Password: ' + word)
                if flag==1:
                    break
    except:
        pass
    
def sha224_hash():
    try:

        for word in olist.split():
            digest = hashlib.sha224(word.encode()).hexdigest()
            

            if digest == hinput:
                flag=1
                print('Password: ' + word)
                if flag==1:
                    break
    except:
        pass

def sha384_hash():
    try:

        for word in olist.split():
            digest = hashlib.sha384(word.encode()).hexdigest()
            

            if digest == hinput:
                flag=1
                print('Password: ' + word)
                if flag==1:
                    break
    except:
        pass

def sha512_hash():
    try:

        for word in olist.split():
            digest = hashlib.sha512(word.encode()).hexdigest()
            

            if digest == hinput:
                flag=1
                print('Password: ' + word)
                if flag==1:
                    break
    except:
        pass

def ripe160_hash():
    try:

        for word in olist.split():
            digest = hashlib.new('ripemd160', word.encode()).hexdigest()
            
            
            

            if digest == hinput:
                flag=1
                print('Password: ' + word)
                if flag==1:
                    break
    except:
        pass

def whirl_hash():
    try:

        for word in olist.split():
            digest = hashlib.new('whirlpool',(word.encode())).hexdigest()
            

            if digest == hinput:
                flag=1
                print('Password: ' + word)
                if flag==1:
                    break
    except:
        pass

def md4_hash():
    try:

        for word in olist.split():
            digest = hashlib.new('md4', (word.encode())).hexdigest()
            
            

            if digest == hinput:
                flag=1
                print('Password: ' + word)
                if flag==1:
                    break
    except:
        pass

if hash_type == '1':
    md4_hash()
if hash_type == '2':
    md5_hash()
if hash_type == '3':
    sha1_hash()
if hash_type == '4':
    sha224_hash()
if hash_type == '5':
    sha256_hash() 
if hash_type == '6':
    sha384_hash()
if hash_type == '7':
    sha512_hash()   
if hash_type == '8':
    whirl_hash()
if hash_type == '9':
    ripe160_hash()     

print("Search finished in", datetime.now()-start)


    

