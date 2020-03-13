#Shashwat Vaibhav
noteList = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

def Octave_of_Note(param):
    pos =Search(param)
    newList =[]
    x= 0
    while(len(newList)<13):
        newList.append(noteList[(pos+x)%12])
        x = x+1
    return newList
def Search(param):
    pos = 0
    for x in noteList:
        if x == param:
            return pos
        pos = pos+1

