from binascii import hexlify, unhexlify
from typing import List

def all_eq(a: List) -> bool:
    return all(x == a[0] for x in a)

def pad(msg: bytes, block_size: int) -> bytes:
    msg_len = len(msg)
    padding_size = (block_size * (msg_len // block_size + 1)) - msg_len
    temp = [b for b in msg] + [padding_size - 1 for _ in range(padding_size)]
    return bytes(temp)

def unpad(msg: bytes, block_size: int) -> bytes:
    last_byte = msg[-1]
    if last_byte >= 0 and last_byte <= (block_size - 2) and all_eq(msg[-1-last_byte:]):
        msg = msg[:-1-last_byte]
    return msg

def msg_to_hex_of_n_bytes(msg: bytes, n: int) -> List[bytes]:
    msg_blocks = [msg[i:i+n] for i in range(0, len(msg), n)]
    msg_blocks = [hexlify(msg) for msg in msg_blocks]
    return msg_blocks

def hex_of_n_bytes_to_msg(msg_blocks: List[bytes]) -> bytes:
    msg_blocks = [unhexlify(block) for block in msg_blocks]
    msg = b''.join(msg_blocks)
    return msg