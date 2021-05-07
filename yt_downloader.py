from tkinter import *
from tkinter import messagebox
from pytube import  YouTube
app=Tk()


def do_btn():
	video=YouTube(f"{entry.get()}")
	stream=video.streams.get_highest_resolution()
	stream.download()
	
	label1.config(text="Your Video Downloaded")
	messagebox.askyesno("Feedback","You are enjoying our software")
	
label1=Label(text="paste your video link")
label1.grid(row=2,column=1)	

entry=Entry()
btn=Button(text="Download",command=do_btn)

entry.grid(row=1,column=1,padx=15,)
btn.grid(row=1,column=2,padx=15)

app.mainloop()
