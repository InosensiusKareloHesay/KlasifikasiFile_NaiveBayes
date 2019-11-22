from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
from string import digits

class Preprocessing:

    #Melakukan Cleaning
    def cleaning(kalimat):
        #print('\nPROSES CLEANING : ')
        remove_digits = str.maketrans('', '', digits)
        res = kalimat.translate(remove_digits)
        return re.sub(r'[^a-zA-Z]', " ",res)

    #Melakukan Case-Folding
    def case_folding(kalimat):
        #print('\nPROSES CASE FOLDING : ')
        return kalimat.lower()

    #Melakukan Tokenisasi
    def tokenisasi(token):
        #print('\nPROSES TOKENISASI : ')
        return word_tokenize(token)

    #Melakukan Filtering
    def filtering(filter):
        #print('\nPROSES FILTERING : ')
        stopwords = open("stopword_list_tala.txt", "r")
        stopwords = stopwords.read()
        stopwords = stopwords.split("\n")
        for i in range(int(len(filter))):
            for text in filter:
                for word in stopwords:
                    if text == word:
                        filter.remove(text)
        return filter

    #Melakukan Stemming
    def stemming(steaming):
        #print('\nPROSES STEMMING : ')
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        output = stemmer.stem(str(steaming))
        terms =[]

        for word in output.split(" "):
            if word not in terms:
                terms.append(word)
        return terms

