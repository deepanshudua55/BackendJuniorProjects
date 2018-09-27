import random


class game:
    dmain = []
    name = ""

    def __init__(self, name):
        self.name = name
    def shuffle(self):
        random.shuffle(self.dmain)

#block of code to form a deck of 52 cards which will then be distributed
class dmainform:
    dmain = []
    x=0
    def dform(self):
        for i in range(4):
            for j in range(13):
                self.dmain.append(self.x)
                self.x+=1
        random.shuffle(self.dmain)


class match_a:
    nround = 0
    nclash = 0
    winner = ""
    plyrdsub = []
    compdsub = []
    def __init__(self):
        self.distrib()
#code to distribute 26 cards each to player and computer
    def distrib(self):
        cards = dmainform()
        cards.dform()
        name = input("Enter Player Name ")
        print("\n")
        p1 = game(name)
        comp = game("Computer")

        for i in range(26):
            p1.dmain = cards.dmain[: 26]
            comp.dmain= cards.dmain[26: 52]


        self.plyrdsub = p1.dmain
        self.compdsub = comp.dmain
        self.playername = p1.name
#actual match takes plae in this code
    def startmatch(self):
        while self.plyrdsub != [] and self.compdsub != []:
            self.nround = self.nround + 1
            if self.plyrdsub[0] > self.compdsub[0]:
                temp1 = self.plyrdsub[0]
                temp2 = self.compdsub[0]
                self.plyrdsub = self.plyrdsub[1:]
                self.plyrdsub.append(temp1)
                self.plyrdsub.append(temp2)
                self.compdsub = self.compdsub[1:]

            elif self.plyrdsub[0] < self.compdsub[0]:
                temp2 = self.plyrdsub[0]
                temp1 = self.compdsub[0]
                self.compdsub = self.compdsub[1:]
                self.compdsub.append(temp1)
                self.compdsub.append(temp2)
                self.plyrdsub = self.plyrdsub[1:]
            else: #code for war
                if len(self.plyrdsub) >= 4 and len(self.compdsub) >= 4:
                    self.nclash = self.nclash + 1
                    sum1 = self.plyrdsub[1] + self.plyrdsub[2] + self.plyrdsub[3]
                    sum2 = self.compdsub[1] + self.compdsub[2] + self.compdsub[3]
                    if sum1 > sum2:
                        tempa = self.plyrdsub[0]
                        tempb = self.plyrdsub[1]
                        tempc = self.plyrdsub[2]
                        tempd = self.plyrdsub[3]
                        tempe = self.compdsub[0]
                        tempf = self.compdsub[1]
                        tempg = self.compdsub[2]
                        temph = self.compdsub[3]
                        self.plyrdsub = self.plyrdsub[4:]
                        self.plyrdsub.append(tempa)
                        self.plyrdsub.append(tempb)
                        self.plyrdsub.append(tempc)
                        self.plyrdsub.append(tempd)
                        self.plyrdsub.append(tempe)
                        self.plyrdsub.append(tempf)
                        self.plyrdsub.append(tempg)
                        self.plyrdsub.append(temph)
                        self.compdsub = self.compdsub[4:]

                    elif (sum1 < sum2):
                        tempa = self.plyrdsub[0]
                        tempb = self.plyrdsub[1]
                        tempc = self.plyrdsub[2]
                        tempd = self.plyrdsub[3]
                        tempe = self.compdsub[0]
                        tempf = self.compdsub[1]
                        tempg= self.compdsub[2]
                        temph = self.compdsub[3]
                        self.compdsub = self.compdsub[4:]
                        self.compdsub.append(tempe)
                        self.compdsub.append(tempf)
                        self.compdsub.append(tempg)
                        self.compdsub.append(temph)
                        self.compdsub.append(tempa)
                        self.computerdeck.append(tempb)
                        self.computerdeck.append(tempc)
                        self.computerdeck.append(tempd)
                        self.plyrdsub = self.plyrdsub[4:]

                    else:
                        self.plyrdsub = self.plyrdsub[4:]
                        self.compdsub = self.compdsub[4:]

                else:
                    if len(self.plyrdsub) >= 4:
                        self.winner = "player"
                        break
                    elif len(self.compdsub) >= 4:
                        self.winner = "computer"
                        break


        print("Number of Rounds: " + str(self.nround))
        print("Number of Wars: " + str(self.nclash))
        if self.plyrdsub == [] or self.winner == "computer":
            print("The Computer is the winner")
        if self.compdsub == [] or self.winner == "player":
            print(str(self.playername) + " is the winner")

#invoking
Game = match_a()
Game.startmatch()