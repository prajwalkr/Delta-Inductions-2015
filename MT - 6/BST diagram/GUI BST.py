import Queue,sys
from Tkinter import *           # GUI library
root = Tk()
root.title("BST diagram")       # Title of the app
root.geometry("300x300")        # Size of window

app = Frame(root)               # Add a frame
app.grid()                      # put frame in grid


def program():
    def next_element(q):
        p = q.get()
        Q = Queue.Queue()
        Q.put(p)
        while q.empty() == False:
            Q.put(q.get())
        while Q.empty() == False:
            q.put(Q.get())
        return p
    class bst:
        def __init__(self,val = None,parent = None):
            self.lchild = None
            self.rchild = None
            self.parent = parent
            self.data = val
        def insert(self,data):
            if self.data == None:
                self.data = data
            elif self.data == data:
                return
            elif self.data > data:
                if self.lchild is None:
                    self.lchild = bst(data,self)
                else:
                    self.lchild.insert(data)
            elif self.rchild is None:
                self.rchild = bst(data,self)
            else:
                self.rchild.insert(data)
        def print_bst(self):
            printmessage = ""
            if self.lchild is not None:
                printmessage = self.lchild.print_bst()
            printmessage += str(self.data)+ ' '
            if self.rchild is not None:
                printmessage += self.rchild.print_bst()
            return printmessage
        def bst_outline(self,q,spaces):
            printmessage = spaces
            nextline = ""
            l = q.qsize()
            for i in range(l):
                p = q.get()
                printmessage += str(p.data) + ' '
                if p.lchild == None:
                    #printmessage += '  '
                    if i == 0:
                        nextline = spaces + ' '
                        spaces += '  '
                    else:
                        nextline += '  '
                else:
                    q.put(p.lchild)
                    if i == 0:
                        spaces = spaces[:len(spaces) - 1]
                        nextline = spaces + '/ '
                        spaces = spaces[:len(spaces) - 1]
                    else:
                        nextline += '/ '
                if p.rchild == None:
                    nextline += '  '
                else:
                    q.put(p.rchild)
                    nextline += '\ '
                if p.lchild == None or p.rchild == None:
                    if i != l - 1:
                        P = next_element(q)
                        if p.parent is not None:
                            if p.parent.data == P.parent.data:
                                printmessage += '  '
                            else:
                                printmessage += '   '
                else:
                    printmessage += '   '
            printmessage += '\n'
            printmessage += nextline + '\n'
            if q.empty() == True:
                return printmessage;
            printmessage += root.bst_outline(q,spaces)
            return printmessage

    a = map(int,(sentence.get()).split())
    root = bst()
    for i in a:
        root.insert(i)
    printmessage = root.print_bst()
    printmessage += '\n\n'
    q = Queue.Queue()
    q.put(root)
    printmessage += root.bst_outline(q," "*(2*len(a)))
    text.delete(0.0,"end")          # clears the text box
    text.insert(0.0,printmessage)         # prints the result                        

display_string = Label(app, text = "Enter elements separated by space and press BST!")            # Initial text
display_string.grid(row = 0, column = 0,rowspan = 1)

sentence = Entry()
sentence.grid(row = 1, column = 0,rowspan = 1,columnspan = 10, sticky = W)          # Entry-box
sentence.focus()

text = Text(width = 37,height = 15,wrap = WORD)                                      # Result text display box
text.grid(row = 10,column = 0, sticky = W)

convert = Button(app, text = "BST!",command = program)                          # Convert button
convert.grid(row = 5,rowspan = 1,column = 0)

root.mainloop()
