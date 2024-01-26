```markdown
# TCP Data Flow Exploration

This repository provides a simple example of TCP data flow exploration using Python. It includes a basic TCP server (`server.py`) and client (`client.py`) script, showcasing the three-way handshake, data transfer, and connection closing phases.
```


## Setup

To explore the TCP data flow, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/byteshiva/tcp-data-flow-exploration.git
   cd tcp-data-flow-exploration
   ```

2. Run the server in one terminal:
   ```bash
   nix develop
   python server.py
   ```

3. Open another terminal and run the client:
   ```bash
   nix develop
   python client.py
   ```

4. In a new terminal, open Wireshark to capture traffic on localhost:
   ```bash
   nix develop
   pkexe wireshark
   ```
   In Wireshark, select the appropriate network interface (e.g., `lo` for localhost) and start capturing.

## Observing TCP Data Flow

Once the server and client are running, you can observe the TCP data flow in the Wireshark window. Explore the packets exchanged during the three-way handshake, data transfer, and connection closing phases.

Feel free to analyze and modify the scripts to further understand the intricacies of TCP communication.

Happy exploring!
```

This README.md provides instructions for setting up and exploring the TCP data flow using the provided Python scripts and Wireshark.
