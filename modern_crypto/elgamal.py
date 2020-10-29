from Crypto.Util import number
from random import randint
from typing import Tuple
from modern_crypto.common import *

KEY_SIZE = 1024

def generate_eg_keypair() -> Tuple[Tuple[int, int, int], Tuple[int, int]]:
    """
    returns public and private key
    """
    p = number.getPrime(KEY_SIZE)
    g = randint(1, p-1)
    x = randint(1, p-2)
    y = pow(g, x, p)

    return (y, g, p), (x, p)

def encrypt(plaintext: bytes, public_key: Tuple[int, int, int]) -> bytes:
    """
    returns ciphertext with double the size of plaintext
    ciphertext is arranged in a_0, b_0, a_1, b_1, ..., a_n, b_n
    where a_x and b_x are the a and b component of block x respectively
    """
    y = public_key[0]
    g = public_key[1]
    p = public_key[2]
    k = randint(1, p-2)
    block_size = KEY_SIZE // 8
    plaintext = pad(plaintext, block_size)
    pt_blocks = msg_to_hex_of_n_bytes(plaintext, block_size)

    ciphertext = []
    for block in pt_blocks:
        m = int(block.decode(), 16)

        a = pow(g, k, p)
        b = (pow(y, k, p) * (m % p)) % p

        ciphertext.append(bytes(f'{a:0256x}', 'ISO-8859-1'))
        ciphertext.append(bytes(f'{b:0256x}', 'ISO-8859-1'))
    ciphertext = hex_of_n_bytes_to_msg(ciphertext)

    return ciphertext

def decrypt(ciphertext: bytes, private_key: Tuple[int, int]) -> bytes:
    """
    returns plaintext with half the size of ciphertext
    ciphertext is arranged in a_0, b_0, a_1, b_1, ..., a_n, b_n
    where a_x and b_x are the a and b component of block x respectively
    """
    x = private_key[0]
    p = private_key[1]
    block_size = KEY_SIZE // 8
    ct_blocks = msg_to_hex_of_n_bytes(ciphertext, block_size)

    plaintext = []
    for i in range(0, len(ct_blocks), 2):
        a = int(ct_blocks[i].decode(), 16)
        b = int(ct_blocks[i+1].decode(), 16)

        a_inv = pow(a, p-1-x, p)
        m = (b * a_inv) % p

        plaintext.append(bytes(f'{m:0256x}', 'ISO-8859-1'))
    plaintext = hex_of_n_bytes_to_msg(plaintext)
    plaintext = unpad(plaintext, block_size)

    return plaintext

def save_public_key(filename: str, public_key: Tuple[int, int, int]):
    with open(filename, 'w+') as f:
        f.write('\n'.join([
            hex(public_key[0])[2:],
            hex(public_key[1])[2:],
            hex(public_key[2])[2:]
        ]))

def save_private_key(filename: str, private_key: Tuple[int, int]):
    with open(filename, 'w+') as f:
        f.write('\n'.join([
            hex(private_key[0])[2:],
            hex(private_key[1])[2:]
        ]))

def load_public_key(filename: str) -> Tuple[int, int, int]:
    with open(filename, 'r') as f:
        content = f.readlines()
    return (int(content[0], 16), int(content[1], 16), int(content[2], 16))

def load_private_key(filename: str) -> Tuple[int, int]:
    with open(filename, 'r') as f:
        content = f.readlines()
    return (int(content[0], 16), int(content[1], 16), )