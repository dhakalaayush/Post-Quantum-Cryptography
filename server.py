import socket
import oqs

# Initialize the PQC algorithm
kem = oqs.KeyEncapsulation("ML-KEM-768")

# Server generates its keypair
print("Generating ML-KEM-768 Keypair...")
public_key = kem.generate_keypair()

# Setup Network Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 65432)) # Listening on loopback port 65432
server_socket.listen(1)

print("Server listening on 127.0.0.1:65432")
conn, addr = server_socket.accept()
print(f"Client connected from {addr}")

# Send the Public Key over the network
print(f"Sending Public Key ({len(public_key)} bytes) over TCP...")
conn.sendall(public_key)

# Wait for the Client to reply with the Ciphertext
print("Waiting for Client Ciphertext...")
ciphertext = conn.recv(2048) # Buffer size large enough for the 1088 byte ciphertext
print(f"Received Ciphertext ({len(ciphertext)} bytes).")

# Decapsulate to get the shared secret
shared_secret = kem.decap_secret(ciphertext)
print("\nSecret decapsulated. Ready for AES-256 data transmission.")

conn.close()
server_socket.close()
kem.free()
