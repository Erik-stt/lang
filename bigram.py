"""Takes a number of parsed sentences as input and returns a list of
dictionaries, where each dictionary corresponds to a sentence and contains
the frequencies of bigrams, where each bigram consists of grammatical relations
occuring next to each other.
"""
import re

class Classify(object):
    def __init__(self, dependencies):
        self.dependencies = dependencies
        

       

    def obj_create(self):
        dependency_list = []
        f = open(self.dependencies)
     
        for line in f:
        
            x = re.findall(r'(.+\().+', line)
            for string in x:
                dependency_list.append(string)
            if '(' not in line:
                dependency_list.append("-")
        f.close()
        

        input_syntax = str(dependency_list)
        input_syntax = input_syntax[2:-2]
    
        self.sentences_syntax = input_syntax.split("-', '")
    
        sentence_list = []
      
        for sentence in self.sentences_syntax:
            dependencies = sentence.split("(', '")
            del dependencies[-1]
            sentence_list.append(dependencies)
       
        l = []
        bigrams = []
        for sent in sentence_list:
            sent_bigram = []
            for i in range(len(sent)):
                try:
                    bigram = sent[i] + sent[i+1]
                    sent_bigram.append(bigram)
                except IndexError:
                    bigrams.append(sent_bigram)
                        
        for sentence in bigrams:
            d = {}
            for bigram in sentence:
                d[bigram] = 1
            l.append(d)
        for affix in l:
            if '-' in affix:
                del affix['-']
            if '' in affix:
                del affix['']
            if 'punct(' in affix:
                del affix['punct(']
                affix['punct'] = 1

        return l
