def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    result = any(map(lambda x: x in command, ignore))

    return result


print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))

# The ignore_command() function takes one string argument
# command as input - the command to be checked,
# and returns True if the command contains a substring
# from the ignore list and False otherwise.