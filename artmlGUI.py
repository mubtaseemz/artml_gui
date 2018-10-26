from tkinter import Tk, Label, Text, Button, Frame, W, E, N, S, END
from tkinter.filedialog import askopenfilename
import pandas as pd

class artmlGUI:
	def __init__(self, master):
		self.master = master
		master.title("ARTML")
		
		# initializes frame for buttons
		self.button_window_frame = Frame(master, bg="red")
		self.button_window_frame.grid(row=0, column=0, rowspan=1, sticky=W+E+N+S)
		
		# initializes display window frame
		self.display_window_frame = Frame(master, highlightbackground="blue", highlightcolor="blue", highlightthickness=1, width=600, height=500, bd=0)
		self.display_window_frame.grid(row=1, column=0, sticky=W+E+N+S)
		
		# imports csv file data for artml operation
		self.import_csv_data_button = Button(self.button_window_frame, text = "Select File", command=self.import_csv_data)
		self.import_csv_data_button.grid(row=0, column=0)
		
		# displays BET
		self.bet_button = Button(self.button_window_frame, text="BET", command=self.bet)
		self.bet_button.grid(row=0, column=1)
	
	
	def import_csv_data(self):
		csv_file_path = askopenfilename(initialdir = "/", title = "Select csv file")
		print(csv_file_path)
		self.df = pd.read_csv(csv_file_path)
		#print(self.df)
		
	def bet(self):
		from artml import module
		# something's wrong with Sundeep's code
		# can't import this #from scipy.stats import chisqprob
		self.basic = module.BET(self.df)
		print(self.basic)
		# diplaying bet table in tabular format
		text = Text(self.display_window_frame)
		text.insert(END, str(self.basic))
		text.grid(row=1, column=0, sticky=W+E+N+S)

	#def lda(self):
		
	
	
root = Tk()
root.geometry("600x500")
my_gui = artmlGUI(root)
root.mainloop()