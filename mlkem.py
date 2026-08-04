import oqs

# Initialize the NIST-approved Post-Quantum algorithm
# ML-KEM (FIPS 203) is the primary algorithm for general encryption and secure key exchange
kem = oqs.KeyEncapsulation("ML-KEM-768")

print("1. Key Generation")
public_key = kem.generate_keypair()
print(f"ML-KEM-768 Public Key Size: {len(public_key)} bytes")

print("\n 2. Encapsulation (Client Side)")

# The client uses the public key to generate and encapsulate a shared secret
ciphertext, shared_secret_client = kem.encap_secret(public_key)
print(f"Ciphertext Size: {len(ciphertext)} bytes")

print("\n 3. Decapsulation (Server Side)")

# The server uses its private key to reveal the shared secret
shared_secret_server = kem.decap_secret(ciphertext)

# Verify that both sides arrived at the exact same secret
if shared_secret_client == shared_secret_server:
    print("\n SUCCESS: Both parties share the same quantum-safe secret!")
    print("The connection is now ready for standard AES encryption.")
else:
    print("\n ERROR: Key mismatch.")

# Clean up memory
kem.free()
