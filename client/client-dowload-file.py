#-*- coding: utf-8 -*-

import socket
import tqdm
import os

class Cliente(object):
	filesize = None
	s = socket.socket()

	def __init__(self):
		self.SEPARATOR = "<SEPARATOR>"
		self.BUFFER_SIZE = 4096 # send 4096 bytes each time step

		# the ip address or hostname of the server, the receiver
		self.host = "192.168.1.101"
		# the port, let's use 5001
		self.port = 5001
		# the name of file we want to send, make sure it exists
		self.filename = "data.csv"

	# get the file size
	def get_file_size(self):
		self.filesize = os.path.getsize(self.filename)

	def connect(self):
		print(f"[+] Connecting to {self.host}:{self.port}")
		self.s.connect((self.host, self.port))
		print("[+] Connected.")

		# send the filename and filesize
		self.s.send(f"{self.filename}{self.SEPARATOR}{self.filesize}".encode())

		# start sending the file
		progress = tqdm.tqdm(range(self.filesize), f"Sending {self.filename}", unit="B", unit_scale=True, unit_divisor=1024)
		with open(self.filename, "rb") as f:

		while True:
			# read the bytes from the file
			bytes_read = f.read(self.BUFFER_SIZE)
			if not bytes_read:
				# file transmitting is done
				break

			# we use sendall to assure transimission in ..
			# busy networks
			self.s.sendall(bytes_read)
			# update the progress bar
			progress.update(len(bytes_read))

		# close the socket
		self.s.close()
