# 7 segmentli bir sayıyı tam sayıya çevirme
# Convert a 7-segment number to an integer
# seg fonksiyonuna sırası ile 1,2 ve 3. satırı giriyoruz.
# We enter lines 1,2 and 3 respectively in seg function.
# Örnek/example: seg("    _  _     _  _  _  _  _ ","  | _| _||_||_ |_   ||_||_|","  ||_  _|  | _||_|  ||_| _|") #123456789
def seg(a,b,c):
    olası = []
    atlama = 0
    gecme = 0

    abc = ""
    zp = zip(a, b, c)
    for i in zp:
        d = i[0] + i[1] + i[2]
        if atlama != 0:
            atlama -= 1
            continue
        elif d == "   " and gecme != 0:
            abc += "1"
            atlama = 1
            olası = []
            gecme = 0
            continue
        elif d == "   ":
            olası = [1, 3, 7]
            gecme = 1
            continue
        elif d == "___" and 3 in olası:
            abc += "3"
            gecme = 0
            atlama = 1
            olası = []
            continue
        elif d == "_  " and 7 in olası:
            abc += "7"
            gecme = 0
            atlama = 1
            olası = []
            continue
        elif d == "  |" and 5 in olası:
            abc += "5"
            olası = []
            continue

        elif d == " | ":
            olası = [4, 5, 9]
            continue
        elif d == " _ " and 4 in olası:
            abc += "4"
            atlama = 1
            olası = []
            continue
        elif d == "___" and 5 in olası:
            olası = [5, 9]
            continue

        elif d == " ||" and 9 in olası:
            abc += "9"
            olası = []
            continue
        elif d == " ||" and 8 in olası:
            abc += "8"
            olası = []
            continue
        elif d == " ||":
            olası = [6, 8]
            continue
        elif d == "___" and 6 in olası:
            continue
        elif d == "  |" and 6 in olası:
            abc += "6"
            olası = []
            continue
        elif d == "  |":
            abc += "2"
            atlama = 2
            continue
    return abc
