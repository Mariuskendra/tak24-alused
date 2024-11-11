#Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks.
#Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi.
#Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida.
#Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)

def classify_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b == c:
            return "võrdhaarne kolmnurk"
        elif a == b or a == c or b == c:
            return "võrdhaarne kolmnurk"
        else:
            return "erikülgne kolmnurk"
    else:
        return "kolmnurk ei saa eksisteerida"
        
a = float(input("Sisesta esimese külje pikkus: "))
b = float(input("Sisesta teise külje pikkus: "))
c = float(input("Sisesta kolmanda külje pikkus: "))

triangle_type = classify_triangle(a, b, c)
print(triangle_type)