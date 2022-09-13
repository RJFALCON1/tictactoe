from tkinter import *
import tkinter.messagebox
root = Tk()
root.title('TicTacToe')
player1 = StringVar()
player2 = StringVar()
player1_box = Entry(root,textvariable=player1)
player2_box = Entry(root,textvariable=player2)
player1_box.grid(row=1,column=1,columnspan=8)
player2_box.grid(row=2,column=1,columnspan=8)
flag = 0
bclick = True
def disableAllButtons():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def winner():
    if (button1['text']=='X' and button2['text']=='X' and button3['text']=='X' or 
        button4['text']=='X' and button5['text']=='X' and button6['text']=='X' or
        button7['text']=='X' and button8['text']=='X' and button9['text']=='X' or
        button1['text']=='X' and button5['text']=='X' and button9['text']=='X' or
        button1['text']=='X' and button4['text']=='X' and button7['text']=='X' or
        button2['text']=='X' and button5['text']=='X' and button8['text']=='X' or
        button3['text']=='X' and button6['text']=='X' and button9['text']=='X' or
        button3['text']=='X' and button5['text']=='X' and button7['text']=='X'):
            disableAllButtons()
            tkinter.messagebox.showinfo('Tic Tac Toe', player1.get()+' wins the game!')
    elif (button1['text']=='O' and button2['text']=='O' and button3['text']=='O' or 
        button4['text']=='O' and button5['text']=='O' and button6['text']=='O' or
        button7['text']=='O' and button8['text']=='O' and button9['text']=='O' or
        button1['text']=='O' and button5['text']=='O' and button9['text']=='O' or
        button1['text']=='O' and button4['text']=='O' and button7['text']=='O' or
        button2['text']=='O' and button5['text']=='O' and button8['text']=='O' or
        button3['text']=='O' and button6['text']=='O' and button9['text']=='O' or
        button3['text']=='O' and button5['text']=='O' and button7['text']=='O'):
            disableAllButtons()
            tkinter.messagebox.showinfo('Tic Tac Toe', player2.get()+' wins the game!')
    elif (flag == 8):
        tkinter.messagebox.showinfo('Tic Tac Toe', 'TIE GAME')

def valDecide(button):
    global flag, bclick
    if bclick == True and button['text'] == ' ':
        button['text'] = 'X'
        bclick = False
        flag = flag + 1
        winner()
    elif bclick == False and button['text'] == ' ':
        button['text'] = 'O'
        bclick = True
        flag = flag + 1
        winner()
    

label1=Label(root,text='Player 1:',font='Times 20 bold',bg='white',fg='black',height = 1,width = 8)
label1.grid(row=1,column=0)
label2=Label(root,text='Player 2:', font='Times 20 bold',bg = 'white', fg = 'black', height = 1, width = 8)
label2.grid(row=2,column=0)
button1=Button(root,text=' ',font='Times 20 bold', bg = 'gray',fg='black',height=4,width=8,command=lambda:valDecide(button1))
button1.grid(row=3,column=0)
button2=Button(root,text=' ',font='Times 20 bold', bg = 'gray',fg='black',height=4,width=8,command=lambda:valDecide(button2))
button2.grid(row=3,column=1)
button3=Button(root,text=' ',font='Times 20 bold', bg = 'gray',fg='black',height=4,width=8,command=lambda:valDecide(button3))
button3.grid(row=3,column=2)
button4=Button(root,text=' ',font='Times 20 bold', bg = 'gray',fg='black',height=4,width=8,command=lambda:valDecide(button4))
button4.grid(row=4,column=0)
button5=Button(root,text=' ',font='Times 20 bold', bg = 'gray',fg='black',height=4,width=8,command=lambda:valDecide(button5))
button5.grid(row=4,column=1)
button6=Button(root,text=' ',font='Times 20 bold', bg = 'gray',fg='black',height=4,width=8,command=lambda:valDecide(button6))
button6.grid(row=4,column=2)
button7=Button(root,text=' ',font='Times 20 bold', bg = 'gray',fg='black',height=4,width=8,command=lambda:valDecide(button7))
button7.grid(row=5,column=0)
button8=Button(root,text=' ',font='Times 20 bold', bg = 'gray',fg='black',height=4,width=8,command=lambda:valDecide(button8))
button8.grid(row=5,column=1)
button9=Button(root,text=' ',font='Times 20 bold', bg = '#807a79',fg='black',height=4,width=8,command=lambda:valDecide(button9))
button9.grid(row=5,column=2)

root.mainloop()
