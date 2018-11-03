import random
from pip._vendor.distlib.compat import raw_input
rounds=0
war=0
player = raw_input("enter your name")
type(player)
class Card():
    def __init__(self,suite,no):
        self.suite=suite
        self.no=no

class Deck():
    X=[]
    def __init__(self):
        self.allcards=[]
        self.calc()
        print(self.allcards)
    def calc(self):
        cards = []
        s = ['heart','diamond','spade','club']
        n = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
        for x in s:
            for o in n:
                cards.append(Card(x,o))
        self.allcards = cards
        X=cards
D1 = Deck()
random.shuffle(D1.X)

class Player(Card):
    C1=[]
    name=player
class Computer(Card):
    C2=[]
    name="system"

a=Player()
b=Computer()
def distribute():
    for j in range(0,25,j=j+1):
        a.C1=D1.X[j]
        b.C2=D1.X[j+26]
distribute()
print("game starts now\n")
while not a.C1 or not b.C2:
    rounds+=1
    i=0
    print("your card",a.C1[i])
    print("computer card",b.C2[i])
    if a.C1[i].no > b.C2[i].no:
        print("you won this round")
        f=a.C1[i]
        del a.C1[i]
        a.C1.append(b.C2[i],f)
        del b.C2[i]
    elif a.C1[i].no < b.C2[i].no:
        print("you lost this round")
        g=b.C2[i]
        del b.C2[i]
        b.C2.append(a.C1[i],g)
        del a.C1[i]
    else:
        print("war starts")
        war+=1
        print("your cards",a.C1[i+1],a.C1[i+2],a.C1[i+3])
        print("computer cards",b.C2[i+1],b.C2[i+2],b.C2[i+3])
        t=a.C1[i+1].no+a.C1[i+2].no+a.C1[i+3].no
        r=b.C2[i+1].no+b.C2[i+2].no+b.C2[i+3].no
        if t > r:
            print("you won this war")
            for w in range(1,3,w=w+1):
                l=a.C1[i+w]
  	            del a.C1[i+w]
                a.C1.append(b.C2[i+w],l)
                del b.C2[i+w]
        elif t < r:
            print("you lost this war")
            for w in range(1,3,w=w+1):
   	            h=b.C2[i+w]
   	            del b.C2[i+w]
   	            b.C2.append(a.C1[i+w],h)
   	            del a.C1[i+w]
        else:
            i=i+4
            continue
    if not a.C1:
        print("you lost","rounds=",rounds,"wars=",war,"winner=",b.name)
    if not b.C2:
        print("you won","rounds=",rounds,"wars=",war,"winner=",a.name)
    i=i+1










