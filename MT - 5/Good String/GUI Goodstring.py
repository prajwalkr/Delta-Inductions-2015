from Tkinter import *           # GUI library
root = Tk()
root.title("Good String")       # Title of the app
root.geometry("300x170")        # Size of window

app = Frame(root)               # Add a frame
app.grid()                      # put frame in grid


def program():                          # The main program to compute the result
    ntwords = ["ain't","aren't","can't","couldn't","daren't","didn't","doesn't","don't","hadn't","hasn't","haven't","isn't","mightn't","mustn't","needn't","oughtn't","shalln't","shouldn't","won't","wouldn'"]
    endchars = [",",";",":"]
    middlechars = ["-","_"]
    def printsentence(a):               # prints sentence by also including a . in the end
        if '.' not in a[len(a) - 1]:
            a[len(a) - 1] = a[len(a) - 1] + '.'
        result = ""
        for i in a:
            result += i + " "
        text.delete(0.0,"end")          # clears the text box
        text.insert(0.0,result)         # prints the result
    b = sentence.get()
    a = map(str,b.split())
    a[0] = a[0][0].upper() + a[0][1:]       #Convert first character of every sentence to caps.
    for i in range(len(a)):
        insertlater = ""
        if "'s" == a[i][len(a[i]) - 2:] or "s'" == a[i][len(a[i]) - 2:]:          # use of ' is valid in this case
                insertlater = a[i][len(a[i]) - 2:]
                a[i] = a[i][:len(a[i]) - 2]
        while "'" in a[i] and a[i] not in ntwords:
                a[i] = a[i][:a[i].index("'")] + a[i][a[i].index("'") + 1:]          # Remove ' if used wrongly.
                if a[i][:len(a[i]) - 1] + "'" + a[i][len(a[i]) - 1] in ntwords:
                    a[i] = a[i][:len(a[i]) - 1] + "'" + a[i][len(a[i]) - 1]
        a[i] += insertlater
        for x in endchars:                                                          # Remove , ; : if used somewhere in the middle of the word
            if x in a[i] and a[i].index(x) != len(a[i]) - 1:
                a[i] = a[i][:a[i].index(x)] + a[i][a[i].index(x) + 1:]
        for x in middlechars:                                                       # Remove -  _ if used at the end of the word
                if x in a[i] and a[i].index(x) == len(a[i]) - 1:
                        a[i] = a[i][:len(a[i]) - 1] 
    printsentence(a)


                
display_string = Label(app, text = "Enter a string, and press Convert!")            # Initial text
display_string.grid(row = 0, column = 0,rowspan = 1)

sentence = Entry()
sentence.grid(row = 1, column = 0,rowspan = 1,columnspan = 10, sticky = W)          # Entry-box
sentence.focus()

text = Text(width = 35,height = 3,wrap = WORD)                                      # Result text display box
text.grid(row = 10,column = 0, sticky = W)
text.delete('1.0',END)
convert = Button(app, text = "Convert!",command = program)                          # Convert button
convert.grid(row = 5,rowspan = 1,column = 0)

root.mainloop()