# Checks if they're are duplicates in the balls picked
# Used for form validation
# Returns balls that are duplicates
def Duplicates(ballList):
    dupList = []
    for x in range(0, len(ballList)):
        for y in range(0, len(ballList)):
            if ballList[x] == ballList[y]:
                if x == y:
                    continue
                else:
                    dupList.append("ball" + str(x + 1))
    return list(set(dupList))
