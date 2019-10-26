import tkinter as tk
from spotify import createTopTen, createToken

root= tk.Tk()




canvas1 = tk.Canvas(root, width = 300, height = 300, bg='black')
canvas1.pack()

verseATility_text = tk.Label(root, text="Welcome to Verse-A-Tility, the only app that creates a playist of your most karaokeable songs!", fg='#1DB954', bg='black')
canvas1.create_window(150, 100, window=verseATility_text)
base_text = tk.Label(root, text="Please input your Spotify username", fg='#1DB954', bg='black')
base_text_created = canvas1.create_window(150, 200, window=base_text)



inputBox = tk.Entry(root, text = 'Please input your Spotify username')

def submit_url ():
    createTopTen(inputBox.get())
    final_text = tk.Label(root, text="Congrats! Go check your Spotify app for the new playlist!")
    canvas1.create_window(150, 200, window=final_text)

def submit_username ():
    createToken(inputBox.get())
    button2 = tk.Button(root, text='Please input the url you were directed to and hit me!',
                              command=submit_url,
                              fg='#1DB954',
                              bg = 'black',
                              font=('helvetica', 12))
    canvas1.delete(button1_created)
    canvas1.delete(base_text_created)
    button2_created = canvas1.create_window(250, 150, window = button2)

button1 = tk.Button(text='Submit', command=submit_username, bg='black', fg='#1DB954')
button1_created = canvas1.create_window(250, 150, window=button1)
canvas1.create_window(150, 150, window=inputBox)
#
# def hello ():
#     label1 = tk.Label(root, text= 'Hello World!', fg='green', font=('helvetica', 12, 'bold'))
#     canvas1.create_window(150, 200, window=label1)
#
# button1 = tk.Button(text='Click Me',command=hello, bg='brown',fg='white')
# canvas1.create_window(150, 150, window=button1)

root.mainloop()
