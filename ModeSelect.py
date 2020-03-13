#Shashwat Vaibhav
#Rule selection among from 7 modes of a scale 
List   = ['W','W','H','W','W','W','H']

def selectMode(mode):
    start = mode-1
    modeList = []
    x = 0
    while(len(modeList)<7):
        modeList.append(List[(start+x)%7])
        x = x+1

    return modeList

    
    
