from tkinter import *
from tkinter import ttk

class display:
	ip_real = []
	user_real = []
	passwrd_real = []
	ip_fix = []
	user_fix = []
	passwrd_fix = []
	frame2_returned_values = []
	def display_function(self):
		root = Tk()
		root.title("Enter the details of the machines..")
		
		frame2 = Frame(root) # The order here tells which frame will be above which one
		frame1 = Frame(root)
		
		ttk.Style().theme_use('vista')

		def save_values_f1(event): # It triggers on clicking the left mouse button on the "Submit The Credentials.." button
			for i in range(0,10):
				self.ip_real.append(ip[i].get())
				self.user_real.append(user[i].get())
				self.passwrd_real.append(passwrd[i].get())

			# Using List Comprehensions to remove the empty strings
			self.ip_fix = [x for x in self.ip_real if x] 
			self.user_fix = [x for x in self.user_real if x]     
			self.passwrd_fix = [x for x in self.passwrd_real if x]

			# Displaying the error Dialog Boxes if one or more columns are left blank
			if not self.ip_fix:
				messagebox.showerror("ERROR" ,"Please enter the IP Addresse(s)")
			if not self.user_fix:
				messagebox.showerror("ERROR" ,"Please enter the User Name(s)")
			if not self.passwrd_fix:
				messagebox.showerror("ERROR" ,"Please enter the Password(s)")	

			# Closing the frame and displaying the new one if following conditions meet
			if((self.ip_fix and self.user_fix and self.passwrd_fix) and (len(self.passwrd_fix) == len(self.user_fix) == len(self.passwrd_fix))):
				close_GUI(frame1)
			else:
				messagebox.showerror("ERROR", "Please fill username(s) and password(s) for the corresponding IP(s) properly")
			

		def save_values_f2(event):
			self.frame2_returned_values.append(var1.get())
			self.frame2_returned_values.append(var2.get())
			self.frame2_returned_values.append(var3.get())
			close_GUI(frame2)
			root.destroy()

		def close_GUI(Frame):
			Frame.destroy()
		
		# ************* Frame1 is configured here
		Label(frame1, text="IP Address", font="Verdana 10 bold", relief=RIDGE).grid(row=0, column=0, ipadx=80, pady=10)
		Label(frame1, text="Username", font="Verdana 10 bold", relief=RIDGE).grid(row=0, column=1, ipadx=80, pady=10 )
		Label(frame1, text="Password", font="Verdana 10 bold", relief=RIDGE).grid(row=0, column=2, ipadx=80, pady=10 )

		ip = []
		user = []
		passwrd = []

		for i in range(0,10):
			Label(frame1, text=str(i+1)+'.', font="Verdana 8", relief=RIDGE).grid(row=i+1, column=0, sticky=W, pady=2)
			ip.append(Entry(frame1, text="ip"+str(i+1), relief=SUNKEN, width=36, highlightthickness=2))
			ip[i].grid(row=i+1, column=0, sticky=E,  pady=2)
			user.append(Entry(frame1, text="user"+str(i+1), relief=SUNKEN, width=38, highlightthickness=2))
			user[i].grid(row=i+1, column=1, sticky=W, padx=5, pady=2)
			passwrd.append(Entry(frame1, text="passwrd"+str(i+1), relief=SUNKEN, width=38, highlightthickness=2))
			passwrd[i].grid(row=i+1, column=2, sticky=W, pady=2)

		submit_f1 = ttk.Button(frame1, text="Submit The Credentials, move to next page -->")
		submit_f1.grid(row=12, column=1)
		submit_f1.bind("<Button-1>", save_values_f1)

		# nextButton = ttk.Button(frame1, text="Next >", width=8, command=frame1.lower)
		# nextButton.grid(row=12, column=2, sticky=E )
				
		#************* Frame2 will be configured here
		label = Label(frame2, text="Check the things you want to have:")
		label.grid(row=0, column=0, pady=4, padx=2)

		var1 = BooleanVar()
		var2 = BooleanVar()
		var3 = BooleanVar()
		Checkbutton(frame2, text="CPG Information", variable=var1).grid(row=1, column=1, pady=2, sticky=W)
		Checkbutton(frame2, text="Node Information", variable=var2).grid(row=2, column=1, pady=2, sticky=W)
		Checkbutton(frame2, text="Port Information", variable=var3).grid(row=3, column=1, pady=2, sticky=W)
		

		submit_f2 = ttk.Button(frame2, text="Submit")
		submit_f2.grid(row=5, column=1, sticky=W)
		submit_f2.bind("<Button-1>", save_values_f2)
	

		root.geometry("720x350")
		
		frame1.grid(row=0, column=0, sticky=N+S+E+W) # To expand the frame to have all the widgets in it
		frame2.grid(row=0, column=0, sticky=N+S+E+W)
		
		root.mainloop()
		return self.ip_fix, self.user_fix, self.passwrd_fix, self.frame2_returned_values



