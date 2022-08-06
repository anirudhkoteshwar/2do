"""
    2DO APP
    Anirudh Koteshwar
    4-8-22
"""
from tabulate import tabulate
import os
import sys

header = "ID`Task`Status\n"
parent_list = []
lt = []

def add(task):
    with open("todo.txt", 'r') as prevsav: #pull the existing file 
        x = 0
        for line in prevsav:
            x += 1
    if x == 0:   #if the file is empty add the header
        with open("todo.txt", 'a') as prevsav: 
            prevsav.write(header)
        id = 1 
    else:
        id = x
    stat = "X" #default status is not done 'X'. when done, changes to '✓'
    entry = str(id)+"`"+task+"`"+stat #create the entry format
    li = list(entry.split("`"))
    parent_list.append(li) #add the entry to the list
    with open("todo.txt", 'a') as newsav: #save the list
        newsav.write("%s\n" % entry)        
        print("Added task Successfully")
    parent_list.clear()

def clean(): #clears the existing file
    open('todo.txt', 'w').close() 
    print("List Cleaned")

def status():
    with open("todo.txt", 'r') as prevsav: #pull the existing file 
        for line in prevsav: #parses the file into a list
            li = list(line[:-1].split("`")) 
            parent_list.append(li)
        print(tabulate(parent_list, headers='firstrow', tablefmt='fancy_grid')) #uses tabulate to display data
        parent_list.clear()
           
def remove(rm):
    try:
        rm = int(rm)
        parent_list.clear()
        with open("todo.txt", 'r') as prevsav:
            for line in prevsav: #parse the data into a list
                li = list(line[:-1].split("`"))
                parent_list.append(li)
            if len(parent_list) < rm:
                input("Invalid ID: Press any key to continue")
            else:
                for i in range(len(parent_list)): #ignore the first line
                    if parent_list[i][0] == "ID":
                        continue
                    if int(parent_list[i][0]) > rm: #decrease all indices after input by 1
                        j = int(parent_list[i][0]) - 1
                        parent_list[i][0] = str(j)
                open('todo.txt', 'w').close() #clear the file
                with open("todo.txt", 'a') as newsav:
                    for i in range(len(parent_list)): #expand the list and write to the file
                        if i != rm:
                            entry = parent_list[i][0]+"`"+parent_list[i][1]+"`"+parent_list[i][2] 
                            newsav.write("%s\n" % entry) 
        parent_list.clear()
    except ValueError:
        input("You need to enter the line ID not the text: Press any key to continue")
         
def done(x):
    try:
        x = int(x)
        parent_list.clear()
        with open("todo.txt", 'r') as prevsav:
            for line in prevsav:
                li = list(line[:-1].split("`"))
                parent_list.append(li)
            if len(parent_list) < x:
                input("Invalid ID: Press any key to continue")
            else:
               parent_list[x][2] = '✓'
               open('todo.txt', 'w').close() #clear the file
               with open("todo.txt", 'a') as newsav:
                    for i in range(len(parent_list)): #expand the list and write to the file
                        entry = parent_list[i][0]+"`"+parent_list[i][1]+"`"+parent_list[i][2] 
                        newsav.write("%s\n" % entry)
        parent_list.clear() 
    except ValueError:
        input("You need to enter the line ID not the whole line: Press any key to continue")

def main():
    while True: #loop to get inputs
        with open("todo.txt", 'r') as prevsav: #pull the existing file 
            j = 0
            for line in prevsav:
                j += 1
        if j != 0: #show the status only if the file isnt empty. Otherwise tabulate looks broken
            status()
        print("Here is what I can do: \n\tTo add a task: add TASK\n\tTo remove a task : remove ID_OF_TASK(s)_TO_BE_REMOVED (separated by spaces) \n\tTo clear the list: clear\n\tTo mark a task as done: done ID_OF_TASK_DONE\n\tTo exit the program: quit")
        x = input("\nWhat should I do? : ")
        ls = x.split(" ")
        if ls[0] == "add":
            ls[1] = ' '.join(ls[1:]) #allows multi-word tasks
            add(ls[1])
            os.system('clear') 
        elif ls[0] == "clear":
            clean()
            os.system('clear') 
        elif ls[0] == "status":
            status()
            os.system('clear') 
        elif ls[0] == "done":
            done(int(ls[1]))
            os.system('clear')
        elif ls[0] == "remove":
            if len(ls) == 2:
                remove(int(ls[1]))
            elif len(ls) > 2:
                for i in ls[1:]: #for multi-remove, sort the inputs in descending order to avoid issues
                    k = int(i)
                    lt.append(k)
                lt.sort(reverse=True)    
                for i in lt:
                    remove(i)
            elif len(ls) == 1:
                print("You need to enter the ID of the task to be removed\n")
            else:
                continue            
            os.system('clear')
        elif ls[0] == "quit":
            sys.exit("Exiting 2do")
            os.system('clear')

        else:
            print("Invalid input")
        os.system('clear')
    
main() 
       
        
