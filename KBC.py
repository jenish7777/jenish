print("hello my friend")
a=input("plese enter your name:-")
print("hy!"," "+a)
print("you want to play KBC ")
print("lets strat")

list=(("which of the following corresponds to 'ek bataa do'?","pura","sawa","adha","pauna"),("which of the following gods is also known as 'Gauri Nanda'?","Agni","indara","hanuman","ganesh"),("in the game of ludo the dics or tokens are of how many colours?","one","two","three","four"),("which of these are names of national parks locted in madhya orades? ","krishna and kanhaiya","kanha and madhav","ghanshyam and murari","girdhar and gopal"),("where was the BRICS summit held in 2014?","brazil","india","russia","china"))

level=(1000,2000,3000,4000,5000)

help=("phone","50 to 50","audience support","skip")

answer=("c","d","d","b","a")

queNo=(1,2,3,4,5)

for i in range(0,len(list)):
    que=list[i]
    print("This questions is",level[i],"Ruppes")
    print(queNo[i],".",que[0])
    print("a",que[1],"         ","b",que[2])
    print("c",que[3],"         ","d",que[4])
    a=input("you want helpline in thish question (yes or no):-")
    if a=="yes":
        print("which helpline to use this question")
        print("a",help[0],"         ","b",help[1])
        print("c",help[2],"         ","d",help[3])
        b=input("enter you answer from(a-d):-")
        if(b=="a"):
            print("wich people you want call")
        elif(b=="b"):
            print("ok")
        elif(b=="c"):
            print("ok")
        else:
            print("ok")
        c=input("enter your answer(a-d):-")
        if(c==answer[i]):
             print("your answer is right you win",level[i],"ruppes")
        else:
             print("you are worng")
             print("try next time")
             break
    elif(a=="no"):
        c=input("enter your answer(a-d):-")
        if(c==answer[i]):
            print("your answer is right you win",level[i],"ruppes")
        else:
            print("you are worng")
            print("try next time")
            break

        


      
        


    
