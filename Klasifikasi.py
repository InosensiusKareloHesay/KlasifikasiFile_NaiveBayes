import numpy as np
from Weighting import Weighting
from Preprocessing import Preprocessing

obj = Weighting()
pre = Preprocessing()
feature = []
featureTes = []
rawGlo = []
rawGloTes = []
dataTrain = []
kelas = []

class Klasifikasi:

    def train(listDoc, listFolder):
        fitur = obj.getFeature()
        for i in range(int(len(fitur))):
            feature.append(fitur[i])
        raw = obj.getTF()
        for i in range(int(len(raw))):
            for j in range(int(len(raw[0]))):
                rawGlo.append(raw[i][j])
        raw = np.array(rawGlo)
        raw = raw.reshape(int(len(feature)), int(len(listDoc)))
        conditionalProb = []
        conditionalProbKategori = []

        print("Fase Training")

        #menghitung conditional probabilitas tiap dokumen
        for i in range(int(len(listDoc))):
            total = 0
            for j in range(len(raw)):
                total += raw[j][i]
            conditionalProb.append(total)
        print('CP = ',conditionalProb)

        #mencari folder apa saja yang tersedia untuk klasifikasi
        for i in range(int(len(listFolder))):
            if listFolder[i] not in kelas:
                kelas.append(listFolder[i])
        print('JK = ',kelas)

        #menghitung total term tiap class
        jumlahDoc = int(int(len(listDoc)) / int(len(kelas)))
        for i in range(int(len(kelas))): #jumlah folder/macam klasifikasi
            total = 0
            for j in range(jumlahDoc): #jumlah doc tiap klasifikasi
                total += conditionalProb[(i*3)+j]
            conditionalProbKategori.append(total)
        print('CPK = ',conditionalProbKategori)

        #Menghitung nilai probability dari masing masing class
        for i in range(int(len(feature))):
            for j in range(int(len(kelas))):
                count = 0;
                for k in range(int(len(listDoc))):
                    if(listFolder[k]==kelas[j]):
                        count += raw[i][k]
                dataTrain.append((count+1)/(conditionalProbKategori[j]+int(len(feature))))
        print(dataTrain)
        nilaiProb = np.array(dataTrain)
        nilaiProb = nilaiProb.reshape(int(len(feature)), int(len(kelas)))
        print("Conditional Probability Tiap Kategori \n",nilaiProb)

    def test(listDoc):
        fitur = obj.getFeature()
        for i in range(int(len(fitur))):
            featureTes.append(fitur[i])
        raw = obj.getTF()
        for i in range(int(len(raw))):
            for j in range(int(len(raw[0]))):
                rawGloTes.append(raw[i][j])
        kategori = []
        hasilTest = []
        raw = np.array(rawGloTes)
        raw = raw.reshape(int(len(fitur)), int(len(listDoc)))
        data = np.array(dataTrain)
        data = data.reshape(int(len(feature)), int(len(kelas)))
        for i in range(int(len(kelas))):
            kategori.append((len(listDoc)/len(kelas))/len(listDoc)) #jumlah doc kelas itu / jumlah doc total
        for i in range(int(len(listDoc))): #panjang doc
            nilai = []
            for c in range(int(len(kelas))): #panjang kelas
                nilai.append(kategori[c])
            for j in range(int(len(feature))): #panjang feature latih
                if (j > int(len(featureTes))-1): #untuk membatasi perulangan supaya tidak lebih dari panjang axis 0 dari raw
                    break
                if (raw[j][i] != 0):
                    for k in range(int(len(feature))):
                        if(featureTes[j] == feature[k]): #mencari temp yang sama dari tes dan latih
                            for l in range(int(len(kelas))):
                                nilai[l] *= (raw[j][i]*data[k][l])
            print(nilai)
            cek = 0 #untuk mencari nilai tebesar
            cekClass = 0 #untuk mencari jenis class yang paling sesuai
            print(len(nilai))
            for l in range(len(nilai)):
                if(cek < nilai[l]):
                    cek = nilai[l]
                    cekClass = l
            hasilTest.append(kelas[cekClass])
        return hasilTest

    def hitungAkurasi(asli,tes):
        counter = 0
        for i in range(int(len(asli))):
            if(asli[i]==tes[i]):
                counter += 1
        akurasi = (counter/int(len(asli)))*100
        return akurasi

