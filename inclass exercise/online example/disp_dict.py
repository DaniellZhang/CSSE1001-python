def display_dictionary(dictionary) :
    """Pretty print 'dictionary' in key sorted order.

    Parameters:
        dictionary dict<str:int>: Dictionary to be pretty printed.
    """
    keys = dictionary.keys()
    keys = sorted(keys)
    for k in keys :
        print('{0}  :  {1}'.format(repr(k), dictionary[k]))
