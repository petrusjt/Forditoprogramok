from domol_automat import DomolAutomat
import sys
#Convert an array of 0s and 1s to an array of False and True values respectively
def convert(arr):
    new_arr = []
    for item in arr:
        new_arr += [True if item == 1  else False]
    return new_arr

alphabet = ["letter", "number", "{", "}", "(", "*", ")", ":", "=", "<", ">", "space", "other", "$"]
state_transition = [[],
[2,4,6,19,8,19,19,12,19,14,17,1,19,21],
[2,2,3,3,3,3,3,3,3,3,3,3,3,3], 
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[5,4,5,5,5,5,5,5,5,5,5,5,5,5],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[6,6,6,7,6,6,6,6,6,6,6,6,6,19],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[20,20,20,20,20,9,20,20,20,20,20,20,20,20,19],
[9,9,9,9,9,10,9,9,9,9,9,9,9,19],
[9,9,9,9,9,10,11,9,9,9,9,9,9,19],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[20,20,20,20,20,20,20,20,13,20,20,20,20,19],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[20,20,20,20,20,20,20,20,15,20,20,20,20,19],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[20,20,20,20,20,20,20,20,18,20,20,20,20,19],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[21,21,21,21,21,21,21,21,21,21,21,21,21,21]
]
backup = convert([0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
read   = convert([0,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,1,0,0])
d = DomolAutomat(alphabet,state_transition,1,[21],backup,read)
#print(d.validate("{én vagyok itt (* nem *)\} 12norbi12:=(* ez **nem*)>=131 erzsi$"))
if len(sys.argv) == 2:
    print("A lexikális elemző elfogadta a programkódot." if d.validate(sys.argv[1]) else "A lexikális elemző nem fogadta el a programkódot.")
    print("A lexikális elemző a(z) " + str(d.getState()) + ". állapotban állt meg.")
    print("A lexikális elemzés eredménye: ", d.getLexicalFormula())