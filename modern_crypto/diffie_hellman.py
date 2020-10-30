from Crypto.Util import number
from random import randint
from typing import Tuple

KEY_SIZE = 1024

def generate_shared_parameter() -> Tuple[int,int]:
    """
    return prime number g and n where g < n
    (g,n)
    """
    a = number.getPrime(KEY_SIZE)
    b = number.getPrime(KEY_SIZE)

    while(a==b):
        b = number.getPrime(KEY_SIZE)
    
    if (a>b):
        return b, a
    
    return a, b

def generate_secret_pow() -> int:
    """
    return big random number
    the number should be kept as secret by the owner
    """
    return randint(1,2**KEY_SIZE-1)

def shared_op(g:int, n:int, secret_pow:int) -> int:
    """
    return X where X === g**secret_pow (mod n)
    the value of X will be shared to the other party to generate private key
    """
    return pow(g, secret_pow, n)

def generate_private_key(shared_op_result:int, n:int, secret_pow:int) -> int:
    """
    return private key where private_key === other_party_op_result**secret_pow (mod n)
    the value of private key should be the same as the other party
    """
    return pow(shared_op_result, secret_pow, n)
