

class Room:
    idCounter = 0
    
    def __init__(self):
        self.id = Room.idCounter
        self.type = 0 # does nothing
        self.pathways =  [None, None, None, None]
        self.players = [] # theoretically only needs to hold the names?
        Room.idCounter += 1
        #    0
        #  3   1
        #    2
        
        # 1 as the room is blocked
        
    def printDescription(self):
        strReturn = ""
        strReturn += (f"ID : {self.id}\n")
        strReturn += (f"Paths : [ ")
        for x in self.pathways:
            if x is not None:
                strReturn += (f"{x.id} ")
            else:
                strReturn += "~ "
        strReturn += "]\n"
        return strReturn
        
    def adjustName(self, name): #returns the name in 12 character max form for printing
        if(len(name) > 14):
            end = name[len(name)-4:]
            return name[:9] + ".." + end
        else:
            return f"{name:^15}"
        
    def __str__(self):
        
        # FIX ME add in a case for no players .needed?

        # player printing # # # # # # # # #
        strEnd =     ""
        strNames =   ""
        strTime =    ""
        strNotice =  ""
        strReturn =  ""
        strKeys =    ""
        # note each block should be "* 15-characters *"
        
        
        for x in self.players: # end piece
            strEnd += "* * * * * * * * * *  " 
        for x in self.players: # name
            strNames += "* " + self.adjustName(x.name) + " *  " # up to 4 player max
        for x in self.players: # time
            temp = f"Time: {x.currTime}/{x.maxTime}"
            temp = "{:^15}".format(temp)
            temp = "* " + temp + " *  "
            strTime += temp
        for x in self.players: # notice
            temp = f"Notice: {x.notice}"
            temp = "{:^15}".format(temp)
            temp = "* " + temp + " *  "
            strNotice += temp
        for x in self.players: # keys
            temp = f"Keys: {x.keys}"
            temp = "{:^15}".format(temp)
            temp = "* " + temp + " *  "
            strKeys += temp
            
        
        length = 51 # middle of print
        strNames = f"{strNames:^{length}}"
        strTime = f"{strTime:^{length}}"
        strNotice = f"{strNotice:^{length}}"
        strKeys = f"{strKeys:^{length}}"
        strEnd = f"{strEnd:^{length}}"
        
        strReturn += f"{strNames}\n{strTime}\n{strNotice}\n{strKeys}\n{strEnd}\n\n" # name printing complete
        
        
        # top exit printing # # # # # # # # # #
        
        # 19 char length
        strTop =  "                   "
        strMid1 = "                   "
        strMid2 = "                   "
        strMid3 = "                   "
        strEnd =  "                   "
        
            
        strTop +=      "* * * * * *  "
        strMid1 +=     "*    1    *  "
        strMid2 +=     "*         * "
        if self.pathways[0] is None:
            strMid3 += "* Blocked *  "
        else:
            strMid3 += "*   Open  *  "
        strEnd +=      "* * * * * *  "
                
        strReturn += f"{strTop}\n{strMid1}\n{strMid2}\n{strMid3}\n{strEnd}\n"
        
        # left exit
        
        # 13 char length to the ends
        strTop =  "             "
        strMid0 = ""
        strMid1 = ""
        strMid2 = ""
        strMid3 = ""
        strMid4 = ""
        strEnd =  "             "
        
            
        strMid0 +=     "* * * * * *  "
        strMid1 +=     "*    4    *  "
        strMid2 +=     "*         *  "
        if self.pathways[3] is None:
            strMid3 += "* Blocked *  "
        else:
            strMid3 += "*   Open  *  "
        strMid4 +=     "* * * * * *  "
        
        # room 
         
        strTop +=  "* * * * * * * * * * * *  "
        strMid0 += "*                     *  "
        strMid1 += "*        Fill         *  "
        strMid2 += "*   with info later   *  "
        strMid3 += "*                     *  "
        strMid4 += "*                     *  "
        strEnd +=  "* * * * * * * * * * * *  "
        
        # right exit
        
        strMid0 +=     "* * * * * *  "
        strMid1 +=     "*    2    *  "
        strMid2 +=     "*         *  "
        if self.pathways[1] is None:
            strMid3 += "* Blocked *  "
        else:
            strMid3 += "*   Open  *  "
        strMid4 +=     "* * * * * *  "
        
        
                
        strReturn += f"{strTop}\n{strMid0}\n{strMid1}\n{strMid2}\n{strMid3}\n{strMid4}\n{strEnd}\n"
        
        
        # bottom exit
        # 19 char length
        strTop =  "                   "
        strMid1 = "                   "
        strMid2 = "                   "
        strMid3 = "                   "
        strEnd =  "                   "
        
            
        strTop +=      "* * * * * * "
        strMid1 +=     "*    3    * "
        strMid2 +=     "*         * "
        if self.pathways[2] is None:
            strMid3 += "* Blocked * "
        else:
            strMid3 += "*   Open  * "
        strEnd +=      "* * * * * * "
                
        strReturn += f"{strTop}\n{strMid1}\n{strMid2}\n{strMid3}\n{strEnd}\n"
        
        
        return strReturn
    

    def leadsTo(self, nextRoom, direction, oneway):
        self.pathways[direction] = nextRoom
        if(oneway == False):
            set = self
        else:
            set = None # blocked
        match(direction): # setting the way back, note visually correct 
            case 0:
                nextRoom.pathways[2] = set
            case 1:
                nextRoom.pathways[3] = set
            case 2:
                nextRoom.pathways[0] = set
            case 3:
                nextRoom.pathways[1] = set
