import socket
import oqs

# Setup Network Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to Server at 127.0.0.1:65432...")
client_socket.connect(('127.0.0.1', 65432))

# Receive the massive Public Key from the server
print("Waiting for Server Public Key...")
public_key = client_socket.recv(2048)
print(f"Received Public Key ({len(public_key)} bytes).")

# Client encapsulates the shared secret
kem = oqs.KeyEncapsulation("ML-KEM-768")
ciphertext, shared_secret = kem.encap_secret(public_key)

# Send the locked Ciphertext back over the network
print(f"Sending Ciphertext ({len(ciphertext)} bytes) over TCP...")
client_socket.sendall(ciphertext)

print("\nSecret encapsulated and sent. Ready for AES-256 data transmission.")

client_socket.close()
kem.free()
