from modern_crypto.elgamal import *

if __name__ == "__main__":
    text = b'i putu gede wirasuta'
    print(text)
    print(len(text))

    public_key, private_key = generate_eg_keypair()
    ciphertext = encrypt(text, public_key)
    print(ciphertext)
    print(len(ciphertext))

    plaintext = decrypt(ciphertext, private_key)
    print(plaintext)
    print(len(plaintext))