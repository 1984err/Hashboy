from ast import While
from codecs import utf_16_le_encode, utf_8_encode
import hashlib
from datetime import datetime


list = input('Wordlist Path: ')
#list = 'rockyou2.txt'
with open (list, 'r') as rlist:
    olist = rlist.read()
    rlist.close()



while True:

    input_val = ('1','2','3','4','5','6','7','8','9')
    hash_type = input('Select Algorithm:\n 1) MD4\n 2) MD5\n 3) SHA1\n 4) SHA224\n 5) SHA256\n 6) SHA384\n 7) SHA512\n 8) WHIRLPOOL\n 9) RIPEMD160\n \nSelection:')
    
    if hash_type not in input_val:
        print('\n***Error: Invalid Entry***\n')
    else:
        break
    



hinput = input('Enter Hash: ')


start=datetime.now()


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


    

