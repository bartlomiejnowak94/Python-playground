suma = 9
lista = [1,3,5,6,11,23]

def sumdoub(suma,lista):
    suma_check = lista[0]
    for j in lista:
        for i in lista:
            suma_check = j
            suma_check += i
            if suma_check == suma:
                print(i, j)
                break
        else:
            continue
        break

sumdoub(suma,lista)