import random

def randomIP():
    while True:
        a = random.randint(0,255)
        b = random.randint(0,255)
        c = random.randint(0,255)
        d = random.randint(0,255)
        if not (
                (a == 10) or
                (a == 172 and 16 <= b <= 31) or
                (a == 192 and b == 168) or
                (a == 127) #i dont know why but most 127 who respond are down
            ):
            return(str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d))
    

