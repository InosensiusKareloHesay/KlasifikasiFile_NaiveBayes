import numpy as np
import math

doc = []
doc2 = []
kata = []
kata2 = []
TF = []
TFIDF = []
counter = []
class Weighting:

    def setText(stem):
        count = 1
        if(len(counter)==0):
            for i in stem:
                #print('d', count,' : ',i, '\n')
                doc.append(i)
                count += 1
        if(len(counter)>0):
            for i in stem:
                #print('d', count,' : ',i, '\n')
                doc2.append(i)
                count += 1

    def getTF(self):
        tf = []
        if(int(len(counter))==0):
            for i in kata:
                for j in range(len(doc)):
                    c = 0
                    for k in doc[j]:
                        if i == k:
                            c += 1
                    tf.append(c)
            tf_ar = np.array(tf)
            tf_ar = tf_ar.reshape(len(kata), len(doc))
            counter.append(1)
            return tf_ar
        if (int(len(counter)) > 0):
            for i in kata2:
                for j in range(len(doc2)):
                    c = 0
                    for k in doc2[j]:
                        if i == k:
                            c += 1
                    tf.append(c)
            tf_ar = np.array(tf)
            tf_ar = tf_ar.reshape(len(kata2), len(doc2))
            return tf_ar

    def getFeature(self):
        if (int(len(counter)) == 0):
            for i in range(len(doc)):
                for j in range(len(doc[i])):
                    if doc[i][j] not in kata:
                        kata.append(doc[i][j])
            return kata
        if (int(len(counter)) > 0):
            for i in range(len(doc2)):
                for j in range(len(doc2[i])):
                    if doc2[i][j] not in kata2:
                        kata2.append(doc2[i][j])
            return kata2

    def getTFIDF(self):
        TF = Weighting.getTF(self)
        TFsementara = np.array(TF).ravel()
        df = []
        for i in range(len(TF)):
            c = 0
            for j in range(len(TF[i])):
                if TF[i][j] != 0:
                    c += 1
            df.append(c)
        d = 0
        e = 0
        for i in range(len(TFsementara)):
            if(TFsementara[i]==0):
                TFIDF.append(TFsementara[i])
            else:
                TFIDF.append((1+math.log10(TFsementara[i]))*(math.log10(len(TF[0])/df[e])))
            d += 1
            if(d%len(TF[0])==0):
                e += 1
        tfidf_ar = np.array(TFIDF)
        tfidf_ar = tfidf_ar.reshape(len(TF), len(TF[0]))
        return tfidf_ar
