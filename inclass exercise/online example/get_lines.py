def get_lines(filename) :
    """Return a dictionary containing each line in the file as values
    and the corresponding line number as keys.

    Parameters:
        filename (str): Name, including path, of the file to be opened.

    Return:
        dict<int:str>: Dictionary containing the contents of the file.

    Preconditions:
        'filename' is the name of a file that can be opened for reading.
    """
    lines = {}
    f = open(filename, 'r')
    for i, line in enumerate(f) :
        lines[i] = line.strip()
    f.close()
    return lines
