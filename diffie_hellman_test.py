from modern_crypto.diffie_hellman import *
# import time

g, n = generate_shared_parameter()
print("Hilmi and Tude decide to use \ng = %d \nand \nn = %d" % (g,n))
print("\n")

hilmi_secret_pow = generate_secret_pow()
tude_secret_pow = generate_secret_pow()
print("Hilmi's secret power x : %d" % hilmi_secret_pow)
print("Tude's secret power y  : %d" % tude_secret_pow)
print("\n")

hilmi_operation = shared_op(g, n, hilmi_secret_pow)
tude_operation = shared_op(g, n, tude_secret_pow)
print("Hilmi shared result X : %d" % hilmi_operation)
print("Tude shared result Y  : %d" % tude_operation)
print("\n")

hilmi_private_key = generate_private_key(tude_operation, n, hilmi_secret_pow)
tude_private_key = generate_private_key(hilmi_operation, n, tude_secret_pow)
print("Hilmi private key : %d" % hilmi_private_key)
print("Tude private key  : %d" % tude_private_key)
