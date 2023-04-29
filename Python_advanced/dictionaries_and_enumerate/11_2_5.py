def merge(values):
    dct_final = {}

    for i in values:
        for k, v in i.items():
            if k not in dct_final:
                dct_final[k] = {v}
            else:
                dct_final[k].add(v)
    return dct_final

# The merge() function, which combines dictionaries into one common one.
# The function takes a list of dictionaries and returns a dictionary,
# each key of which contains a set (data type set)
# of unique values collected from all dictionaries of the passed list.