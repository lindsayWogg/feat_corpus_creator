from tkinter import *
from tkinter import ttk, messagebox
import sys
import mysql.connector
from PIL import Image, ImageTk
import pandas as pd
import os
import subprocess
from tkinter import PhotoImage
main_path=os.getcwd()
root = Tk()
##################taille de la fenetre##################
root.geometry("500x720+450+10")

#######################################################

root.wm_iconbitmap("")
root.title('')

full_canv = Canvas(root, bg='#FFF', highlightthickness=0)
full_canv.place(rely=0, relx=0, relwidth=1, relheight=1)

#bd781d
def updateWindow():
     try:
         if root.state() == "normal":
             root.xm_overideredirect(1)
     except:
         pass
     root.after(100, updateWindow)
     
updateWindow()

def minimizeWindow(event):
    root.overideredirect(0)
    root.iconify()

def reset():
                global entry_
                window = Tk()
                window.title("Fampitandremana")
                
                # Définir la taille de la fenêtre
                window.geometry("300x150")
            
                # Centrer la fenêtre sur l'écran
                screen_width = window.winfo_screenwidth()
                screen_height = window.winfo_screenheight()
            
                # Calculer les décalages x et y pour centrer la fenêtre
                x_offset = (screen_width - 300) // 2
                y_offset = (screen_height - 150) // 2
            
                # Définir les décalages x et y de la fenêtre
                window.geometry(f"+{x_offset}+{y_offset}")
            
                # Créer le texte
                text = Label(window, text=f"Ampidiro ny solon'anarana")
                text.pack()
                entry_= Entry(window,bg='white')
                entry_.pack(pady=10,ipady=4)
            
                # Créer les boutons
                button1 = Button(window, text="Ekena")
                button3 = Button(window, text="Hiverina")
            
                # Placer les boutons horizontalement
                button1.place(x=10, y=80)  
                button3.place(x=200, y=80)
             # Déclarez la variable value comme une variable de chaîne Tkinter
                # Définir les fonctions à exécuter lorsque les boutons sont cliqués
                def set_value1():
                   username=entry_.get()
                   if(username=='' or username==None):
                        window.destroy() 
                        messagebox.showerror("Fampitandremana", "Ampidiro ny solon'anaranao azafady...")
                   else:
                       window.destroy() 
                       delete_pwd(username)
            
                def set_value3():
                    window.destroy()
            
                # Assigner les fonctions aux boutons
                button1.config(command=set_value1)
                button3.config(command=set_value3)
            
                # Afficher la fenêtre
                window.mainloop()
def add():
                global entry_
                window = Tk()
                window.title("Famoronana kaonty")
                
                # Définir la taille de la fenêtre
                window.geometry("300x250")
            
                # Centrer la fenêtre sur l'écran
                screen_width = window.winfo_screenwidth()
                screen_height = window.winfo_screenheight()
            
                # Calculer les décalages x et y pour centrer la fenêtre
                x_offset = (screen_width - 300) // 2
                y_offset = (screen_height - 300) // 2
            
                # Définir les décalages x et y de la fenêtre
                window.geometry(f"+{x_offset}+{y_offset}")
            
                # Créer le texte
                text_1 = Label(window, text=f"Anarana")
                text_1.pack()
                entry_anarana= Entry(window,bg='white')
                entry_anarana.pack(pady=10,ipady=4)
                
                text_2 = Label(window, text=f"Fanampiny")
                text_2.pack()
                entry_fanampiny= Entry(window,bg='white')
                entry_fanampiny.pack(pady=10,ipady=4)
                
                text_3 = Label(window, text=f"Solon'anarana")
                text_3.pack()
                entry_usrname= Entry(window,bg='white')
                entry_usrname.pack(pady=10,ipady=4)
            
                # Créer les boutons
                button1 = Button(window, text="Ekena")
                button3 = Button(window, text="Hiverina")
            
                # Placer les boutons horizontalement
                button1.place(x=10, y=200)  
                button3.place(x=200, y=200)
             # Déclarez la variable value comme une variable de chaîne Tkinter
                # Définir les fonctions à exécuter lorsque les boutons sont cliqués
                def set_value1():
                   username=entry_usrname.get()
                   nom=entry_anarana.get()
                   prenom=entry_fanampiny.get()
                   if(username=='' or nom=='' or prenom==''):
                        window.destroy() 
                        messagebox.showerror("Fampitandremana", "Fenoy ny banga rehetra azafady...")
                   else:
                        window.destroy()
                        print(username,nom,prenom)
                        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
                        mycursor = mysqldb.cursor()
                        sql =f"select * from mpampiasa where solon_anarana='{username}'"
                        mycursor.execute(sql)
                        records = mycursor.fetchall()
                        print(records)
                        if records!=[]:
                            messagebox.showerror("Fampitandremana", f"Efa misy ny solon'anarana '{username}' tompoko.")
                        else:
                            requete=f"""INSERT INTO `mpampiasa`( `anarana`, `fanampiny`, `solon_anarana`, `teny_miafina`) VALUES ('{nom}','{prenom}','{username}','0000')"""
                            print('mbola tsy ao : ',requete)
                            mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
                            mycursor = mysqldb.cursor()
                            mycursor.execute(requete)
                            mysqldb.commit()
                            messagebox.showinfo("Tafiditra", f"Tontosa ny famoronana ny kaontinao. '0000' ny teny miafinao.")
                def set_value3():
                    window.destroy()
            
                # Assigner les fonctions aux boutons
                button1.config(command=set_value1)
                button3.config(command=set_value3)
            
                # Afficher la fenêtre
                window.mainloop()
def delete_pwd(username):
                global entry_
                window = Tk()
                window.title("Fampitandremana")
                
                # Définir la taille de la fenêtre
                window.geometry("300x100")
            
                # Centrer la fenêtre sur l'écran
                screen_width = window.winfo_screenwidth()
                screen_height = window.winfo_screenheight()
            
                # Calculer les décalages x et y pour centrer la fenêtre
                x_offset = (screen_width - 300) // 2
                y_offset = (screen_height - 150) // 2
            
                # Définir les décalages x et y de la fenêtre
                window.geometry(f"+{x_offset}+{y_offset}")
            
                # Créer le texte
                text = Label(window, text=f"Tinao fafana ve ny teny miafinao?")
                text.pack()
            
                # Créer les boutons
                button1 = Button(window, text="Fafàna")
                button3 = Button(window, text="Hiverina")
            
                # Placer les boutons horizontalement
                button1.place(x=20, y=40)  
                button3.place(x=190, y=40)
             # Déclarez la variable value comme une variable de chaîne Tkinter
                # Définir les fonctions à exécuter lorsque les boutons sont cliqués
                def set_value1():
                    print(username)
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
                    mycursor = mysqldb.cursor()
                    sql =f"select * from mpampiasa where solon_anarana='{username}'"
                    mycursor.execute(sql)
                    records = mycursor.fetchall()
                    if not records:
                        window.destroy()
                        messagebox.showerror("Fampitandremana", "Tsy misy ny solon'anarana nampidirinao...")
                    else:
                        window.destroy()
                        requete=f"UPDATE `mpampiasa` SET `teny_miafina`='0000' WHERE `solon_anarana`='{username}'; "
                        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
                        mycursor = mysqldb.cursor()
                        mycursor.execute(requete)
                        mysqldb.commit()
                        messagebox.showinfo("", "Voasolo ho '0000' ny teny miafinao!!!")
                def set_value3():
                    window.destroy()
            
                # Assigner les fonctions aux boutons
                button1.config(command=set_value1)
                button3.config(command=set_value3)
            
                # Afficher la fenêtre
                window.mainloop()
    
def login():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("Fampitandremana", "Azafady, fenoy daholo ny banga...")
    else:
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
        mycursor = mysqldb.cursor()
        username = usernameEntry.get()
        password = passwordEntry.get()
        sql ="select * from mpampiasa where solon_anarana=%s and teny_miafina=%s"
        val = (username, password)
        mycursor.execute(sql,val)
        records = mycursor.fetchall()
        print("ITO EE",records)
        
        a = records
        session=pd.DataFrame(columns=['id','anarana','fanampiny','solon_anarana','teny_miafina'])
        if not records:
            messagebox.showerror("Fampitandremana", "Diso ny solon anarana na ny teny miafina...")
        else:
            user_logged={'id':f'{a[0][0]}','anarana':f'{a[0][1]}','fanampiny':f'{a[0][2]}','solon_anarana':f'{a[0][3]}','teny_miafina':f'{a[0][4]}'}
            session=session.append(user_logged,ignore_index=True)
            print(f'main path: {main_path}')
            session.to_parquet(main_path+r'/Session/session.parquet',compression='gzip')
            print(session)
            messagebox.showinfo("", "Tafiditra ianao")
            root.destroy()   
            subprocess.run(["python", "Scripts/app.py"])
clos_nav = Canvas(full_canv, bg="#1f1f3a", highlightthickness=0)
clos_nav.place(rely=0, relx=0, relwidth=1, height=35)

title_label = Label(clos_nav, bg="#1f1f3a", fg="#ffffff", text="Famoronana corpus hoan ny teny Malagasy", font=("Cambria", 13))
title_label.pack(side=LEFT, padx=7)

root.update_idletasks()

mainCanvas = Canvas(root, bg="#FFF", highlightthickness=0)
mainCanvas.place(y=35, relx=0, relheight=(root.winfo_height() - 35) / root.winfo_height(), relwidth=1)

logo_canv = Canvas(mainCanvas, highlightthickness=0, bg="#FFF")
logo_canv.place(y=50, relx=0.3, relwidth=0.4, relheight=0.3)

logo_canv.update_idletasks()
#logo_img = ImageTk.PhotoImage(Image.open("./assets/MUTLOGO.png"))
image = PhotoImage(file=r"./assets/asja_logo_officiel.png")
image = image.subsample(10, 10) # redimensionne l'image
label = Label(root, image=image)

bottom_canvas = Canvas(mainCanvas, highlightthickness=0, bg="#FFFFFF")
bottom_canvas.place(y=logo_canv.winfo_height()+ 100, relx=0, relwidth=1, relheight=0.7)
label.pack(side=TOP,pady=40)
style = ttk.Style(root)
style.theme_use("clam")

usernameLbl = Label(bottom_canvas, background="#fff", foreground="#2b2b2b", text="Solon'anarana", font=("Cambria", 14))
usernameLbl.pack(side=TOP)

usernameEntry = ttk.Entry(bottom_canvas, justify=CENTER, font=("Cambria", 16))
usernameEntry.pack(side=TOP, pady=10, ipady=4, ipadx=4)


passwordLbl = Label(bottom_canvas, background="#fff", foreground="#2b2b2b", text="Teny miafina", font=("Cambria", 14))
passwordLbl.pack(side=TOP)

passwordEntry = ttk.Entry(bottom_canvas, justify=CENTER, font=("Cambria", 16),show="*")
passwordEntry.pack(side=TOP, pady=10, ipady=4, ipadx=4)

loginBtn = Button(bottom_canvas, text="Hiditra", relief=FLAT, font=("Cambria", 15), background="#1f1f3a", foreground="lime", command=login)
loginBtn.pack(side=TOP, ipadx=90, ipady=4, pady=15)

resetBtn = Button(bottom_canvas, text="Hadino ny teny miafina", relief=FLAT, font=("Cambria", 12), background="#1f1f3a", foreground="lime", command=reset)
resetBtn.pack(side=TOP, ipadx=15, ipady=4, pady=15)

addBtn = Button(bottom_canvas, text="+", relief=FLAT, font=("Cambria", 12), background="#1f1f3a", foreground="lime", command=add)
addBtn.pack(side=TOP, ipadx=15, ipady=4, pady=15)


root.mainloop()