# to minimize clutter in the actual main file

import random

class call():
    @staticmethod
    def roll(string):
        roll = 0
        returnStr = "Your roll: "
        words = string.split()
        adding = True
        for x in range(len(words)):
            numRolls = ""
            rollSize = ""
            if words[x] == "+":
                returnStr += "+ "
            elif words[x] == "-":
                returnStr += "- "
                adding = False
            else:
                x_modified = words[x] + "$"  # Create a new modified string
                firstHalf = True
                for y in range(len(x_modified)):
                    try:
                        if x_modified[y] in "+-$":  # Handle end of die or whole word
                            if y == 0: #in case the spaces are weird like so "2d6 +1d6"
                                if x_modified[y] == "+":
                                    adding = True
                                    returnStr += "+ "
                                elif x_modified[y] == "-":
                                    adding = False
                                    returnStr += "- "
                                continue
                            if firstHalf: # must be just a number
                                roll += int(numRolls)
                                returnStr += numRolls + " "
                            else:
                                numRolls = int(numRolls)
                                rollSize = int(rollSize)
                                returnStr += "("
                                for z in range(numRolls):
                                    temp = random.randint(1, rollSize)
                                    if adding:
                                        roll += temp
                                    else:
                                        roll -= temp
                                    returnStr += str(temp)
                                    if z + 1 < numRolls:
                                        returnStr += " + "
                                    else:
                                        returnStr += ") "
                            if x_modified[y] == "+":
                                adding = True
                                returnStr += "+ "
                            elif x_modified[y] == "-":
                                adding = False
                                returnStr += "- "
                            numRolls = ""
                            rollSize = ""
                            firstHalf = True
                            continue
                        
                        elif x_modified[y] != 'd' and firstHalf:
                            numRolls += x_modified[y]
                        elif x_modified[y] != 'd' and not firstHalf:
                            rollSize += x_modified[y]
                        elif x_modified[y] == 'd' and firstHalf:
                            firstHalf = False
                        else:
                            raise ValueError("Invalid format")  # Raise a more specific exception
                    except Exception as e:
                        return f"Failed to roll, try to format as XdX, where X is a number. Note: {str(e)}"
        returnStr += f"= `{roll}`"
        return returnStr

print(call.roll("2d6 + 1d6"))