import os
from Preprocessing import Preprocessing
from Weighting import Weighting
from Klasifikasi import Klasifikasi
dok = []
dokTes = []
obj = Weighting()
listDoc = []
listDocTes =[]
listFolder = []
listFolderTes = []
directory = input('Masukkan directory folder tempat file training : ')

for folder in os.listdir(directory):
    new_direc = directory+'//'+folder
    for file in os.listdir(new_direc):
        if file.lower().endswith('.txt') and not file.startswith('._'):
            listFolder.append(folder);
            Openfile = open(new_direc + '/' + file, 'r', encoding="ISO-8859-1")
            IsiFile = Openfile.read()
            listDoc.append(file)
            Openfile.close()
            term = Preprocessing.cleaning(IsiFile)
            #print(term)
            term = Preprocessing.case_folding(term)
            #print(term)
            term = Preprocessing.tokenisasi(term)
            #print(term)
            term = Preprocessing.filtering(term)
            #print(term)
            dok.append(term)
            term = Preprocessing.stemming(term)
            #print(term)
            #print('\nTERM PREPROCESSING : \n' + str(term))

Weighting.setText(dok)
Klasifikasi.train(listDoc, listFolder)

directoryTes = input('Masukkan directory folder tempat file testing : ')
for folder in os.listdir(directoryTes):
    new_direcTes = directoryTes+'//'+folder
    for file in os.listdir(new_direcTes):
        if file.lower().endswith('.txt') and not file.startswith('._'):
            listFolderTes.append(folder);
            Openfile = open(new_direcTes + '/' + file, 'r', encoding="ISO-8859-1")
            IsiFileTes = Openfile.read()
            listDocTes.append(file)
            Openfile.close()
            termTes = Preprocessing.cleaning(IsiFileTes)
            #print(termTes)
            termTes = Preprocessing.case_folding(termTes)
            #print(termTes)
            termTes = Preprocessing.tokenisasi(termTes)
            #print(termTes)
            termTes = Preprocessing.filtering(termTes)
            #print(termTes)
            dokTes.append(termTes)
            termTes = Preprocessing.stemming(termTes)
            #print(termTes)
            #print('\nTERM PREPROCESSING : \n' + str(termTes))

Weighting.setText(dokTes)
hasilTest = Klasifikasi.test(listDocTes)
print('Klasifikasi hasil testing\n',hasilTest)
akurasi = Klasifikasi.hitungAkurasi(listFolderTes,hasilTest)
print('Akurasi : ',akurasi)