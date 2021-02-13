import pyttsx3
import PyPDF2
from tkinter.filedialog import *
from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('Audio Book')
text = Label(root, text = 'Please pick any pdf file')
text.pack()
photo = PhotoImage(file='pdf.png')
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)
def chose_btn():
    book = askopenfilename()
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    for num in range(7, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()

btn = Button(root, image=photo, command=chose_btn)
btn.pack()
root.mainloop()


