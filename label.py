"""Takes a number of parsed sentences as input and returns a list of
dictionaries, where each dictionary corresponds to a sentence and contains
the frequencies of unigrams, where each unigram is a grammatical relation.
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
            sentence_list.append(dependencies)
        l = []
        
        for sentence in sentence_list:
            d = {}
            for dependency in sentence:
                d[dependency] = 1
            l.append(d)
        for affix in l:
            if '-' in affix:
                del affix['-']
            if '' in affix:
                del affix['']
            if 'punct(' in affix:
                del affix['punct(']
                affix['punct'] = 1
        print(l[0])
        return l
