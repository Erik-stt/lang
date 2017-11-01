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


   
    
                    
            
        
