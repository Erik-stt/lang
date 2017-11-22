"""Reads the english-sourcelang.train.bz2-file and outputs a file where
the tags are stripped from the sentences.
"""
import re

def read_train(file, outfile):
    c = 0
    with open(file, 'r') as f, open(outfile, 'w') as fout:
        for line in f:
            
            c += 1
            x = re.findall(r'.*?([A-Z][A-Z])(.*(?:\.|!|\?|.)).*?', line)
            
            for tup in x:
                a, b = tup
                
                b = b.lstrip("\t")
                r = re.findall(r'(.+\.)\s', b)
                for string in r:
                    print(string, file=fout)
    print(c)
    
"""
These are the line IDs where a new language is found in the output-file.
"CS": #1
"DA": #6732
"DE": #23300
"EL": #164377
"EN": #194720
"ES": #403133
'ET': #461524
"FI": #461823
"FR": #481819
"HU": #604268
"IT": #609656
"LT": #660849
'LV': #666209  
'MT': #666637
"NL": #666687
"PL": #739767
"PT": #759783
"RO": #810203
"SK": #817946
"SL": #820377
"SV": #821054
"""


   
    
                    
            
        
