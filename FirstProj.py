userName = input("Enter your name\n")
notes = input("Enter some notes\n")

with open("file.txt","w") as f :
    f.write(userName + "\n" + notes)

with open("file.txt","r") as f :    
    print(f.read())