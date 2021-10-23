import random

#///////////////////////////////////
#////////Lanceur de dés ////////////
#///////////////////////////////////
d1 = random.randint(1,6)
d2 = random.randint(1,6)
d3 = random.randint(1,6)
d4 = random.randint(1,6)
ensemble = [d1,d2,d3,d4]

def lanceur():
    d1 = random.randint(1,6)
    print(d1)
    d2 = random.randint(1,6)
    print(d2)
    d3 = random.randint(1,6)
    print(d3)
    d4 = random.randint(1,6)
    print(d4)

def lanceur_tru():
        totalus = sum(ensemble)-min(ensemble)
        d1 = random.randint(1,6)
        if d1 < 2: 
            truc = random.randint(1,100)
            print(truc)
            if truc > 80 :
                d1 = 6
            print("Yes")
                #print(d1)
            else :
                d1 = 1 #print("alors?")
        else :
            #print(d1)
        d2 = random.randint(1,6)
        print(d2)
        d3 = random.randint(1,6)
        print(d3)
        d4 = random.randint(1,6)
        print(d4)

        
lanceur_tru()