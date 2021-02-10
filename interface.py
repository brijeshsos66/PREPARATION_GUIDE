import pyttsx3
import PyPDF2
from tkinter import *
from tkinter.filedialog import *
window = Tk()
window.configure(background = 'light blue')
window.geometry("500x300")

window.title("AUDIOBOOK - TEXT TO SPEECH")
speaker = pyttsx3.init()
#FUNCTIONS SPACE
def audiobookfunc():
    book = askopenfilename()
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speaker = pyttsx3.init()

    for num in range(0,pages):
        page = pdfReader.getPage(num)
        txt = page.extractText()
        speaker.say(txt)
        speaker.runAndWait()

def stop_func():
    speaker.stop()

def quit_func():
    window.destroy()

#WIDGETS
l1 = Label(window,text = "AudioBook - Listen Anywhere Anytime")
l1.grid(column = 0, row = 0)
l1.pack()

#labels name
book_name = Label(window,text = "Click To Select .pdf file & Listen: ").place(x=40,y=60)

keywords = Label(window,text = "Keywords: ").place(x = 40,y = 100)

notes = Label(window,text = "Notes: ").place(x = 40, y = 140)

#text inside labels
    
keyword_input = Entry(window,width = 60).place(x = 105,y = 100)

notes_input = Entry(window,width = 60).place(x = 105,y = 140)

#operation
convert_button=Button(window,text="Select & Listen", command = audiobookfunc).place(x = 250,y=60)

stop_button=Button(window,text="Stop", command= stop_func).place(x = 40,y=190)

quit_button=Button(window,text="Quit", command = quit_func).place(x = 435,y=190)

window.mainloop()
