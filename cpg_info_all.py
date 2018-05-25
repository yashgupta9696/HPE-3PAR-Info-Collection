from paramiko import client
import os
import zipfile
from tkinter import messagebox
from tkinter_main import * 

class ssh:
	client = None
	def __init__(self, address, username, password):
		print("******Connecting to the 3PAR Machine...******")
		self.client = client.SSHClient()
		self.client.set_missing_host_key_policy(client.AutoAddPolicy())
		self.client.connect(address, username = username, password = password, look_for_keys = False)
	def close_connect(self):
		self.client.close()


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
		showspace = self.sendCommand("showspace")
		file_cpg_info.write("*******showspace**********\n"+str(showspace))
		file_cpg_info.write("\n\n\n")
		showspace_cpg = self.sendCommand("showspace -cpg")
		file_cpg_info.write("*******showspace -cpg**********\n"+str(showspace_cpg))
		

	def node_info(self, file_node_info):
		show_node_d = self.sendCommand("shownode -d")
		file_node_info.write("*******shownode -d**********\n"+str(show_node_d))
		file_node_info.write("\n\n\n")
		show_node_i = self.sendCommand("shownode -i")
		file_node_info.write("*******shownode -i**********\n"+str(show_node_i))
		file_node_info.write("\n\n\n")
		show_node_status = self.sendCommand("servicenode status")
		file_node_info.write("*******servicenode status**********\n"+str(show_node_status))
		

	def port_info(self, file_port_info):
		show_port = self.sendCommand("showport")
		file_port_info.write("*******showport**********\n"+str(show_port))
		file_port_info.write("\n\n\n")
		show_port_c = self.sendCommand("showport -c")
		file_port_info.write("*******showport -c**********\n"+str(show_port_c))
		file_port_info.write("\n\n\n")
		show_port_i = self.sendCommand("showport -i")
		file_port_info.write("*******showport -i**********\n"+str(show_port_i))
		file_port_info.write("\n\n\n")
		show_port_iscsi = self.sendCommand("showport -iscsi")
		file_port_info.write("*******showport -iscsi**********\n"+str(show_port_iscsi))
		file_port_info.write("\n\n\n")
		show_port_iscsiname = self.sendCommand("showport -iscsiname")
		file_port_info.write("*******showport -iscsiname**********\n"+str(show_port_iscsiname))
		file_port_info.write("\n\n\n")
		show_port_par = self.sendCommand("showport -par")
		file_port_info.write("*******showport -par**********\n"+str(show_port_par))
		file_port_info.write("\n\n\n")
		show_port_rc = self.sendCommand("showport -rc")
		file_port_info.write("*******showport -rc**********\n"+str(show_port_rc))
		file_port_info.write("\n\n\n")
		show_port_sfp = self.sendCommand("showport -sfp")
		file_port_info.write("*******showport -sfp**********\n"+str(show_port_sfp))
		file_port_info.write("\n\n\n")
		show_port_sfpd = self.sendCommand("showport -sfp -d")
		file_port_info.write("*******showport -sfp -d**********\n"+str(show_port_sfpd))
		file_port_info.write("\n\n\n")
		show_port_sfpddm = self.sendCommand("showport -sfp -ddm")
		file_port_info.write("*******showport -sfp -ddm**********\n"+str(show_port_sfpddm))
		file_port_info.write("\n\n\n")
		show_port_arp = self.sendCommand("showportarp")
		file_port_info.write("*******showportarp**********\n"+str(show_port_arp))
		file_port_info.write("\n\n\n")
		show_port_dev = self.sendCommand("showportdev")
		file_port_info.write("*******showportdev**********\n"+str(show_port_dev))
		file_port_info.write("\n\n\n")
		show_port_isns = self.sendCommand("showportisns")
		file_port_info.write("*******showportisns**********\n"+str(show_port_isns))
		
	def vv_info(self, file_vv_info):
		showvv = self.sendCommand("showvv")
		file_vv_info.write("*******showvv**********\n"+str(showvv))
		file_vv_info.write("\n\n\n")
		showvv_d = self.sendCommand("showvv -d")
		file_vv_info.write("*******showvv -d**********\n"+str(showvv_d))
		file_vv_info.write("\n\n\n")
		showvv_p = self.sendCommand("showvv -p")
		file_vv_info.write("*******showvv -p**********\n"+str(showvv_p))
		file_vv_info.write("\n\n\n")
		showvv_r = self.sendCommand("showvv -r")
		file_vv_info.write("*******showvv -r**********\n"+str(showvv_r))
		file_vv_info.write("\n\n\n")
		showvv_s = self.sendCommand("showvv -s")
		file_vv_info.write("*******showvv -s**********\n"+str(showvv_s))
		file_vv_info.write("\n\n\n")
		showvv_p_dds = self.sendCommand("showvv -p -prov dds")
		file_vv_info.write("*******showvv -p -prov dds**********\n"+str(showvv_p_dds))
		file_vv_info.write("\n\n\n")
		showvvcpg = self.sendCommand("showvvcpg")
		file_vv_info.write("*******showvvcpg**********\n"+str(showvvcpg))
		file_vv_info.write("\n\n\n")
		showvvset = self.sendCommand("showvvset")
		file_vv_info.write("*******showvvset**********\n"+str(showvvset))
		file_vv_info.write("\n\n\n")
		showvlun = self.sendCommand("showvlun")
		file_vv_info.write("*******showvlun**********\n"+str(showvlun))
		file_vv_info.write("\n\n\n")
		showld = self.sendCommand("showld")
		file_vv_info.write("*******showld**********\n"+str(showld))
		file_vv_info.write("\n\n\n")
		showld_d = self.sendCommand("showld -d")
		file_vv_info.write("*******showld_d**********\n"+str(showld_d))
		file_vv_info.write("\n\n\n")
		show_flashcache = self.sendCommand("showflashcache -vvset")
		file_vv_info.write("*******showflashcache -vvset**********\n"+str(show_flashcache))
		file_vv_info.write("\n\n\n")
		showvvolsc = self.sendCommand("showvvolsc")
		file_vv_info.write("*******showvvolsc**********\n"+str(showvvolsc))
		

	def cage_info(self, file_cage_info):
		show_cage_d = self.sendCommand("showcage -d")
		file_cage_info.write("*******showcage -d**********\n"+str(show_cage_d))
		file_cage_info.write("\n\n\n")
		show_cage_sfp = self.sendCommand("showcage -sfp")
		file_cage_info.write("*******showcage -sfp**********\n"+str(show_cage_sfp))
		file_cage_info.write("\n\n\n")
		show_cage_sfp_ddm = self.sendCommand("showcage -sfp -ddm")
		file_cage_info.write("*******showcage -sfp -ddm**********\n"+str(show_cage_sfp_ddm))
		file_cage_info.write("\n\n\n")
		show_cage_sfp_d = self.sendCommand("showcage -sfp -d")
		file_cage_info.write("*******showcage -sfp -d**********\n"+str(show_cage_sfp_d))
		file_cage_info.write("\n\n\n")
		show_pd = self.sendCommand("showpd")
		file_cage_info.write("*******showpd**********\n"+str(show_pd))
		file_cage_info.write("\n\n\n")
		show_pd_c = self.sendCommand("showpd -c")
		file_cage_info.write("*******showpd -c**********\n"+str(show_pd_c))
		file_cage_info.write("\n\n\n")
		show_pd_i = self.sendCommand("showpd -i")
		file_cage_info.write("*******showpd -i**********\n"+str(show_pd_i))
		file_cage_info.write("\n\n\n")
		show_pd_s = self.sendCommand("showpd -s")
		file_cage_info.write("*******showpd -s**********\n"+str(show_pd_s))
		

	def mgr_info(self, file_mgr_info):
		show_snmpmgr = self.sendCommand("showsnmpmgr")
		file_mgr_info.write("*******showsnmpmgr**********\n"+str(show_snmpmgr))
		file_mgr_info.write("\n\n\n")
		show_sys_d = self.sendCommand("showsys -d")
		file_mgr_info.write("*******showsys -d**********\n"+str(show_sys_d))
		file_mgr_info.write("\n\n\n")
		show_sys_param = self.sendCommand("showsys -param")
		file_mgr_info.write("*******showsys -param**********\n"+str(show_sys_param))
		file_mgr_info.write("\n\n\n")
		show_sys_space = self.sendCommand("showsys -space")
		file_mgr_info.write("*******showsys -space**********\n"+str(show_sys_space))
		file_mgr_info.write("\n\n\n")
		show_sysmgr = self.sendCommand("showsysmgr")
		file_mgr_info.write("*******showsysmgr**********\n"+str(show_sysmgr))
		file_mgr_info.write("\n\n\n")
		show_sysmgr_l = self.sendCommand("showsysmgr -l")
		file_mgr_info.write("*******showsysmgr -l**********\n"+str(show_sysmgr_l))
		file_mgr_info.write("\n\n\n")
		show_battery = self.sendCommand("showbattery")
		file_mgr_info.write("*******showbattery**********\n"+str(show_battery))
		file_mgr_info.write("\n\n\n")
		show_cim = self.sendCommand("showcim")
		file_mgr_info.write("*******showcim**********\n"+str(show_cim))
		file_mgr_info.write("\n\n\n")
		show_license = self.sendCommand("showlicense")
		file_mgr_info.write("*******showlicense**********\n"+str(show_license))
		file_mgr_info.write("\n\n\n")
		show_net = self.sendCommand("shownet")
		file_mgr_info.write("*******shownet**********\n"+str(show_net))
		file_mgr_info.write("\n\n\n")
		show_net_d = self.sendCommand("shownet -d")
		file_mgr_info.write("*******shownet -d**********\n"+str(show_net_d))
		file_mgr_info.write("\n\n\n")
		show_version = self.sendCommand("showversion")
		file_mgr_info.write("*******showversion**********\n"+str(show_version))
		file_mgr_info.write("\n\n\n")
		show_toc = self.sendCommand("showtoc")
		file_mgr_info.write("*******showtoc**********\n"+str(show_toc))
	


	def host_info(self, file_host_info):
		show_host_d = self.sendCommand("showhost -d")
		file_host_info.write("*******showhost -d**********\n"+str(show_host_d))
		file_host_info.write("\n\n\n")
		show_host_chap = self.sendCommand("showhost -chap")
		file_host_info.write("*******showhost -chap**********\n"+str(show_host_chap))
		file_host_info.write("\n\n\n")
		show_host_set = self.sendCommand("showhostset")
		file_host_info.write("*******showhostset**********\n"+str(show_host_set))
		file_host_info.write("\n\n\n")
		show_date = self.sendCommand("showdate")
		file_host_info.write("*******showdate**********\n"+str(show_date))
		file_host_info.write("\n\n\n")
		show_domain_d = self.sendCommand("showdomain -d")
		file_host_info.write("*******showdomain -d**********\n"+str(show_domain_d))
		file_host_info.write("\n\n\n")
		show_auth_param = self.sendCommand("showauthparam")
		file_host_info.write("*******showauthparam**********\n"+str(show_auth_param))
		file_host_info.write("\n\n\n")
		show_domainset = self.sendCommand("showdomainset")
		file_host_info.write("*******showdomainset**********\n"+str(show_domainset))
	
	def other_info(self, file_other_info):
		showrcopy_d = self.sendCommand("showrcopy -d")
		file_other_info.write("*******showrcopy -d**********\n"+str(showrcopy_d))
		file_other_info.write("\n\n\n")	
		showsched_all = self.sendCommand("showsched -all")
		file_other_info.write("*******showsched -all**********\n"+str(showsched_all))
		file_other_info.write("\n\n\n")
		showsched_all = self.sendCommand("showsched -all")
		file_other_info.write("*******showsched -all**********\n"+str(showsched_all))
		file_other_info.write("\n\n\n")
		showtask = self.sendCommand("showtask")
		file_other_info.write("*******showtask**********\n"+str(showtask))
		file_other_info.write("\n\n\n")
		controlenc = self.sendCommand("controlencryption status")
		file_other_info.write("*******controlencryption status**********\n"+str(controlenc))
		file_other_info.write("\n\n\n")
		controlenc = self.sendCommand("controlencryption status")
		file_other_info.write("*******controlencryption status**********\n"+str(controlenc))
		file_other_info.write("\n\n\n")
		showflashcache = self.sendCommand("showflashcache")
		file_other_info.write("*******showflashcache**********\n"+str(showflashcache))
		file_other_info.write("\n\n\n")
		showflashcache = self.sendCommand("showflashcache")
		file_other_info.write("*******showflashcache**********\n"+str(showflashcache))
		file_other_info.write("\n\n\n")
		show_sr = self.sendCommand("showsr")
		file_other_info.write("*******showsr**********\n"+str(show_sr))
		file_other_info.write("\n\n\n")
		show_sr_alert = self.sendCommand("showsralertcrit")
		file_other_info.write("*******showsralertcrit**********\n"+str(show_sr_alert))
		file_other_info.write("\n\n\n")
		show_wsapi = self.sendCommand("showwsapi")
		file_other_info.write("*******showwsapi**********\n"+str(show_wsapi))
		file_other_info.write("\n\n\n")
		control_recoveryauth = self.sendCommand("controlrecoveryauth status")
		file_other_info.write("*******controlrecoveryauth status**********\n"+str(control_recoveryauth))
		file_other_info.write("\n\n\n")
		show_inventory = self.sendCommand("showinventory -svc")
		file_other_info.write("*******showinventory -svc**********\n"+str(show_inventory))
		file_other_info.write("\n\n\n")
		show_template = self.sendCommand("showtemplate")
		file_other_info.write("*******showtemplate**********\n"+str(show_template))
		file_other_info.write("\n\n\n")
		showqos = self.sendCommand("showqos")
		file_other_info.write("*******showqos**********\n"+str(showqos))
		file_other_info.write("\n\n\n")
		showvasa = self.sendCommand("showvasa")
		file_other_info.write("*******showvasa**********\n"+str(showvasa))
		file_other_info.write("\n\n\n")
		showfed = self.sendCommand("showfed")
		file_other_info.write("*******showfed**********\n"+str(showfed))
		



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

	if(info_to_show[3]):
		file_name = "vvInfo_"+ip[index]+".txt"
		file_pointer = open(os.path.join('.\\'+ip[index], file_name), "w+")
		connection.vv_info(file_pointer)
		print("The file with all VV details is made with name: vvInfo_"+ ip[index]+".txt")

	if(info_to_show[4]):
		file_name = "cageInfo_"+ip[index]+".txt"
		file_pointer = open(os.path.join('.\\'+ip[index], file_name), "w+")
		connection.cage_info(file_pointer)
		print("The file with all cage details is made with name: cageInfo_"+ ip[index]+".txt")

	if(info_to_show[5]):
		file_name = "systemInfo_"+ip[index]+".txt"
		file_pointer = open(os.path.join('.\\'+ip[index], file_name), "w+")
		connection.mgr_info(file_pointer)
		print("The file with all system details is made with name: systemInfo_"+ ip[index]+".txt")

	if(info_to_show[6]):
		file_name = "hostInfo_"+ip[index]+".txt"
		file_pointer = open(os.path.join('.\\'+ip[index], file_name), "w+")
		connection.host_info(file_pointer)
		print("The file with all host details is made with name: hostInfo_"+ ip[index]+".txt")

	if(info_to_show[7]):
		file_name = "otherInfo_"+ip[index]+".txt"
		file_pointer = open(os.path.join('.\\'+ip[index], file_name), "w+")
		connection.other_info(file_pointer)
		print("The file with all the other details is made with name: otherInfo_"+ ip[index]+".txt")

# Creating .zip file for separate folders separately
	print("Creating a .zip file for the above .txt files..")
	zf = zipfile.ZipFile(os.path.join('.\\'+ip[index]+"\\"+ip[index]+".zip"), mode='w')
	try:
		if(info_to_show[0]):
			zf.write(os.path.join('.\\'+ip[index]+"\\cpgInfo_"+ip[index]+".txt"))
		if(info_to_show[1]):
			zf.write(os.path.join('.\\'+ip[index]+"\\nodeInfo_"+ip[index]+".txt"))
		if(info_to_show[2]):
			zf.write(os.path.join('.\\'+ip[index]+"\\portInfo_"+ip[index]+".txt"))
		if(info_to_show[3]):
			zf.write(os.path.join('.\\'+ip[index]+"\\vvInfo_"+ip[index]+".txt"))
		if(info_to_show[4]):
			zf.write(os.path.join('.\\'+ip[index]+"\\cageInfo_"+ip[index]+".txt"))
		if(info_to_show[5]):
			zf.write(os.path.join('.\\'+ip[index]+"\\systemInfo_"+ip[index]+".txt"))
		if(info_to_show[6]):
			zf.write(os.path.join('.\\'+ip[index]+"\\hostInfo_"+ip[index]+".txt"))
		if(info_to_show[7]):
			zf.write(os.path.join('.\\'+ip[index]+"\\otherInfo_"+ip[index]+".txt"))
	finally:
		zf.close
		print("Created the "+ip[index]+".zip file")

	connection.close_connect()

