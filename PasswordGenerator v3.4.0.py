#                                         PasswordGenerator 09.08.2021/10.08.2021 Version: 3.2.0
#Source code: Youtube Tutorial from Codemy.com https://www.youtube.com/watch?v=XaVp2l6Z_Dc, RightclickMenü: https://www.youtube.com/watch?v=KRuUtNxOb_k
#                                             <<Modyfied the Original Project from Codemy>>
#               Special thanks to Tobias Monsees for an more eficiant code Generator and also for Codemy for helping with his Videos :)

# Version die im info Popup und im titel angezeigt wird
Version = "3.4.0"

# TODO  I need to add a options to choose with witch carekters the Passwordgeneretor should generate the password
# Alle importierten Bibliotheken
from tkinter import *
from random import randint
import os
import numpy as np

#--------------------------------------------------------------------------------------------
# Erstellung des Hauptfensters
root = Tk()

root.title(f"Passwort Generator v{Version}")
root.resizable(False, False)  # T
#root.geometry("500x500")  #500x300 default without Checkboxes
root.iconbitmap('test2.ico') # Ads a Ico Picture to the Programm 

# places window in the middle
window_height = 300 #y    type here the height of the main window
window_width = 500 #x  type here the with of the main window

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

#-----------------------------------------------------------------------------------------------
# The Core of this Programm

def destro():
    win.destroy()
# Herausgabe von generirtem Paswort # Das ❤ vom Passwortgenerator
def new_rand():

    # TODO Fix Error der nach eingabe eines Buchstaben oder einem Fremdzeichen passiert
    global win
    global pw_entry
    global my_password
    global my_entry
    global integer_list
    global pw_lenght
    #ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÖÄÜöäü!§$%&/()=?``´´@;,:._-'#*+~ß}][{²³^^°°|"


    if my_entry.get() == "":
        #print(varc.get())
        pw_entry.delete(0, END)

        pw_lenght = int(0)


        my_password = ''


        for x in range(pw_lenght):
            my_password += chr(randint(33, 126))
        pw_entry.insert(0, my_password)

        # Benachrichtigung für nicht eingegebene anzahl an charakteren im Fenster
        win = Tk()
        #win.eval('tk::PlaceWindow . center')
        #win.geometry("300x100")
        win.resizable(False, False)
        win.title("Zeichen !!!")
        win.iconbitmap('test2.ico')

# place window in the center
        window_height3 = 100
        window_width3 = 300

        screen_width3 = win.winfo_screenwidth()
        screen_height3 = win.winfo_screenheight()

        x_cordinate3 = int((screen_width3 / 2) - (window_width3 / 2))
        y_cordinate3 = int((screen_height3 / 2) - (window_height3 / 2))

        win.geometry("{}x{}+{}+{}".format(window_width3, window_height3, x_cordinate3, y_cordinate3))
#-------------------------------------------------------------------------------------------------------

        okButton = Label(win, text="Bitte eine Zahl eingeben", fg="black", font="Calibri 11")
        okButton.place(x=72, y=24)

        okButtonNewrand = Button(win, text="OK", bg="#dc5432", fg="black", command=destro)
        okButtonNewrand.place(x=135, y=60)


    else:
        #if varc.get() == "on": # KLein und Großbuchstaben
         #   print("test")

        #if varc.get() == "onS": # Sonderzeichen
         #   A = np.arange(33, 47)
          #  B = np.arange(58, 63)

        # if varc.get() == "onA":  # Alles
           # A = 33
            # B = 126


        pw_entry.delete(0, END)
        A = 33
        B = 126
        a = np.arange(1, 3)
        b = np.arange(7, 9)
        # print([*a, *b])
        n_symbols = B-A+1
        pw_lenght = int(my_entry.get())
        random_index_list = np.random.permutation(n_symbols) + A
        my_password = ''
        integer_list = []
        if pw_lenght < n_symbols:
            integer_list.clear()
            my_password = ''
            for x in range(pw_lenght):
                my_password += chr(random_index_list[x])
            pw_entry.insert(0, my_password)
        else:
            pw_entry.delete(0, END)
            pw_lenght = int(my_entry.get())
            my_password = ''
            for x in range(pw_lenght):
                my_password += chr(randint(A, B))
            pw_entry.insert(0, my_password)



def destroyKopiert():
    top.destroy()
# Kopiert Popup
def kopiert():

    global top
    top = Tk()

    #top.geometry("300x100")
    top.resizable(False, False)  # T
    top.title("Kopiert !!!")
    top.iconbitmap('test2.ico')

    window_height1 = 100
    window_width1 = 300

    screen_width1 = top.winfo_screenwidth()
    screen_height1 =top.winfo_screenheight()

    x_cordinate1 = int((screen_width1 / 2) - (window_width1 / 2))
    y_cordinate1 = int((screen_height1 / 2) - (window_height1 / 2))

    top.geometry("{}x{}+{}+{}".format(window_width1, window_height1, x_cordinate1, y_cordinate1))

    okButton = Label(top, text="  Kopiert !!!", fg="black", font="Calibri 11")
    okButton.place(x=112, y=23)

    Destroy= Button(top, text="OK",bg="#dc5432", fg="black", command=destroyKopiert)
    Destroy.place(x=135, y=60)

    #top.mainloop()


# Der Kopieren Knopf + ausfuhren von Kopiert Popup
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())


# läst das Kopieren Popup nur dann öffnen wenn ein random passwort generiert und Kopiert worden ist
    if pw_entry.get() == "":
        pass
    else:
        kopiert()

#------------------------------------------------------------------------------------------------------------------------

# Benutzeroberfläche >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
lf = LabelFrame(root, text="Wie viele Zeichen?")
lf.pack(pady=20)
my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)
my_entry.focus_set()


pw_entry = Entry(root, font=("Helvetica", 24), bd=0, bg='systembuttonface')
pw_entry.pack(pady=20)


my_frame = Frame(root)
my_frame.pack(pady=20)


clip_button = Button(my_frame, text="In Zwischenablage Kopieren", command=clipper)
clip_button.grid(row=0, column=2, padx=10)


my_button = Button(my_frame, text="Passwort Generieren",bg="#2E9AFE", fg="black", command=new_rand)
my_button.grid(row=0, column=0, padx=10)
root.bind('<Return>',lambda event:new_rand())

exitButton = Button(my_frame, text="Abbrechen",bg="#dc5432", fg="black", command=root.destroy)
exitButton.grid(row=0, column=1, padx=10)


#---------------------------------------------------------------------------------------------------------

def destroyPopup():
    dot.destroy()

#Popup Information
def Popup():

    global dot

    dot =Tk()

    dot.configure(background="systembuttonface")
    #dot.geometry("300x170")  # 260x150 newer 300x210
    dot.resizable(False, False)
    dot.title("Passwortgenerator Info")
    titl= Label(dot, text=f"Passwordgenerator mit Python v{Version}", bg="systembuttonface", fg="black")
    titl.place(x=60, y=90)

# centers this Window on the desktop
    window_height2 = 170
    window_width2 = 300

    screen_width2 = dot.winfo_screenwidth()
    screen_height2 = dot.winfo_screenheight()

    x_cordinate2 = int((screen_width2 / 2) - (window_width2 / 2))
    y_cordinate2 = int((screen_height2 / 2) - (window_height2 / 2))

    dot.geometry("{}x{}+{}+{}".format(window_width2, window_height2, x_cordinate2, y_cordinate2))


# Buttons and titles/lables
    textSecond3 = """      Passwort Generator zum
     Generieren von Passwörtern """

    textSecond4 = """Programmmiert in Python"""

    dot.iconbitmap('test2.ico')
    # beschriftung im Fenster
    second = Label(dot, text=textSecond3, bg="systembuttonface", fg="black")
    # second.place(x=20, y=210)  # x=20, y=110
    second.pack(pady=20, padx=20)

    second2 = Label(dot, text=textSecond4, bg="systembuttonface", fg="black")
    second2.place(x=85, y=70)  # x=20, y=110



    okButton = Button(dot, text="OK",bg="#dc5432", fg="black", command=destroyPopup)
    okButton.place(x=135, y=130)

    dot.mainloop()

    dot.mainloop()

#------------------------------------------------------------------------------------------------------------
# Rechtsklickmenü funktionen aufbau

def copy():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

    # läst das Kopieren Popup nur dann öffnen wenn ein random passwort generiert und Kopirt worden ist
    if pw_entry.get() == "":
        pass
    else:
        kopiert()

def quite():
    pw_entry.delete(0, END)

def delAll():
    pw_entry.delete(0, END)
    my_entry.delete(0, END)

def deleate():
    my_entry.delete(0, END)

def my_popup(e):
    my_menu.tk_popup(e.x_root, e.y_root)

def changes():
    os.startfile("Changelog PasswordGenerator.txt")

def Help():
    os.startfile("Help.txt")

def Licence():
    os.startfile("Licence.txt")

def credits1():
    os.startfile("Danke ❤.txt")

def KeyBindings():
    os.startfile("KeyBindings.txt")


my_menu = Menu(root, tearoff=False)
my_menu.add_command(label= "Kopieren (STRG+C)", command= copy)
my_menu.add_command(label= "Password löschen (ALT+P) ", command= quite)
my_menu.add_command(label="Charakteranzahl löschen (ALT+C)", command= deleate)
my_menu.add_command(label="Password generieren (ENTER)", command= new_rand)
my_menu.add_command(label="Alles löschen (ENTF/DEL)", command= delAll)

my_menu.add_separator()

my_menu.add_command(label="Hilfe (F1)", command= Help)
my_menu.add_command(label="KeyBindings (ALT+K)", command= KeyBindings)
my_menu.add_command(label="Danke ❤ (ALT+D)", command= credits1)
my_menu.add_command(label="Changelog (STRG+D)", command= changes)
my_menu.add_command(label="Lizenz (ALT+L)", command= Licence)
my_menu.add_command(label="Information (ALT+I)", command= Popup)

my_menu.add_separator()

my_menu.add_command(label= "Programm schließen (ESC)", command=root.quit)
root.bind("<Button-3>", my_popup)

# Keybindings
root.bind('<Control-c>',lambda event:copy())
root.bind('<Alt-p>',lambda event:quite())
root.bind('<Alt-c>',lambda event:deleate())

root.bind('<Delete>',lambda event:delAll())

root.bind('<F1>',lambda event:Help())
root.bind('<Alt-d>',lambda event:credits1())
root.bind('<Control-d>',lambda event:changes())
root.bind('<Alt-l>',lambda event:Licence())
root.bind('<Alt-i>',lambda event:Popup())
root.bind('<Alt-k>',lambda event:KeyBindings())

root.bind('<Escape>',lambda event:root.quit())

mainloop()
