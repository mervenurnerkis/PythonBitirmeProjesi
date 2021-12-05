#proje1
#1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:
#input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
#output: [1,'a','cat',2,3,'dog',4,5]

def flatten(list):
    flatten_list = []
    for eleman in list:
        if type(eleman) != type([]):
            flatten_list.append(eleman)
        else:
            flatten_list.extend(flatten(eleman))
    return flatten_list
 
 #Proje-2
 #Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:
#input: [[1, 2], [3, 4], [5, 6, 7]]
#output: [[[7, 6, 5], [4, 3], [2, 1]]

l = []
def ters(l):
    for i in range(len(l)):
        l.reverse()
        for i in range(len(l)):
            l[i].reverse()
            
        return l

