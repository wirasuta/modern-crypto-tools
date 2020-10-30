from modern_crypto.rsa import *
import time

if __name__ == "__main__":
    text = b'hilmi naufal yafie do testing! the output of decryption should be the same as this message'
    print(text)
    print(len(text))

    start = time.time()   
    public_key, private_key = generate_rsa_key()
    end = time.time()
    print('generate key time : %f s' % (end-start))

    # print('pow(pow(10,e,n),d,n) : ',pow(pow(100,public_key[0],public_key[1]),private_key[0],private_key[1]))
    # print(pow(100,public_key[0]) < public_key[1])
    start = time.time()
    ciphertext = encrypt(text, public_key)
    end = time.time()
    print('encryption time : %f s' % (end-start))
    print(ciphertext)
    print(len(ciphertext))

    start = time.time()
    plaintext = decrypt(ciphertext, private_key)
    end = time.time()
    print('decryption time : %f s' % (end-start))
    print(plaintext)
    print(len(plaintext))