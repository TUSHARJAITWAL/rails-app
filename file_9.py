file = open('studentcse.txt','w')
file.write("Name\t Age\t Class\n")
file.write("ashutosh 25\t B.Tech\n")
file.write("akshay\t 23\t BE\n")
file.write("ankit\t 24\t BSC\n")
file.write("sahil\t 20\t B.Tech\n")
file.write("rupesh\t 30\t M.Tech\n")
file.write("rahul\t 30\t M.Tech\n")
file.close()

def studentdetails():
    what = input("What you want to do search,delete or add a student:")
    if what=='search':
        word= input("Enter Student Name:\n")

        fr=open('studentcse.txt','r')
        for line in fr:
            if word in line:
                print("-------STUDENT FOUND-------")
                print(line)
                break
        fr.close()
            
    elif what=='delete':
        word= input("Enter Student Name:\n")
        fr=open("studentcse.txt", "r")
        f=open("new.txt", "w")
        for line in fr:
            if word in line:
                continue
        f.write(line)
        fr.close()
    
        f=open("new.txt")
        fr=open("studentcse.txt", "w")
        fr.write(f.read())
        f.close()
        fr.close()
        fr=open("studentcse.txt")
        print(fr.read())
        fr.close()
        
    elif what=='add':
        print("Write Student:")
        name=input("NAME:")
        age=int(input("AGE:"))
        clas=input("CLASS:")
        line=f"{name} {age} {clas}"
        fr=open("studentcse.txt", 'a')
        fr.write(line)
        fr.close()
        fr=open("studentcse.txt", 'r')
        print(fr.read())
        fr.close()

    else:
        print("---------Invalid Input!--------")
        print("-----Try again-------")
studentdetails()
studentdetails()
studentdetails()