# Post Quantum Cryptography

This project demonstrates a Post-Quantum Key Encapsulation Mechanism (KEM) using the NIST-approved ML-KEM algorithm. It utilizes the Open Quantum Safe (`liboqs`) C library and its Python wrapper to simulate a quantum-safe handshake.

## Requirements

This project requires a Linux environment to compile the underlying C library.

1. Update the package list and install the required compilers, CMake, and Python tools

          sudo apt update
          sudo apt install -y git build-essential cmake libssl-dev python3 python3-pip python3-venv

2. The script relies on (`liboqs`) library which can be cloned from github

          git clone [https://github.com/open-quantum-safe/liboqs.git](https://github.com/open-quantum-safe/liboqs.git)
          cd liboqs

3. Configure the build environment

          mkdir build && cd build
          cmake -DOQS_USE_OPENSSL=OFF ..

4. Compile and install

          make
          sudo make install

5. Set up the python environment: Return to the root folder to execute these commands

          python3 -m venv mlkem_env
          source mlkem_env/bin/activate

5. Install the python wrapper

          pip install liboqs-python

6. Run the program

          python3 client.py
          python3 server.py
