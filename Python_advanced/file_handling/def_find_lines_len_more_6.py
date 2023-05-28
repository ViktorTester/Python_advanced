def find_lines_len_more_6(file_name:str) -> int:
    """The function takes a filename and finds the
    number of lines greater than 6 characters."""
    with open(file_name, encoding='utf-8') as file:
        line = file.readline()
        counter = 0
        while line != '':
            if len(line.strip()) > 6:
                counter += 1
            line = file.readline()
    return counter