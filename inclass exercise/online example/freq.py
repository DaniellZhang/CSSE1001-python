def freq_count(filename):
    """Return the frequency count of characters occuring in a file.

    Parameters:
        filename (str): Name, including path, of the file to be opened.

    Return:
        dict<str:int>: Frequency of each character occuring in the file.

    Preconditions:
        'filename' is the name of a file that can be opened for reading.
    """
    freq = {}
    file = open(filename, 'r')
    for line in file :
        for char in line :
            freq[char] = freq.get(char, 0) + 1
    file.close()
    return freq
