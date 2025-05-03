#variables
with open("notdone.txt", "r") as file:
    notdone = file.read()
new = 0
with open("done.txt", "r") as file:
    done = file.read()

deleted = 0
#info
print("Taskcli(opensource project by desu)\n",
      "new: new task\n",
      "done: moves chosen task to done\n",
      "clear: removes EVERYTHING from done\n",
      "help:displays this screen\n"
      " read: prints out all the tasks(done and not done)")
#asks for user input
userinput = input("task:")


#make strikethrugh text
def strikethrough(text):
    return ''.join(c + '\u0336' for c in text)
#actual code
while True:
    #input

    #adding new tasks
    if "new" in userinput:

        #deffines the task
        new = input("new:")

        with open("notdone.txt", "a") as file:
            file.write("\n" + new)
        with open("notdone.txt", "r") as file:
            notdone = file.read()

    #moving tasks to done
    if "done" in userinput:
        with open("done.txt", "w") as file:
            done = ""
            file.write("")
        #deffines the done word
        with open("notdone.txt", "r") as file:
            notdone = file.read()
        print(notdone)
        value_to_move = input("done:")

        # Read all lines from
        with open("notdone.txt", "r") as file:
            lines = file.readlines()

        #Remove the value from the lines
        lines = [line.strip() for line in lines if line.strip() != value_to_move]

        #Write the updated lines back to notdone
        with open("notdone.txt", "w") as file:
            for line in lines:
                file.write(line + "\n")

        #Append the value to done.txt
        with open("done.txt", "a") as file:
            file.write(value_to_move + "\n")
        #reeds the inside of done.txt
        with open("done.txt", "r") as file:
             done = file.read()
        #reeds the inside of notdone.txt
        with open("notdone.txt", "r") as file:
              notdone = file.read()
        # output
        print("done:")
        print(strikethrough(done))
        print("not done:")
        print(notdone)
        userinput = input("task:")
    #displays the help screen
    if "help" in userinput:
         print("Taskcli(opensource project by desu)\n",
                "new: new task\n",
                "done: moves chosen task to done\n",
                "clear: removes EVERYTHING from done\n",
                "help:displays this screen\n"
                "read: prints out all the tasks(done and not done)")

    #reads the done and not done tasks
    if "read" in userinput:
        # output
        print("done:")
        if "null" in done:
            print("there is nothing in done")
        else:
            print(strikethrough(done))

        print("not done:")
        print(notdone)


    if "clear" in userinput:
        with open("done.txt", "w") as file:
            file.write("null")
        done = "null"


    userinput = input("task:")