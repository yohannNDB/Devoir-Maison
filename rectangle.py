# Créé par 33645, le 16/10/2022 en Python 3.7


from array import*
tab = [ \

         [1, 0, 0, 1], \

         [1, 1, 1, 1], \

         [1, 0, 1, 1], \

         [1, 0, 1, 1] \

     ]

print(tab[0].index(1))
print(tab[1][0])
list_rec = []

def search_for_rec(i,tab,t):
    if tab == [0,None,[]]:
        return list_rec
    else:
        try:
            if i in tab[0] and tab[1]:
                x1 = array.index(i,tab[0])
                x2 = array.index(i[x1 +1[tab]])
                x3 = array.index(i,tab[1])
                x4 = tab[1].index(i[x3 +1[tab]])

                y1 = tab[1].index(i)
                y2 = tab[1].index(i)
            return 0
        except ValueError:
            pass


            if x1 == y1 and x2 == y2:
                print("Les coordonnées des sommets du rectangle",t, "sont :", (x,y))
                rec[t] = (x1,y2)
                list_rec.append(rec[t])
            else:
                search_for_rec(1,tab[+1],t + 1)
        else:
            search_for_rec(1,tab[+1],t + 1)






