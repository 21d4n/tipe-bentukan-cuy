# Nama File     : point.py
# Deskripsi     : Tipe data point
# Nama / NIM    : Dehar Zaidan Dzaki Amirullah / 24060124130099
# Tanggal       : 30/10/2024

# ------------------------------------------------- SELEKTOR ---------------------------------------------------

def absis(P):
    return P[0]

def ordinat(P):
    return P[1]

def Titik1(G):
    return G[0]

def Titik2(G):
    return G[1]

# ------------------------------------------------- KONSTRUKTOR ---------------------------------------------------

def MakePoint(x,y):
    return [x,y]

def MakeGaris(P1,P2):
    return [P1,P2]

# ------------------------------------------------- OPERATOR ---------------------------------------------------

def Gradien(G):
    return (ordinat(Titik2(G)) - ordinat(Titik1(G))) / (absis(Titik2(G)) - absis(Titik1(G)))

def PanjangGaris(G):
    return ((absis(Titik2(G)) - absis(Titik1(G))) ** 2 + (ordinat(Titik2(G)) - ordinat(Titik1(G))) ** 2)**(1/2)

# ------------------------------------------------- PREDIKAT ---------------------------------------------------

def IsSejajar(G1,G2):
    return Gradien(G1) == Gradien (G2)

def IsTegakLurus(G1,G2):
    return Gradien(G1) * Gradien(G2) == -1

# ------------------------------------------------- NOTFUNG---------------------------------------------------

# TYPE POINT
# DEFINISI DAN SPESIFIKASI TYPE
# type point : < x: real, y: real >
#   {<x,y> adalah sebuah point, dengan x adalah absis dan y adalah ordinat}
# type garis : < P1: point, P2: point >
#   {<P1,P2> adalah sebuah garis yang menghubungan P1 (titik 1) dengan P2 (titik 2)}
# 
# DEFINISI DAN SPESIFIKASI SELEKTOR
# absis : point --> real
#   {absis(P) memberikan absis point P}
# ordinat : point --> real
#   {ordinat(P) memberikan ordinat point P}
# titik1 : garis --> point 
#   {titik1(G) memberikan point 1 dari garis G}
# titik2 : garis --> point
#   {titik2(G) memberikan point 2 dari garis G}
# 
# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePoint : 2 real --> point
#   {MakePoint(x,y) membentuk sebuah point dengan x sebagai absis dan y sebagai ordinat}
# MakeGaris : 2 point --> garis
#   {MakeGaris(P1,P2) membentuk sebuah garis dari P1 hingga P2}
# 
# DEFINISI DAN SPESIFIKASI OPERATOR
# Gradien : garis --> real
#   {Gradien(G) menghitung gradien dari garis G}
# PanjangGaris : garis --> real
#   {PanjangGaris(G) menghitung panjang dari garis G}
# 
# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSejajar?: 2 garis --> boolean
#   {IsSejajar?(G1,G2) true jika gradien G1 = Gradien G2}
# IsTegakLurus?: 2 garis --> boolean
#   {IsTegakLurus?(G1,G2) true jika gradien G1 * Gradien G2 = -1}