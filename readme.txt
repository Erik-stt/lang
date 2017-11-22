This software contains the following modules:
read_train.py
label.py
bigram.py
L1.py
L1_bigram.py

The translated sentences requires a login to mumin.ling.su.se. It is found in /home/corpora/europarl7 
and is called english-sourcelang.train.bz2. The free parser is found
at https://nlp.stanford.edu/software/lex-parser.shtml and is called 
stanford-parser-full-2017-06-09. To run it, Java 8 is required (JDK 1.8.0+).
If the "java -version" command returns 1.8+ it will be working. 

To run the code, follow these steps.

1)separate language tags from sentences: in the python interpreter, write 
from read_train import read_train
and then 
read_train(”input_file.txt”, ”output_file.txt”)
2)parse text: java -Xmx2g -cp "*" edu.stanford.nlp.parser.nndep.DependencyParser \
    -model edu/stanford/nlp/models/parser/nndep/english_UD.gz \
    -textFile data/output_file.txt -outFile data/output_file.txt.out
3)train and test classifier with unigrams: python L1.py
4)train and test classifier with bigrams: python L1_bigram.py

Erik Hidmark
