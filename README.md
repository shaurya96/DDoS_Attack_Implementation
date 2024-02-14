#DDoS Attack Implementations of attacking server with TCP SYN/HTTP flood requests

This project explores the practical implementation of Distributed Denial of Service (DDoS) attacks, focusing on three key components: Socket programming (required), TCP SYN flood attack (required), and HTTP flood attack (bonus). The project is instructed in Python, with an option to use C/C++. Ubuntu is recommended for running experiments, but macOS and Windows are also acceptable as long as Python programs and required libraries can be successfully executed.

**Pre-requisites**

Ensure that you have Python3 installed on your system. For information on installing Python, visit [python.org](python.org) or [realpython.com](realpython.com). Additionally, Scapy, a packet crafting library, is utilized in the project. Installation details can be found [here](http://phaethon.github.io/kamene/api/installation.html). The project is composed of 3 tasks, where Task-1 implements basic socket programming, Task-2 implements TCP SYN Flood Attack and Task-3 implements HTTP Flood Attack.

Before executing the tasks locally, first clone the repository locally by using command - git clone https://github.com/shaurya96/DDoS_Attack_Implementation.git

**Task-1 (Socket Programming Implementation)**

In the required Socket Programming task, the project entails the interaction between client and server. The client-side functionality involves the transmission of messages to the server, while the server side is responsible for listening to and receiving these messages. The successful execution of this task requires proficient socket creation, ensuring seamless communication between the client and server, encompassing both message sending and receiving capabilities. The effective implementation of these socket programming examples forms a fundamental aspect of the overall project's objectives.

*Steps to execute the task-*

1. Open Task-1 folder.
2. Run main_server.py by opening terminal in ../../DDoS_Attack_Implementation/Task-1 and typing command - python3 main_server.py
3. Run main.py by opening terminal in ../../DDoS_Attack_Implementation/Task-1 and typing command - python3 main.py

**Task-2 (TCP SYN Flood Attack Implementation)**

The TCP SYN Flood Attack implementation involves several key components. Firstly, Scapy is employed for SYN packet creation, leveraging its capabilities in crafting packets for the attack. To introduce randomness and obfuscation, the implementation utilizes Python's random module for generating random IP addresses and port numbers. Scalability is achieved through the implementation of an infinite loop, continuously generating SYN packets to overwhelm the target server. The monitoring and analysis of these packets are conducted using Wireshark, providing valuable insights into the attack's impact on the network. Emphasis is placed on timer accuracy, highlighting the crucial role of precise timing for the effectiveness of the SYN flood attack. The entire implementation is executed on an Ubuntu (Version – 22.04.3) Virtual Machine, equipped with 4 GB RAM and 2 CPUs, ensuring a controlled and standardized environment for consistent experimentation and assessment of the attack's performance.

*Steps to execute the task-*

1. Open Task-2 folder.
2. Run main_server_1.py by opening terminal in ../../DDoS_Attack_Implementation/Task-2 and typing command - python3 main_server_1.py
3. Run main_1.py by opening terminal in ../../DDoS_Attack_Implementation/Task-2 and typing command - sudo python3 main_1.py

**Task-3 (HTTP Flood Attack Implementation)**

The HTTP Flood Attack implementation involves various critical elements to simulate a scenario with multiple clients. Leveraging Python's multi-threading capabilities, the project creates multiple threads to mimic distinct clients participating in the attack. The crafting of HTTP packets incorporates the generation of random URL paths, adding complexity to the attack. Scalability is achieved through the use of loops, ensuring the creation of the specified number of threads to enhance the attack's reach. Wireshark is employed to monitor and track the generated packets, providing valuable insights into the attack's progress and its impact on the target server. The implementation places significant emphasis on timer accuracy, underscoring the importance of precise timing for the successful execution of the HTTP flood attack. The entire project is executed on an Ubuntu (Version – 22.04.3) Virtual Machine, equipped with 4 GB RAM and 2 CPUs, providing a consistent and controlled environment for the experimentation and evaluation of the attack's effectiveness. 

*Steps to execute the task-*

1. Open Task-3 folder.
2. Run main_server_2.py by opening terminal in ../../DDoS_Attack_Implementation/Task-3 and typing command - python3 main_server_2.py
3. Run main_2.py by opening terminal in ../../DDoS_Attack_Implementation/Task-3 and typing command - sudo python3 main_2.py    
