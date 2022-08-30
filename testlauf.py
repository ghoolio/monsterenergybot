alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
counter = 0

#zähler soll von 0 bis 26 laufen
#wenn zähler bei 23

vergleich = 26


if(counter >= 22):
    counter = counter - 22
else:
    for counter in range(0,25,3):
        print(alphabet[counter])
    
        


