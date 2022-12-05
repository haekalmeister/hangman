import random
from tkinter import *
from tkinter import messagebox
import winsound


score = 0
run = True
location = "E:/Kuliah/Akademik/Semester 5/Pemlan/Dosen/Projek/"


# main loop
while run:
    root = Tk()
    root.geometry('905x700')
    root.title('H_NGM_N')
    root.config(bg = 'white')
    count = 0
    win_count = 0
    winsound.PlaySound("E:/Kuliah/Akademik/Semester 5/Pemlan/Dosen/Projek/music.wav", winsound.SND_ASYNC)
    
    

    # pemilihan kata
    index = random.randint(0,9)
    file = open('{}words.txt'.format(location),'r')
    l = file.readlines()
    selected_word = l[index].strip('\n')
    
    # variabel word dashes
    x = 250
    for i in range(0,len(selected_word)):
        x += 60
        exec('d{}=Label(root,text="_",bg="white",fg = "black",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,450))
        
    #huruf
    al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for let in al:
        exec('{}=PhotoImage(file="{}{}.png")'.format(let,location,let))
        
    # gambar hangman
    h123 = ['h1','h2','h3','h4','h5','h6','h7']
    for hangman in h123:
        exec('{}=PhotoImage(file="{}{}.png")'.format(hangman,location,hangman))
        
    #penempatan button
    button = [['b1','a',0,595],['b2','b',70,595],['b3','c',140,595],['b4','d',210,595],['b5','e',280,595],['b6','f',350,595],['b7','g',420,595],['b8','h',490,595],['b9','i',560,595],['b10','j',630,595],['b11','k',700,595],['b12','l',770,595],['b13','m',840,595],['b14','n',0,645],['b15','o',70,645],['b16','p',140,645],['b17','q',210,645],['b18','r',280,645],['b19','s',350,645],['b20','t',420,645],['b21','u',490,645],['b22','v',560,645],['b23','w',630,645],['b24','x',700,645],['b25','y',770,645],['b26','z',840,645]]

    for q1 in button:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="white",activebackground="white",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))
        
    #penempatan gambar hangman
    han = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
    for p1 in han:
        exec('{}=Label(root,bg="white",image={})'.format(p1[0],p1[1]))

    # penempatan gambar hangman pertama
    c1.place(x = 300,y =- 50)
    
    # exit
    def close():
        global run
        answer = messagebox.askyesno('Perhatian','Apakah Anda ingin keluar permainan?')
        if answer == True:
            run = False
            root.destroy()
            
    e1 = PhotoImage(file = '{}exit.png.'.format(location))
    ex = Button(root,bd = 0,command = close,bg="white",activebackground = "white",font = 10,image = e1)
    ex.place(x=770,y=10)
    s2 = 'HIGHSCORE:'+str(score)
    s1 = Label(root,text = s2,bg = "white",font = ("helvetica",25), fg = 'black')
    s1.place(x = 10,y = 10)

    # checking jawaban
    def check(letter,button):
        global count,win_count,run,score
        exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(0,len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}", fg = "black")'.format(i,letter.upper()))
            if win_count == len(selected_word):
                score += 1
                winsound.PlaySound("E:/Kuliah/Akademik/Semester 5/Pemlan/Dosen/Projek/win.wav", winsound.SND_ASYNC)
                answer = messagebox.askyesno('SELAMAT','Anda Menang!\nBermain lagi?')
                if answer == True:
                    run = True
                    root.destroy()   
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count+1,300,-50))
            if count == 6:
                winsound.PlaySound("E:/Kuliah/Akademik/Semester 5/Pemlan/Dosen/Projek/Gameover.wav", winsound.SND_ASYNC)
                answer = messagebox.askyesno('GAME OVER\\','Anda Kalah!\nBermain lagi?')
                if answer == True:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()         
    root.mainloop()