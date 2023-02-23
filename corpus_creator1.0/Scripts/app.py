from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import cv2
import os
import pytesseract
from PIL import Image
import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.probability import FreqDist
import pandas as pd
import mysql.connector
from tkinter import filedialog 
from backend import *
from tkinter import PhotoImage
from tkinter import messagebox
import re
import string
def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)
w=Tk()
#debut test
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
window_width = 900
window_height = 500
x_coordinate = (screen_width/2) - (window_width/2)
y_coordinate = (screen_height/2) - (window_height/2)
w.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))
#fin test
#w.geometry('900x500')
w.configure(bg='#262626')#12c4c0')
w.resizable(0,0)
w.title('Famoronana Corpus')
global entry_teny
global entry_sokajy
global var
main_path=os.getcwd()
text_directory=main_path+'/Texts/'
def default_home():
    #f1.destroy()
    f2=Frame(w,width=900,height=455,bg='#262626')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Tongasoa ato amin ny fanaovana corpus.' ,fg='white',bg='#262626')
    l2.config(font=('Comic Sans MS',20))
    l3=Label(f2,text='<< Andrianiko ny teniko. >>')
    l3.config(font=('Comic Sans MS',20))
    l3.place(x=290,y=200)
    l2.place(x=290,y=150-45)
    l3.place(x=290,y=200)
    #toggle_win()

   
def home():
    f1.destroy()
    f2=Frame(w,width=900,height=455,bg='#262626')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Tongasoa ato amin ny fanaovana corpus' ,fg='white',bg='#262626')
    l2.config(font=('Comic Sans MS',20))
    l2.place(x=290,y=150-45)
    l3=Label(f2,text='<< Andrianiko ny teniko. >>',fg='white',bg='#262626')
    l3.config(font=('Comic Sans MS',20))
    l3.place(x=290,y=200)
    toggle_win()

def browseFiles(): 
    fichier = filedialog.askopenfilename(initialdir = "/home",title = "Select a File",filetypes = (("Image files", "*.png*"),("all files","*.*"))) 
    #Chemin.configure(text=fichier)
    nom_image.insert(0,fichier)
    t.delete(1.0, END)
    return fichier

def ocr():
    global nom_image
    #global Sortie
    global t
    global Bouton2
    global titre1,label_titre
    f1.destroy()
    f2=Frame(w,width=900,height=500)
    f2.place(x=0,y=0)
    l2=Label(f2,text='Fisintonana lahatsoratra avy ao anatin ny sary',fg='black')
    l2.config(font=('Comic Sans MS',12))
    l2.place(x=200,y=10)
    label_ocr = Label(f2, text='Ampidiro ny anaran ny sary : ')
    label_ocr.config(font=('Comic Sans MS',12))
    label_ocr.place(x=20, y=80)
    nom_image = Entry(f2, bg="white", highlightcolor="green")
    nom_image.place(x=100, y=110, width=230, height=30)
    Bouton_select_fichier = Button(w,text = "Hisafidy",command = browseFiles) 
    Bouton_select_fichier.place(x=10, y=110)
    Bouton = Button(f2, text="Ekena >>", command=reconnaissance)
    Bouton.place(x=10, y=150)
    label_text = Label(f2, text='Mivoaka eto ny lahatsoratra azo : ')
    label_text.config(font=('Comic Sans MS',12))
    label_text.place(x=500, y=80)
    ligne = Frame(f2, bg='black')
    ligne.place(x=340, y=80, width=3, height=400)
    champ = Frame(f2, bg='white')
    champ.place(x=350, y=110, width=545, height=330)
    Bouton2 = Button(f2, text="Rasaina >>", command=tokenisation)
    label_titre=Label(f2,text="Lohateny : ")
    titre1=Entry(f2,bg="white")
    #Sortie = Message(champ, bg='green')
    #Sortie.place(x=5, y=5, width=535, height=320)
    t = Text(champ, bg='white', width=530)
    t.place(x=5, y=5, width=535, height=320)
    toggle_win()
    return nom_image
def gestion_password():
    global entry_old_pwd
    global entry_new1_pwd
    global entry_new2_pwd
    f1.destroy()
    f2=Frame(w,width=900,height=500)
    f2.place(x=0,y=0)
    a=60
    police=11
    session=pd.read_parquet(main_path+r'/Session/session.parquet')
    for x,y in session.iterrows():
        id=y['id']
        anarana=y['anarana']
        fanampiny=y['fanampiny']
        solon_anarana=y['solon_anarana']
        teny_miafina=y['teny_miafina']
    #
    #separation
    ligne = Frame(f2, bg='black')
    ligne.place(x=340, y=80, width=3, height=400)
    #
    l2=Label(f2,text='Indro ny momba ny mpampiasa:',fg='black')
    l2.config(font=('',12))
    section_label=Label(f2,text='Ireo momba anao:')
    section_label.config(font=('',police))
    label_nom=Label(f2,text="Anarana: "+anarana)
    entry_nom=Entry(f2,bg='white',state="readonly")
    label_nom.config(font=("",police))
    label_prenom=Label(f2,text="Fanampiny: "+fanampiny)
    label_prenom.config(font=("",police))
    label_username=Label(f2,text="Solon'anarana: "+solon_anarana)
    label_username.config(font=("",police))
    label_pwd=Label(f2,text="Teny miafina: "+"".join(["*" for c in teny_miafina]))
    label_pwd.config(font=("",police))
    #section update
    edition_label=Label(f2,text='Hanova teny miafina:')
    edition_label.config(font=('',police))
    label_old_pwd=Label(f2,text='Teny miafina taloha: ')
    entry_old_pwd=Entry(f2,show='*')
    label_new1_pwd=Label(f2,text='Teny miafina vaovao: ')
    entry_new1_pwd=Entry(f2,show='*')
    label_new2_pwd=Label(f2,text='Hamarino: ')
    entry_new2_pwd=Entry(f2,show='*')
    Btn=Button(f2,text='Hovaina',command=update)    
    l2.place(x=200,y=10)
    distance=a+20
    section_label.place(x=20, y=distance)
    edition_label.place(x=400, y=distance)
    distance=distance+a
    label_nom.place(x=10, y=distance)
    label_old_pwd.place(x=400, y=distance)
    entry_old_pwd.place(x=550, y=distance-5,width=200, height=25)
    entry_nom.insert(0, anarana)
    distance=distance+a
    label_prenom.place(x=10, y=distance)
    label_new1_pwd.place(x=400, y=distance)
    entry_new1_pwd.place(x=550, y=distance-5,width=200, height=25)
    distance=distance+a
    label_username.place(x=10, y=distance)
    label_new2_pwd.place(x=400, y=distance)
    entry_new2_pwd.place(x=550, y=distance-5,width=200, height=25)
    distance=distance+a
    label_pwd.place(x=10, y=distance)  
    Btn.place(x=550, y=distance-5,width=200, height=25)
    toggle_win()

   
def update():
            global entry_old_pwd
            global entry_new1_pwd
            global entry_new2_pwd
            if(entry_old_pwd.get()=='' or entry_new2_pwd.get()=='' or entry_new2_pwd.get()==''):
                    messagebox.showerror("Fampitandremana", "Azafady, fenoy ny banga rehetra!!!")
            else:
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
                text = tk.Label(window, text=f"Tianao soloina ve ny teny miafina?")
                text.pack(pady=20)
            
                # Créer les boutons
                button1 = tk.Button(window, text="Eny")
                button2 = tk.Button(window, text="Tsia")
                button3 = tk.Button(window, text="Hiverina")
            
                # Placer les boutons horizontalement
                button1.place(x=10, y=80)  # Ajouter une marge en haut des boutons
                button2.place(x=110, y=80)
                button3.place(x=200, y=80)
             # Déclarez la variable value comme une variable de chaîne Tkinter
            
                # Définir les fonctions à exécuter lorsque les boutons sont cliqués
                def set_value1(): # Utilisez la méthode set() de Tkinter pour mettre à jour la valeur de value
                    session=pd.read_parquet(main_path+r'/Session/session.parquet')    
                    for x,y in session.iterrows():
                        id=y['id']
                        anarana=y['anarana']
                        fanampiny=y['fanampiny']
                        solon_anarana=y['solon_anarana']
                        teny_miafina=y['teny_miafina']
                    old_pwd=entry_old_pwd.get()
                    if(old_pwd==teny_miafina):
                        if(entry_new1_pwd.get()==entry_new2_pwd.get()):
                            requete=f"UPDATE `mpampiasa` SET `teny_miafina`='{entry_new2_pwd.get()}' WHERE `id`='{id}'; "
                            mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
                            mycursor = mysqldb.cursor()
                            mycursor.execute(requete)
                            mysqldb.commit()
                            session=pd.DataFrame(columns=['id','anarana','fanampiny','solon_anarana','teny_miafina'])
                            user_logged={'id':f'{id}','anarana':f'{anarana}','fanampiny':f'{fanampiny}','solon_anarana':f'{solon_anarana}','teny_miafina':f'{entry_new1_pwd.get()}'}
                            session=session.append(user_logged,ignore_index=True)
                            print(f'main path: {main_path}')
                            session.to_parquet(main_path+r'/Session/session.parquet',compression='gzip')
                            window.destroy()
                            messagebox.showinfo("", "Voasolo soamantsara ny teny miafina")
                            print(session)
                        else:
                            messagebox.showerror("Fampitandremana", "Azafady, hamarino ny teny miafina vaovao!!!")
                    else:
                        messagebox.showerror("Fampitandremana", "Azafady, diso ny teny miafina taloha!!!")
                    window.destroy()
                def set_value2():
                    window.destroy()
            
                def set_value3():
                    window.destroy()
            
                # Assigner les fonctions aux boutons
                button1.config(command=set_value1)
                button2.config(command=set_value2)
                button3.config(command=set_value3)
            
                # Afficher la fenêtre
                window.mainloop()
def reconnaissance():
    global nom_image
    global Sortie
    global t
    global text
    global Bouton2
    global titre1,label_titre
    im = cv2.imread(nom_image.get())
    nom_image.delete(0,END)
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(imgray, 128, 255, cv2.THRESH_BINARY)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, thresh1)
    img = Image.open(filename)
    text = pytesseract.image_to_string(img)
    label_titre.place(x=10,y=200)
    titre1.place(x=100, y=195, width=230, height=30)
    Bouton2.place(x=620, y=450)
    #Sortie.configure(text="Voici le texte exporté : \n"+text)
    t.insert(END, text)
    return text

def tokenisation():
    global text
    global t
    titre=titre1.get()
    import_text(titre,text)
    #print(t.get(END))
    print("##########TOKENISATION EN PHRASE#########""")
    print(nltk.sent_tokenize(text))
    print("##########TOKENISATION EN MOT#########""")
    text = nltk.word_tokenize(text) 
    print(text)
    df = pd.DataFrame({'text':text})
    text = df['text'].apply(lambda x:"".join(re.findall(r'[a-zA-Z+" "]', x)))#enlever ponctuation
    print("#####################-ENLEVER PONCTUATIONS-#######################")
    print(text)
     #debut bag of words
    new_list = []
    for i in text :
        if i not in new_list:
            new_list.append(i)
    print("#####################-BAG OF WORDS-#######################")
    print(new_list)
    #fin bag of words
    print("#####################-INSERTION DES MOTS DANS LA BAS DE DONNÉES-#######################")
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT teny FROM teny")
    records = mycursor.fetchall()
    print(records)
    for i in new_list:
        if i not in records:
            print("mbola tsy ao ny : "+i)
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
            mycursor = mysqldb.cursor()
            try:
                sql ="INSERT INTO teny (teny, sokajy) VALUES (%s, %s)"
                val = (i,0)
                if(i!=''):
                    mycursor.execute(sql, val)
                    mysqldb.commit()
                    lastid = mycursor.lastrowid
            except Exception as e:
                print(e)
                print("efa ao ny : "+i)
                mysqldb.rollback()
                mysqldb.close()
        else:
            print("efa ao ny : "+i)

def get_content_corpus(event): #récupérer path
    global listBox
    global text_saisi
    global path
    #entry_teny.delete(0,END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    print('title::::::',select['Lohateny'])
    print('cat::::::',select['sokajy'])
    titre=select['Lohateny']
    categorie=select['sokajy']
    print(titre,categorie)
    df_corpus_selected=pd.DataFrame(columns=(['titre']))
    mycursor.execute(f"SELECT `path` FROM `corpus` WHERE `status`='1' and `titre`='{titre}'")
    text=mycursor.fetchall()
    path=text[0][0]
    print('::::::>',text[0])
    with open(f'{text[0][0]}') as file:
        content=file.read()
    print(content)
    df_corpus_selected.loc[len(df_corpus_selected)]=[titre]
    df_corpus_selected.to_csv(main_path+'\\     temp_file.txt')
    df_corpus_selected.to_parquet(main_path+'\\temp_id.parquet',compression='gzip')
    df = pd.DataFrame(columns=["Path"])
    current_file={'Path':f'{text[0][0]}'}
    df.append(current_file,ignore_index=True)
    df.to_parquet(main_path+r'/cache/corp_temp.parquet',compression='gzip')
    text_saisi.delete(1.0, END)
    text_saisi.insert(END, content)

def list_corpus():
    global listBox,text_saisi
    global var
    f1.destroy()
    f2=Frame(w,width=900,height=500)
    f2.place(x=0,y=0)
    l2=Label(f2,text='Lisitry ny \'CORPUS\'',fg='black')
    l2.config(font=('Comic Sans MS',12))
    l2.place(x=320,y=20)
    l3=Label(f2,text='Lahatsoratra : ',fg='black')
    l3.place(x=620,y=80)
    cols = ('Lohateny','sokajy')
    listBox = ttk.Treeview(f2, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=1)
        listBox.place(x=10, y=80, height=400)
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT `id`, `titre`, `categorie` FROM `corpus` WHERE `status`='1'")
    records = mycursor.fetchall()
    for i, (id,titre,categorie) in enumerate (records, start=1):
        listBox.insert("", "end", values=(titre,categorie))
        mysqldb.close()
    listBox.bind('<Double-Button-1>', get_content_corpus)
    text_saisi = Text(f2, bg="white", highlightcolor="green")
    text_saisi.place(x=450, y=110,width=430, height=300)
    Bouton2 = Button(f2, text="Sokajin-teny >>", command=bag_of_words)
    Bouton2.place(x=680, y=450)
    Bouton3 = Button(f2, text="<< Fafàna", command=traiter_texte)
    Bouton3.place(x=550, y=450)
    toggle_win()
def remove_punctuation_and_numbers(text):
    import string
    text_without_punctuation = text.translate(str.maketrans("", "", string.punctuation + string.digits))
    return text_without_punctuation

def bag_of_words():
    global text
    global text_saisi
    global path
    text = text_saisi.get("1.0","end")
    print(f'texte:::::::{text}')
    text = remove_punctuation_and_numbers(text)
    tokens = nltk.wordpunct_tokenize(text)
    print('TOKENS: ',tokens)
    #recupérer liste des mots
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
    mycursor = mysqldb.cursor()
    classed_word=[]
    for word in tokens:
        requete=f"select teny,sokajy from teny where teny ='{word}' and voasokajy=1"
        mycursor.execute(requete)
        mots_classed=mycursor.fetchall()
        print(mots_classed)
        classed_word.append(mots_classed)
    print(classed_word)
    result = [item for sublist in classed_word for item in sublist if item]
    #print([i.replace("'", "").replace("(", "").replace(")", "") for i in classed_word])
    # Construction de la statistique des mots
    fdist = FreqDist(tokens)
    
    # Affichage des 10 mots les plus fréquents
    #print(fdist.most_common(10))
    
    # Affichage de la fréquence du mot "text"
    #print('fdist["text"]:::',fdist["text"])
    
    # Affichage de la longueur du vocabulaire (nombre de mots uniques)
    print('len(fdist):::',len(fdist))
    print(path)
    final_result=f"""
    ******TOERANA MISY NY LAHATSORATRA******
    {path}
    
    ***********IREO SOKAJIN-TENY************
    {result}
    
    
    ***TENY 10 VOALOHANY MIVERINA MATETIKA***
    {fdist.most_common(10)}
    """
    text_saisi.delete(1.0, END)
    text_saisi.insert(END, final_result)
    print(final_result)
    return text

def list_text():
    global listBox,text_saisi
    global var,entry_sokajy
    f1.destroy()
    f2=Frame(w,width=900,height=500)
    f2.place(x=0,y=0)
    l2=Label(f2,text='Fanasokajian-dahatsoratra',fg='black')
    l2.config(font=('Comic Sans MS',12))
    l2.place(x=320,y=20)
    l3=Label(f2,text='Lahatsoratra : ',fg='black')
    l3.place(x=620,y=80)
    cols = ('Laharana','Lohateny')
    listBox = ttk.Treeview(f2, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=1)
        listBox.place(x=10, y=80, height=400)
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT `id`, `titre` FROM `corpus` WHERE `status`='0'")
    records = mycursor.fetchall()
    for i, (id,titre) in enumerate (records, start=1):
        listBox.insert("", "end", values=(id, titre))
        mysqldb.close()
    listBox.bind('<Double-Button-1>', get_content_text)
    text_saisi = Text(f2, bg="white", highlightcolor="green")
    text_saisi.place(x=450, y=110,width=430, height=270)
    l4=Label(f2,text='Sokajy : ',fg='black')
    l4.place(x=525,y=400)
    entry_sokajy = Entry(f2,bg='white')
    entry_sokajy.place(x=620, y=400, height=25)
    Bouton2 = Button(f2, text="Sokajiana >>", command=classer_corpus)
    Bouton2.place(x=680, y=450)
    Bouton3 = Button(f2, text="<< Fafàna", command=delete_content)
    Bouton3.place(x=550, y=450)
    toggle_win()
    
    #def Delete(event):
    #global listBox
    #global entry_teny
    ##entry_teny.delete(0,END)
    #row_id = listBox.selection()[0]
    #select = listBox.set(row_id)
   # entry_teny.insert(0, select['Teny'])
def classer_corpus():###classification des corpus non classés
    global text_saisi,entry_sokajy
    import mysql.connector
    #from config import *
    text = text_saisi.get("1.0","end")
    texte= remove_punctuation(text)
    print(text)
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
    mycursor = mysqldb.cursor()
    requete='select teny from teny where voasokajy=1'
    mycursor.execute(requete)
    liste_mots_classed=mycursor.fetchall()
    classed_word=[]
    for a in liste_mots_classed:
        classed_word.append(str(a[0].lower()))
    print(f'word classed:{liste_mots_classed}')
    print(f'contenu :{text}')
   # text = nltk.wordpunct_tokenize(text) 
    punct_tokenizer = nltk.WordPunctTokenizer()
    tokens = punct_tokenizer.tokenize(text)
    text = [token for token in tokens if token.isalnum()]
    print('filtered text:',text)
    word_non_classed=[]
    classement=True
    sokajy=entry_sokajy.get()
    for i in text:
        if i.lower() in classed_word:     
            print('ao zany')
        else:
            classement=False
            word_non_classed.append(str(i))
            print('tsy ao zany')
    if(classement==True):
        if(sokajy!=None and sokajy!=''):
            df_id=pd.read_parquet(main_path+'\\temp_id.parquet')
            for x,y in df_id.iterrows():
                id=y['id']
            #result = messagebox.askyesno("Question", "Do you want to save your changes?", icon='warning', yesbutton='Eny', nobutton='Tsia')
            #############################################################################"
            global value
            # Créer la fenêtre principale
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
            text = tk.Label(window, text=f"Tena sokajiana ve ity lahatsoratra ity?")
            text.pack(pady=20)
        
            # Créer les boutons
            button1 = tk.Button(window, text="Eny")
            button2 = tk.Button(window, text="Tsia")
            button3 = tk.Button(window, text="Hiverina")
        
            # Placer les boutons horizontalement
            button1.place(x=10, y=80)  # Ajouter une marge en haut des boutons
            button2.place(x=110, y=80)
            button3.place(x=200, y=80)
         # Déclarez la variable value comme une variable de chaîne Tkinter
        
            # Définir les fonctions à exécuter lorsque les boutons sont cliqués
            def set_value1(): # Utilisez la méthode set() de Tkinter pour mettre à jour la valeur de value
                window.destroy()
                mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
                mycursor = mysqldb.cursor()
                print('le corpus peut etre classee')
                requete=f"UPDATE `corpus` SET `categorie`='{entry_sokajy.get()}',`status`='1' WHERE `id`='{id}'"
                try:
                    # execute update query
                    mycursor.execute(requete)
                    mysqldb.commit()
                except mysql.connector.Error as error:
                    print("Error: {}".format(error))
                finally:
                    mysqldb.close()
                list_text
                print(requete)
                messagebox.showerror("Voasokajy", "Voasokajy soamantsara ny lahatsoratra!!!")
            def set_value2():
                window.destroy()
        
            def set_value3():
                window.destroy()
        
            # Assigner les fonctions aux boutons
            button1.config(command=set_value1)
            button2.config(command=set_value2)
            button3.config(command=set_value3)
        
            # Afficher la fenêtre
            window.mainloop()
            ##############################################################################"
        else:
            messagebox.showerror("fampitandremana", "Fenoy ny sokajy azafady!!!")
    else:
        print('classement impossible')
        text_saisi.delete(1.0, END)
        messagebox.showerror("fampitandremana", "Fenoy ny sokajy azafady!!!")
def delete_content():
            global listBox
            global text_saisi
    #############################################################################"
            global value
            # Créer la fenêtre principale
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
            text = tk.Label(window, text=f"Tianao fafàna ve ity lahatsoratra ity?")
            text.pack()
        
            # Créer les boutons
            button1 = tk.Button(window, text="Eny")
            button2 = tk.Button(window, text="Tsia")
            button3 = tk.Button(window, text="Hiverina")
        
            # Placer les boutons horizontalement
            button1.place(x=10, y=80)  # Ajouter une marge en haut des boutons
            button2.place(x=110, y=80)
            button3.place(x=200, y=80)
         # Déclarez la variable value comme une variable de chaîne Tkinter
        
            # Définir les fonctions à exécuter lorsque les boutons sont cliqués
            def set_value1(): # Utilisez la méthode set() de Tkinter pour mettre à jour la valeur de value
                window.destroy()
                text_saisi.delete(1.0, END)
                row_id = listBox.selection()[0]
                select = listBox.set(row_id)
                print('id::::::',select['Laharana'])
                id=select['Laharana']
                df_corpus_selected=pd.DataFrame(columns=(['id']))
                mycursor.execute(f"DELETE FROM `corpus` WHERE `id`='{id}'")
                mysqldb.commit()
                
            def set_value2():
                window.destroy()
        
            def set_value3():
                window.destroy()
        
            # Assigner les fonctions aux boutons
            button1.config(command=set_value1)
            button2.config(command=set_value2)
            button3.config(command=set_value3)
        
            # Afficher la fenêtre
            window.mainloop()
            
            ##############################################################################"
    
def get_content_text(event): #récupérer path
    global listBox
    global text_saisi
    #entry_teny.delete(0,END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    print('id::::::',select['Laharana'])
    id=select['Laharana']
    df_corpus_selected=pd.DataFrame(columns=(['id']))
    mycursor.execute(f"SELECT `path` FROM `corpus` WHERE `status`='0' and `id`='{id}'")
    text=mycursor.fetchall()
    print('::::::>',text[0])
    with open(f'{text[0][0]}') as file:
        content=file.read()
    print(content)
    df_corpus_selected.loc[len(df_corpus_selected)]=[id]
    df_corpus_selected.to_csv(main_path+'\\     temp_file.txt')
    df_corpus_selected.to_parquet(main_path+'\\temp_id.parquet',compression='gzip')
    text_saisi.delete(1.0, END)
    text_saisi.insert(END, content)
    
def mots_classed():
    global listBox
    global var
    f1.destroy()
    f2=Frame(w,width=900,height=500)
    f2.place(x=0,y=0)
    l2=Label(f2,text='Fanasokajina teny',fg='black')
    l2.config(font=('Comic Sans MS',12))
    l2.place(x=320,y=20)
    cols = ('Laharana','Teny', 'Sokajy')
    listBox = ttk.Treeview(f2, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=1)
        listBox.place(x=10, y=80, height=400)
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,teny,sokajy FROM teny WHERE voasokajy=1 ORDER BY teny")
    records = mycursor.fetchall()
    for i, (id,teny,sokajy) in enumerate (records, start=1):
        listBox.insert("", "end", values=(id, teny, sokajy))
        mysqldb.close()
    listBox.bind('<Double-Button-1>', Delete)
    label_teny = Label(f2, text='Teny : ')
    label_teny.place(x=650, y=100)
    label_sokajy = Label(f2, text='Sokajy: ')
    label_sokajy.place(x=650, y=150)
    global entry_teny
    global cb1
    global curr_var
    entry_teny = Entry(f2)
    entry_teny.place(x=700, y=95, height=25)
    curr_var= StringVar()
    sokajy=['Matoanteny','Tambinteny','Anarana','Mpamaritra','Mpisolo','Mpanoritra','Mpampiankin-teny','Mpampitohy fehezan-teny','Mpampitohy','Tenim-piontanana','Kian-teny'] # options
    cb1 = ttk.Combobox(f2, values=sokajy,width=7,textvariable=curr_var)
    cb1.place(x=700, y=145, height=25, width=145)
    cb1.set('Matoanteny')
    supprimer = Button(f2, text='<< Esorina', command=Supprimer_mot_non_classed)
    supprimer.place(x=625, y=200)
    Modifier = Button(f2, text='Ovaina >>', command=update_classement)
    Modifier.place(x=745, y=200)
    toggle_win()
    
def update_classement():
    global entry_teny
    global cb1
    global curr_var
    teny = entry_teny.get()
    sokajy = curr_var.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
    mycursor = mysqldb.cursor()    
    try:
        sql = "UPDATE teny SET sokajy=%s,voasokajy=%s WHERE teny=%s"
        val = (sokajy, 1, teny)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo ("information","Voasokajy soamantsara.....")
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
    mots_classed()
def classement_mots():
    global listBox
    global var
    f1.destroy()
    f2=Frame(w,width=900,height=500)
    f2.place(x=0,y=0)
    l2=Label(f2,text='Fanasokajina teny',fg='black')
    l2.config(font=('Comic Sans MS',12))
    l2.place(x=320,y=20)
    cols = ('Laharana','Teny')
    listBox = ttk.Treeview(f2, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=1)
        listBox.place(x=10, y=80, height=400)
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,teny FROM teny WHERE voasokajy=0 ORDER BY teny")
    records = mycursor.fetchall()
    for i, (id,teny) in enumerate (records, start=1):
        listBox.insert("", "end", values=(id, teny))
        mysqldb.close()
    listBox.bind('<Double-Button-1>', Delete)
    CHOIX = ["oui", "non", "peut-être"]
    var = StringVar()
    classe1 = Radiobutton(f2, text="Matoanteny", variable=var, value="Matoanteny", command=sel)
    classe1.place(x=450, y=100)
    classe2 = Radiobutton(f2, text="Tambinteny", variable=var, value="Tambinteny", command=sel)
    classe2.place(x=450, y=150)
    classe3 = Radiobutton(f2, text="Anarana", variable=var, value="Anarana", command=sel)
    classe3.place(x=450, y=200)
    classe4 = Radiobutton(f2, text="Mpamaritra", variable=var, value="Mpamaritra", command=sel)
    classe4.place(x=450, y=250)
    classe5 = Radiobutton(f2, text="Mpisolo", variable=var, value="Mpisolo", command=sel)
    classe5.place(x=550, y=100)
    classe6 = Radiobutton(f2, text="Mpanoritra", variable=var, value="Mpanoritra", command=sel)
    classe6.place(x=550, y=150)
    classe7 = Radiobutton(f2, text="Mpampiankin-teny", variable=var, value="Mpampiankin-teny", command=sel)
    classe7.place(x=550, y=200)
    classe8 = Radiobutton(f2, text="Mpampitohy fehezan-teny", variable=var, value="Mpampitohy fehezan-teny", command=sel)
    classe8.place(x=550, y=250)   
    classe9 = Radiobutton(f2, text="Mpampitohy", variable=var, value="Mpampitohy", command=sel)
    classe9.place(x=690, y=100)
    classe10 = Radiobutton(f2, text="Tenim-piontanana", variable=var, value="Tenim-piontanana", command=sel)
    classe10.place(x=690, y=150)
    classe11 = Radiobutton(f2, text="Kian-teny", variable=var, value="Kian-teny", command=sel)
    classe11.place(x=690, y=200)
    label_teny = Label(f2, text='Teny : ')
    label_teny.place(x=450, y=300)
    label_sokajy = Label(f2, text='Sokajy: ')
    label_sokajy.place(x=450, y=350)
    global entry_teny
    global entry_sokajy
    entry_teny = Entry(f2)
    entry_teny.place(x=500, y=295, height=25)
    entry_sokajy = Entry(f2)
    entry_sokajy.place(x=503, y=345, height=25)
    classer = Button(f2, text='Sokajiana >>', command=classer_mot)
    classer.place(x=600, y=400)
    supprimer = Button(f2, text='<< Esorina', command=Supprimer_mot_non_classed)
    supprimer.place(x=500, y=400)
    toggle_win()
    
def classer_mot():
    global entry_teny
    global entry_sokajy
    teny = entry_teny.get()
    sokajy = entry_sokajy.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
    mycursor = mysqldb.cursor()    
    try:
        sql = "UPDATE teny SET sokajy=%s,voasokajy=%s WHERE teny=%s"
        val = (sokajy, 1, teny)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo ("information","Voasokajy soamantsara.....")
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
    classement_mots()
def Supprimer_mot_non_classed():
    global entry_teny
    teny = entry_teny.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
    mycursor = mysqldb.cursor()
    try:
        sql = "DELETE FROM teny WHERE teny=%s"
        val = (teny,)
        mycursor.execute(sql,val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo ("information","Record deleted successfully.....")
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
        
def Delete(event):
    global listBox
    global entry_teny
    entry_teny.delete(0,END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    entry_teny.insert(0, select['Teny'])
    
def sel():
    global listBox
    global var
    global entry_sokajy
    entry_sokajy.delete(0,END)
    entry_sokajy.insert(0, var.get())
    print(str(var.get()))
    

    
def entrer_texte():
    global text_saisi
    global titre1,label_titre
    f1.destroy()
    f2=Frame(w,width=900,height=500)
    f2.place(x=0,y=0)
    l2=Label(f2,text='Fampidirana lahatsoratra',fg='black')
    l2.config(font=('Comic Sans MS',12))
    l2.place(x=320,y=20)
    label_indic = Label(f2, text='Ampidiro etsy ambany ny lahatsoratra : ')
    label_indic.config(font=('Comic Sans MS',12))
    label_indic.place(x=20, y=80)
    text_saisi = Text(f2, bg="white", highlightcolor="green")
    text_saisi.place(x=20, y=110, height=350)
    Bouton2 = Button(f2, text="Rasaina >>", command=traiter_texte)
    Bouton2.place(x=320, y=470)
    label_titre=Label(f2,text="Lohateny : ")
    titre1=Entry(f2,bg="white")
    label_titre.place(x=600,y=85)
    titre1.place(x=690, y=80, width=200, height=30)
    toggle_win()

def traiter_texte():
    global text
    global text_saisi
    text = text_saisi.get("1.0","end")
    tokenisation()
    messagebox.showinfo("Tafiditra", f"Tafiditra ary voarasa soamantsara ny lahatsoratra.")
    return text

def quiter():
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
            text = tk.Label(window, text=f"Tena hiala tokoa ve ianao?")
            text.pack(pady=25)
        
            # Créer les boutons
            button1 = tk.Button(window, text="Eny")
            button2 = tk.Button(window, text="Tsia")
            button3 = tk.Button(window, text="Hiverina")
        
            # Placer les boutons horizontalement
            button1.place(x=10, y=80)  # Ajouter une marge en haut des boutons
            button2.place(x=110, y=80)
            button3.place(x=200, y=80)
         # Déclarez la variable value comme une variable de chaîne Tkinter
        
            # Définir les fonctions à exécuter lorsque les boutons sont cliqués
            def set_value1(): # Utilisez la méthode set() de Tkinter pour mettre à jour la valeur de value
                window.destroy()
                delete_session()
                w.destroy()
                
            def set_value2():
                window.destroy()
        
            def set_value3():
                window.destroy()
        
            # Assigner les fonctions aux boutons
            button1.config(command=set_value1)
            button2.config(command=set_value2)
            button3.config(command=set_value3)
        
            # Afficher la fenêtre
            window.mainloop()
            
    
def toggle_win():
    global f1
    f1=Frame(w,width=300,height=500,bg='#12c4c0')
    f1.place(x=0,y=0)
    
    #buttons
    def bttn(x,y,text,bcolor,fcolor,cmd):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#262626'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#262626'

        myButton1 = Button(f1,text=text,
                       width=42,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

    bttn(0,80,'Tranokala','#0f9d9a','#12c4c0',home)
    bttn(0,117,'Haka lahatsoratra avy @ sary','#0f9d9a','#12c4c0',ocr)
    bttn(0,154,'Hampiditra lahatsoratra','#0f9d9a','#12c4c0',entrer_texte)
    bttn(0,191,'Fanasokajiana teny','#0f9d9a','#12c4c0',classement_mots)
    bttn(0,228,'Teny voasokajy','#0f9d9a','#12c4c0',mots_classed)
    bttn(0,265,'Lahatsoratra tsy voasokajy','#0f9d9a','#12c4c0',list_text)
    bttn(0,302,'Lahatsoratra voasokajy','#0f9d9a','#12c4c0',list_corpus)
    bttn(0,339,'Teny miafina','#0f9d9a','#12c4c0',gestion_password)
    bttn(0,376,'Hiala','#0f9d9a','#12c4c0',quiter)
    #
    def dele():
        f1.destroy()
        b2=Button(w,image=img1,
               command=toggle_win,
               border=0,
               bg='#262626',
               activebackground='#262626')
        b2.place(x=5,y=8)

    global img2
    img2 = ImageTk.PhotoImage(Image.open(r"./assets/close.png"))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#12c4c0',
           activebackground='#12c4c0').place(x=5,y=10)
    



img1 = ImageTk.PhotoImage(Image.open(r"./assets/open.png"))
global nom_image
global b2
global Sortie
global t
b2=Button(w,image=img1,
       command=toggle_win,
       border=0,
       bg='#262626',
       activebackground='#262626')
b2.place(x=5,y=8)

default_home()
w.mainloop()
