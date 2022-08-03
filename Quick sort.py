#quick sort version 1
#pierwszy typ quciksortu

#Opiera się na metodzie dziel i zwyciężaj
#logarytmiczna złożoność czasowa O(log(n))

# algorithm uses divide and conquer scheme
# time complexity: O(log(n))


def sorotwanie_szybkie(tablica):
    mniejsze=[]
    rowne=[]
    wieksze=[]

    if len(tablica)>1:
        piwot=tablica[0] #granica//liczba według której sortujemy wszystkie mniejesze na lewo większe na prawo
        for i in tablica:
            if i>piwot:
                wieksze.append(i)
            elif i<piwot:
                mniejsze.append(i)
            elif i==piwot:
                rowne.append(i)

        return sorotwanie_szybkie(mniejsze)+rowne+sorotwanie_szybkie(wieksze) #gdy chemy zmienić kolejność starczy zamienić rekurencyjne wywołania mniejszych,większych
    else:
        return tablica

A=[6,17,2,61,64,22,1,23,4,612,8,94,2,4,3,34,55,9,111]

print(A)
print('sorted version 1:',sorotwanie_szybkie(A))

#quciksort version 2
#second version is based on moving values to the left or right of your pivot

#sortowanie szybkie typ 2
#potrzebujemy dwóch funkcji

#USTAWIANIE WZGLĘDEM OSI

def ustawianie_wz_osi(tab,lewy,prawy):
    i=lewy-1
    os=tab[prawy]

    for j in range(lewy,prawy):
        if tab[j]<os:
            i+=1
            tab[i],tab[j]=tab[j],tab[i]

    tab[i+1],tab[prawy]=tab[prawy],tab[i+1]
    return i+1

def sort_szybkie(tab,lewy,prawy):
    if lewy<prawy:
        pop_indeks=ustawianie_wz_osi(tab,lewy,prawy)
        sort_szybkie(tab,lewy,pop_indeks-1)
        sort_szybkie(tab,pop_indeks+1,prawy)


B=[21,79,10,214,31,1,5,2,12,213,32,26,74,126,4,7,8,11,13,15,33,3]

print(B)
print('sorted version 2:',sorotwanie_szybkie(B))