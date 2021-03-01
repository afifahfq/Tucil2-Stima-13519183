# Nama : Afifah Fathimah Qur'ani
# NIM : 13519183
# Kelas : K-04

from collections import defaultdict
import os
import sys

# KELAS
class Graph :
    def __init__ (self, countV): #constructor
        self.names = []
        self.graph = defaultdict(list) 
        self.vertices = countV #jumlah simpul
    
    def addName(self, x, y): #re-assign nama node
        names[x] = y

    def addEdge(self, u, v): 
        self.graph[u].append(v) 

    def delEdge(self, x): #hapus edge antara node x node y
        for item in self.graph:
            if (x in self.graph[item]):
                self.graph[item].remove(x)

    def addNode(self, x): #tambah node
        self.names.append(x)
        self.vertices += 1

    def delNode(self): #hapus node dan seluruh edge yg terhubung
        count = 0
        for i in printed:
            if i in self.graph:
                del self.graph[i]
                count += 1
            self.delEdge(i)
        self.vertices -= count

    def topologicalSort(self):
        result = [] #inisialisasi stack
        keys = [*g.graph]
        values = [*g.graph.values()]

        # Key tanpa values (matakuliah tanpa prereq)
        for list in values:
            for item in list:
                if (item not in g.graph.keys() and item not in result):
                    result.append(item)
                    self.vertices -= 1

        checked = [0 for i in range(self.vertices)] #set nodes false (belum dilalui)

        for i in range(len(keys)):
            if checked[i] == 0:
                self.recursiveTopological(keys, values, i, checked, result)
        
        return (result)

    def recursiveTopological(self, keys, values, i, checked, result):
        checked[i] = 1
        
        for j in [*g.graph.values()][i]:
            if (j not in keys): # jika mata kuliah tidak ada prereq
                continue
            if checked[keys.index(j)] == 0:
                self.recursiveTopological(keys, values, keys.index(j), checked, result)
        
        result.append(keys[i])

#PROGRAM UTAMA 

# Membuka file txt
filename = input("Masukkan nama file: ")
file = open(os.path.join(sys.path[0], filename), "r")

# Membaca file per line
lines = file.read().splitlines()

# Inisialisasi graph
countV = 0
for i in lines: # Hitung jumlah vertices (asumsi jmlh lines = jml vertices)
    if i:
        countV += 1
g = Graph(countV)

# Meng-assign isi line menjadi atribut graph
for i in range(len(lines)):
    lines[i] = lines[i].split(', ') # Membagi isi line menjadi list of string
    lines[i][-1] = lines[i][-1].replace('.', '')

# Buat edges
for i in range(len(lines)):
    for j in range(1, len(lines[i])):
        g.addEdge(lines[i][0], lines[i][j])

# Panggil topological sort
result = g.topologicalSort()

# Print hasil
printed = []
for i in range(8):
    print("Semester", i+1, ":")
    for j in result:
        if (j not in g.graph): # matakuliah tanpa prereq
            printed.append(j)
            print(j)
        elif (i > 0):
            # cek apakah matakuliah masih ada di keys
            check = (any(item in g.graph for item in g.graph[j]))
            if (check==False):
                printed.append(j)
                print(j)
            else:
                continue

    result = [x for x in result if x not in printed]
    g.delNode() # hapus key yang sudah di print