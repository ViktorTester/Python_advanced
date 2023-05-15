def flatten_dict(d: dict) -> dict:
    s, c = {}, 0
    for k, v in d.items():
        if type(v) == int: s[k] = v
        else:
            for k1, v1 in v.items():
                s[k+'_'+k1] = v1
                if type(v1) == dict: c+=1
    if c != 0:
        return flatten_dict(s)
    else:
        return s

# The function takes a dictionary of unlimited nesting as input, and returns a linear
# dictionary, where the keys are formed by concatenation of
# nested keys connected by the '_' sign