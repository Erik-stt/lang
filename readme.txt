The function ”read_train.py” shall be fed with a europarl7-file. The second argument can be named anything. The file will contain around 860689 lines. The lines to be parsed can be inserted in a new .txt-file. After that, paste the following command in Terminal:

java -Xmx2g -cp "*" edu.stanford.nlp.parser.nndep.DependencyParser \
    -model edu/stanford/nlp/models/parser/nndep/english_UD.gz \
    -textFile data/english-onesent.txt -outFile data/english-onesent.txt.out

The file ending in .out is the output file. It is the input file for the class Classify in the code label.py (unigrams) or bigram.py. It returns a list of dictionaries, and the dictionaries corresponds to the sentences. To have bigrams returned instead of unigrams, use the file bigram.py. The L1 class in L1.py takes two arguments: the list of dictionaries, and a list of labels, which has to be created separately. In the L1-code, the following calls produce a list of labels from the file with 100 sentences (the files following the hashtag produce a list of two languages):

from label import Classify
c = Classify("train3.txt") #"outCS-SV.txt"
a = c.obj_create()
l1 = L1(a, "train3_label.txt") #"labels.txt"
l1.data_input(a)
l1.lang_input("train3_label.txt") #"labels.txt"
l1.log_obj()
c1 = Classify("test.txt") #"test2.txt"
a1 = c1.obj_create()
l1.data_input(a1)
l1.lang_input("test1_label.txt") #"test2_label.txt"
l1.log_obj()
l1.predict_lang(a1)

The input files can be chosen freely.

Erik Hidmark

Footnote:

The java command comes from README.TXT. from the unzipped file: stanford-parser-full-2017-06-09. Downloaded from https://nlp.stanford.edu/software/lex-parser.shtml. Requires Java 8.
