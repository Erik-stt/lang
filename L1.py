"""Trains a model and tests it on translated sentences to find the source
language. It is based on unigrams.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer 
from sklearn import preprocessing
from label import Classify

class L1(object):
    def __init__(self, affixes, labels):
        self.affixes = affixes #list
        self.labels = labels
        self.affixes_list = []
        self.label_list = [] #test data is saved here as well
        self.log_lst = [] #the log-object is stored here for later use in
        #predict_lang
        self.log_lst_test = []
        self.d = DictVectorizer()
        self.label = preprocessing.LabelEncoder()
        self.log = LogisticRegression()

    def data_input(self, affixes): #stores list of dictionaries
        if len(self.affixes_list) == 0:
            self.affixes_list.append(self.affixes)
        else:
            self.affixes_list.append(affixes)

    def lang_input(self, tags):
        if len(self.label_list) == 0:
            f = open(self.labels)
            languages = []
            for line in f:
                languages.append(line)
            self.label_list.append(languages)
            f.close()
        else:
            f = open(tags)
            languages = []
            for line in f:
                languages.append(line)
            self.label_list.append(languages)
            f.close()

    def log_obj(self):
           

        if len(self.log_lst) == 0:
            self.affixes_train = self.d.fit_transform(self.affixes_list[0])  
            self.labels = self.label.fit_transform(self.label_list[0])
            self.log = self.log.fit(self.affixes_train, self.labels)
            self.log_lst.append(self.log)
        else:
            for obj in self.log_lst:
                self.affixes_test = self.d.fit_transform(self.affixes_list[1])

                self.labels = self.label.fit_transform(self.label_list[1])
                self.test_obj = obj.fit(self.affixes_test, self.labels)
                self.log_lst_test.append(self.test_obj)


    def predict_lang(self, sentence_aff):
        data = self.d.fit_transform(sentence_aff)
        self.out = []
        for log in self.log_lst:
            
            obj = log.predict(data)
            output = self.label.inverse_transform(obj)
            self.out.append(output)
        print(accuracy)
        print(self.out)
        print(self.label_list[1])
        return self.out

def main():
    c = Classify("train3.txt") #"trainout.txt"
    a = c.obj_create()
    l1 = L1(a, "train3_label.txt") #"train_label.txt"
    l1.data_input(a)
    l1.lang_input("train3_label.txt") #"train_label.txt"
    l1.log_obj()
    c1 = Classify("test.txt") #"testout.txt"
    a1 = c1.obj_create()
    l1.data_input(a1)
    l1.lang_input("test1_label.txt") #"test_label.txt"
    l1.log_obj()
    l1.predict_lang(a1)

if __name__ == "__main__":
    main()
