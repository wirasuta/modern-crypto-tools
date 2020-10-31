from Crypto.Util import number
from random import randint
from math import gcd
from typing import Tuple
from modern_crypto.common import *

KEY_SIZE = 1024
# key size above 16 sometimes give different result from the initial plaintext
# public key range should be wider for bigger key size, but it would effect the private key generator performance

def generate_rsa_key() -> Tuple[Tuple[int,int], Tuple[int,int]]:
    """
    return public and private key for rsa algorithm
    """
    p = number.getPrime(KEY_SIZE)
    q = number.getPrime(KEY_SIZE)
    n = p*q
    euler = (p-1)*(q-1)
    public = 65537
    private = modinv(public, euler)

    return (public, n), (private, n)

def encrypt(plaintext:bytes, public_key: Tuple[int,int]) -> bytes:
    
    key = public_key[0]
    n = public_key[1]

    block_size = KEY_SIZE // 4
    
    plaintext = pad(plaintext, block_size)
    message_block = msg_to_hex_of_n_bytes(plaintext, block_size)
    
    ciphertext = bytearray()
    for block in message_block:
        msg_val = int(block.decode(), 16)
        c = pow(msg_val, key, n)
        ciphertext += c.to_bytes((c.bit_length() + 7) // 8, 'big')

    return bytes(ciphertext)

def decrypt(ciphertext:bytes, private_key: Tuple[int,int]) -> bytes:
    key = private_key[0]
    n = private_key[1]

    block_size = KEY_SIZE // 4
    message_block = msg_to_hex_of_n_bytes(ciphertext, block_size)

    plaintext = bytearray()
    for block in message_block:
        msg_val = int(block.decode(), 16)
        p = pow(msg_val, key, n)
        plaintext += (p.to_bytes((p.bit_length() + 7) // 8, 'big'))
    
    plaintext = bytes(plaintext)
    plaintext = unpad(plaintext, block_size)
    return plaintext

