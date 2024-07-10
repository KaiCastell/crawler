#import entity

class Mind:
    
    def __init__(self, type): # type is class, same thing
        blank = Thought("blank")
        self.thoughtArray = [
            [blank, blank, blank],
            [blank, blank, blank],
            [blank, blank, blank]
        ]
        match(type):
            case "Blank":
                return
            case "Scientist":
                pass #empty for now
            
    def __str__(self):
        
        strReturn = ""
        for row in self.thoughtArray:
            strTop =  ""
            strMid0 = ""
            strMid1 = ""
            strMid2 = ""
            strMid3 = ""
            strMid4 = ""
            strMid5 = ""
            strEnd =  ""
            
            for element in row:
                temp = str(element)
                strTop +=  temp[:22] # we are given one continuous string so im splitting it back up
                temp = temp[22:]
                strMid0 += temp[:22]
                temp = temp[22:]
                strMid1 += temp[:22]
                temp = temp[22:]
                strMid2 += temp[:22]
                temp = temp[22:]
                strMid3 += temp[:22]
                temp = temp[22:]
                strMid4 += temp[:22]
                temp = temp[22:]
                strMid5 += temp[:22]
                temp = temp[22:]
                strEnd +=  temp[:22]
                temp = temp[22:]
                
            strReturn += f"{strTop}\n{strMid0}\n{strMid1}\n{strMid2}\n{strMid3}\n{strMid4}\n{strMid5}\n{strEnd}\n"
            strReturn += "\n"
            
        return strReturn


class Thought: # like cards so this is going to be quite long
    
    def __init__(self, thoughtName):
        self.name = None
        self.timeCost = 0
        match(thoughtName):
            case "blank":
                self.name = "Blank"
            case _:
                pass
            
    def __str__(self):  # 21 char length per line
        strTop =  "* * * * * * * * * *   "
        strMid0 = "*                 *   "
        strMid1 = "*                 *   "
        strMid2 = "*                 *   "
        strMid3 = "*                 *   "
        strMid4 = "*                 *   "
        strMid5 = "*                 *   "
        strEnd =  "* * * * * * * * * *   "
        
        match(self.name):
            case "blank":
                temp = self.name
                temp = "{:^16}".format(temp)
                strMid2 = "* "
                strMid2 += temp
                strMid2 += "*   "
                
                temp = "Do nothing"
                temp = "{:^16}".format(temp)
                strMid3 = "* "
                strMid3 += temp
                strMid3 += "*    "
            case _: # same as blank
                temp = self.name
                temp = "{:^16}".format(temp)
                strMid2 = "* "
                strMid2 += temp
                strMid2 += "*   "
                
                temp = "Does nothing"
                temp = "{:^16}".format(temp)
                strMid3 = "* "
                strMid3 += temp
                strMid3 += "*   "
        
        return strTop + strMid0 + strMid1 + strMid2 + strMid3 + strMid4 + strMid5 + strEnd
        