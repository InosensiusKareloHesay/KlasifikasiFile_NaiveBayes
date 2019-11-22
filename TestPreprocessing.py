import os
from Preprocessing import Preprocessing

directory = input('Masukkan directory folder tempat file yang akan dibaca: ')

for file in os.listdir(directory):
    if file.lower().endswith('.txt') and not file.startswith('._'):
        Openfile = open(directory + '/' + file, 'r', encoding="ISO-8859-1")
        IsiFile = Openfile.read()
        Openfile.close()
        term = Preprocessing.cleaning(IsiFile)
        #print(term)
        term = Preprocessing.case_folding(term)
        #print(term)
        term = Preprocessing.tokenisasi(term)
        #print(term)
        term = Preprocessing.filtering(term)
        #print(term)
        term = Preprocessing.stemming(term)
        #print(term)
        #print('\nTERM PREPROCESSING : \n' + str(term))
