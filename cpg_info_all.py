from paramiko import client
import os
import zipfile
from tkinter import messagebox
from tkinter_main import * 



class ssh:
	client = None
	def __init__(self, address, username, password):
		print("******Connecting to server...******")
		self.client = client.SSHClient()
		self.client.set_missing_host_key_policy(client.AutoAddPolicy())
		self.client.connect(address, username = username, password = password, look_for_keys = False)
		


	def sendCommand(self, command):
		if(self.client):
			stdin, stdout, stderr = self.client.exec_command(command)
			while not stdout.channel.exit_status_ready():
                # Print data when available
				if stdout.channel.recv_ready():
					alldata = stdout.channel.recv(1024)
					prevdata = b"1" # Just to initialize
					while prevdata: # Won't exit till the previously received data is None or Null 
					    prevdata = stdout.channel.recv(1024)
					    alldata += prevdata
					return str(alldata, 'utf-8')
		else:
			print("Connection not opened...")

	def cpg_info(self, file_cpg_info):
		show_cpg = self.sendCommand("showcpg")
		file_cpg_info.write("*******showcpg**********\n"+str(show_cpg))
		file_cpg_info.write("\n\n\n")
		show_cpg_sdg = self.sendCommand("showcpg -sdg")
		file_cpg_info.write("*******showcpg -sdg**********\n"+str(show_cpg_sdg))
		file_cpg_info.write("\n\n\n")
		show_cpg_r = self.sendCommand("showcpg -r")
		file_cpg_info.write("*******showcpg -r**********\n"+str(show_cpg_r))
		file_cpg_info.write("\n\n\n")
		show_cpg_sag = self.sendCommand("showcpg -sag")
		file_cpg_info.write("*******showcpg -sag**********\n"+str(show_cpg_sag))
		file_cpg_info.write("\n\n\n")
		show_cpg_space = self.sendCommand("showcpg -space")
		file_cpg_info.write("*******showcpg -space**********\n"+str(show_cpg_space))

	def node_info(self, file_node_info):
		show_node_d = self.sendCommand("shownode -d")
		file_node_info.write("*******shownode -d**********\n"+str(show_node_d))
		file_node_info.write("\n\n\n")
		show_node_i = self.sendCommand("shownode -i")
		file_node_info.write("*******shownode -i**********\n"+str(show_node_i))
		file_node_info.write("\n\n\n")
		
	def port_info(self, file_port_info):
		show_port = self.sendCommand("showport")
		file_port_info.write("*******showport**********\n"+str(show_port))
		file_port_info.write("\n\n\n")
		show_port_c = self.sendCommand("showport -c")
		file_port_info.write("*******showport -c**********\n"+str(show_port_c))
		file_port_info.write("\n\n\n")


# Using the Tkinter file to generate the GUI
# Getting the values from the Tkinter GUI
# info_to_show contains the checkbox values on the second frame to know what information we need to put inside the directory as a file
cool = display() 
ip, user, passwrd, info_to_show = cool.display_function() 

# Connecting to different machines and making different directories of each machine
for index in range(0,len(ip)): 
	connection = ssh(ip[index], user[index], passwrd[index])

	print("Connected to ip: " + ip[index] )
	try:
		os.makedirs(".\\"+ip[index])
	except OSError:
		pass

# Making the required files with the relevant information
	if(info_to_show[0]):
		file_name = "cpgInfo_"+ip[index]+".txt"
		file_pointer = open(os.path.join('.\\'+ip[index], file_name), "w+")
		connection.cpg_info(file_pointer)
		print("The file with all CPG details is made with name: cpgInfo_"+ ip[index]+".txt")

	if(info_to_show[1]):
		file_name = "nodeInfo_"+ip[index]+".txt"
		file_pointer = open(os.path.join('.\\'+ip[index], file_name), "w+")
		connection.node_info(file_pointer)
		print("The file with all node details is made with name: nodeInfo_"+ ip[index]+".txt")

	if(info_to_show[2]):
		file_name = "portInfo_"+ip[index]+".txt"
		file_pointer = open(os.path.join('.\\'+ip[index], file_name), "w+")
		connection.port_info(file_pointer)
		print("The file with all port details is made with name: portInfo_"+ ip[index]+".txt")

# Creating .zip file for separate folders separately
	print("Creating a .zip file for the above .txt files..")
	zf = zipfile.ZipFile(os.path.join('.\\'+ip[index]+"\\"+ip[index]+".zip"), mode='w')
	try:
		zf.write(os.path.join('.\\'+ip[index]+"\cpgInfo_"+ip[index]+".txt"))
		zf.write(os.path.join('.\\'+ip[index]+"\\nodeInfo_"+ip[index]+".txt"))
		zf.write(os.path.join('.\\'+ip[index]+"\portInfo_"+ip[index]+".txt"))
	finally:
		zf.close
		print("Created the "+ip[index]+".zip file")

