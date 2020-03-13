import ScaleNotes as SN
import ModeSelect as MS

Note = input("Note(in capital): ")

OctaveList = SN.Octave_of_Note(Note)

Mode = int(input("Mode(1 to 7): "))

ModeList   = MS.selectMode(Mode)

def Scale_in_Mode():
    List = []
    pos_in_octave = 0
    List.append(Note)
    for x in ModeList:
        if (x == 'W'):
            move = 2 
        elif (x == 'H'):
            move = 1
        pos_in_octave = pos_in_octave + move
        List.append(OctaveList[pos_in_octave])

    return List

print("The scale for ",Note," in mode ",Mode," is:\n")
print(Scale_in_Mode())
    
