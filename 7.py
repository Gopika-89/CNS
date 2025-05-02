import random

def generate_prime():
    return 19
def generate_primitive_root(p):
    return 41 

def generate_private_key():
    return random.randint(1, 100)  
def compute_public_key(g, private_key, p):
    return pow(g, private_key, p)

def compute_shared_secret(public_key, private_key, p):
    return pow(public_key, private_key, p)

p = generate_prime()  
g = generate_primitive_root(p)  

print(f"Publicly shared values: p={p}, g={g}")

private_key_A = generate_private_key()
private_key_B = generate_private_key()

public_key_A = compute_public_key(g, private_key_A, p)
public_key_B = compute_public_key(g, private_key_B, p)

print(f"User A Public Key: {public_key_A}")
print(f"User B Public Key: {public_key_B}")

shared_secret_A = compute_shared_secret(public_key_B, private_key_A, p)
shared_secret_B = compute_shared_secret(public_key_A, private_key_B, p)

print(f"Shared Secret (computed by A): {shared_secret_A}")
print(f"Shared Secret (computed by B): {shared_secret_B}")

assert shared_secret_A == shared_secret_B, "Key exchange failed!"

