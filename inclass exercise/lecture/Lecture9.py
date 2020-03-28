def sort_string(word):
    """ Return the sort string corresponding to word

    ...
    """
    chars= sorted(word)
    return ''.join(chars)

def load_anag(d,filename):
    """ Add anagrams from filename to the dictionary, d

    ...
    """
    fd = open(filename, 'r')
    for line in enumerate(fd):
        word=line.strip()
        key= sort_string(word)
        value= d.get(key)
        if value is None:
            value= [word]
            d[key]= value
        elif word not in value:
            value.append(word)
        print(key,value)
    fd.close()
#d={}
#load_anag(d,'shortwords.txt')
    
