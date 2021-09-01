dep = input("How much do you want to deposit (between 0 and 590k?)")
z=len(dep)
if dep[z-1] == "k" :
    dep = int(dep[:z-1])
    dep = dep*1000
def error():
    print("Error, please input an integer between 0 and 590000")
    quit()

try :
    dep = int(dep)
except :
    error()

if dep > 590000 :
    error()
else :
    def twenty(x) :
        print("Deposit $", x, "into Ant Bank ac for 2%pa interest")
    def forty(x) :
        twenty(20000)
        print("Then, deposit $", x-20000, "into Airstar Bank for 1.2%pa interest")
    def ninety(x) :
        forty(40000)
        print ("Then, deposit $", x-40000, "into Livi Bank for 1%pa interest")
    try :
        if dep <= 20000 :
            twenty(dep)
        elif dep <= 40000 :
            forty(dep)
        elif dep <= 90000 :
            ninety(dep)
        elif dep <= 590000 :
            ninety(90000)
            print("Spend $4000 on Mox card and then deposit", dep-90000, "into Mox account")
    except :
        quit()
