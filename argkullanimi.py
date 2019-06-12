#argumanlar 1
def arguman_listele(header,*args):
    print(header)
    for metin in args:
        print(metin)

arguman_listele("baslik","arg1","arg2","arg3",4,5,6)


#argumanlar 2 (argumana çevirme işlemi)
def arguman_listele2(header,*args):
    print(header)
    for metin in args:
         print(metin)

argumanlar =["arg1","arg2","arg3",4,5,6]

arguman_listele2("baslik",*argumanlar,argumanlar)
