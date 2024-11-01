# Nama File     : pecahan.py
# Deskripsi     : Tipe data pecahan
# Nama / NIM    : Dehar Zaidan Dzaki Amirullah / 24060124130099
# Tanggal       : 30/10/2024

# ------------------------------------------------- SELEKTOR ---------------------------------------------------

def bil(P):
    return P[0]

def nom(P):
    return P[1]

def den(P):
    return P[2]

def pemb(P):
    return P[0]

def peny(P):
    return P[1]

# ------------------------------------------------- KONSTRUKTOR ---------------------------------------------------

def MakePecahanC(b,n,d):
    return [b,n,d]

def MakePecahan(n,d):
    return [n,d]

# ------------------------------------------------- OPERATOR ---------------------------------------------------

def KonversiPecahan(P):
    return MakePecahan(bil(P) * den(P) + nom(P),den(P))

def KonversiReal(P):
    return nom(P) / den(P) + bil(P)

def KonversiPecahanc(P):
    return MakePecahanC(pemb(P) // peny(P), pemb(P) % peny(P), peny(P))

def AddP(P1,P2):
    return MakePecahanC(bil(P1) + bil(P2), nom(P1) * den(P2) + nom(P2) * den(P1), den(P1) * den(P2))

def SubP(P1,P2):
    return MakePecahanC(bil(P1) - bil(P2), nom(P1) * den(P2) - nom(P2) * den(P1), den(P1) * den(P2))

def MulP(P1,P2):
    return KonversiPecahanc(MakePecahan(pemb(KonversiPecahan(P1)) * pemb(KonversiPecahan(P2)), peny(KonversiPecahan(P1)) * peny(KonversiPecahan(P2))))

def DivP(P1,P2):
    return KonversiPecahanc(MakePecahan(pemb(KonversiPecahan(P1)) * peny(KonversiPecahan(P2)), pemb(KonversiPecahan(P2)) * peny(KonversiPecahan(P1))))

# ------------------------------------------------- PREDIKAT ---------------------------------------------------

def IsEqP(P1,P2):
    return KonversiReal(P1) == KonversiReal(P2)

def IsLtP(P1,P2):
    return KonversiReal(P1) < KonversiReal(P2)

def IsGtP(P1,P2):
    return KonversiReal(P1) > KonversiReal(P2)
print(DivP(MakePecahanC(1,1,2),MakePecahanC(1,1,2)))

# ------------------------------------------------- NOTFUNG ---------------------------------------------------

# TYPE PECAHAN
# DEFINISI DAN SPESIFIKASI TYPE
# type pecahanc : < b: integer, n: integer >= 0, d: integer > 0 >
#   {<b,n,d> adalah pecahan campuran, dengan b adalah bilangan bulat dari pecahan, n adalah
#    nominator (pembilang), d adalah denominator (penyebut)}
# type pecahan : < n: integer, d: integer > 0 >
#   {<n,d> adalah pecahan biasa, dengan n adalah nominator (pembilang), d adalah denominator (penyebut)}

# DEFINISI DAN SPESIFIKASI SELEKTOR
# bil : pecahanc --> integer
#   {bil(P) memberikan bilangan dari pecahan campuran P}
# nom : pecahanc --> integer >= 0
#   {nom(P) memberikan nominator atau pembilang dari pecahan campuran P}
# den : pecahanc --> integer > 0
#   {den(P) memberikan denominator atau penyebut dari pecahan campuran P}
# pemb : pecahan --> integer >= 0
#   {pemb(P) memberikan pembilang dari pecahan biasa P}
# peny : pecahan --> integer > 0
#   {peny(P) memberikan penyebut dari pecahan biasa P}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePecahanC : integer, integer >= 0, integer > 0 --> pecahanc
#   {MakePecahanC(b,n,d) membuat sebuah pecahan campuran dari bilangan bulat b, pembilang n, dan penyebut d}
# MakePecahan : integer, integer > 0 --> pecahan
#   {MakePecahan(n,d) membuat sebuah pecahan biasa dari pembilang n, dan penyebut d}

# DEFINISI DAN SPESIFIKASI OPERATOR
# KonversiPecahan : pecahanc --> pecahan
#   {KonversiPecahan(P) mengubah pecahan campuran P menjadi tipe pecahan biasa }
# KonversiReal : pecahanc --> real
#   {KonversiReal(P) mengubah pecahan campuran P menjadi bentuk real}
# KonversiPecahanC : pecahan --> pecahanc
#   {KonversiPecahanC(P) mengubah pecahan biasa P menjadi pecahan campuran}
# AddP : 2 pecahanc --> pecahanc
#   {AddP(P1,P2) menjumlahkan dua buah pecahan campuran P1 dan P2}
# SubP : 2 pecahanc --> pecahanc
#   {SubP(P1,P2) mengurangkan dua buah pecahan campuran P1 dan P2}
# MulP : 2 pecahanc --> pecahanc
#   {MulP(P1,P2) mengalikan dua buah pecahan campuran P1 dan P2}
# DivP : 2 pecahanc --> pecahanc
#   {DivP(P1,P2) membagi dua buah pecahan campuran P1 dan P2}

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEqP?: 2 pecahanc --> boolean
#   {IsEqP?(P1,P2) true jika P1 = P2, membandingkan apakah 2 buah pecahan sama nilainya}
# IsLtP?: 2 pecahanc --> boolean
#   {IsLtP?(P1,P2) true jika P1 < P2, membandingkan apakah P1 lebih kecil dari P2}
# IsGtP?: 2 pecahanc --> boolean
#   {IsEqP?(P1,P2) true jika P1 > P2, membandingkan apakah P1 lebih besar dari P2}