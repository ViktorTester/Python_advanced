def build_query_string(params):
    res = [f'{k}={v}' for k, v in params.items()]
    return '&'.join(sorted(res))

# Query string - part of the URL containing the keys and their values.
# It starts after the question mark and goes to the end of the address.

# The build_query_string() function takes a dictionary with parameters as
# input and returns a query string formed from these parameters.
