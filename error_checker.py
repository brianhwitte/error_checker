'''To print out a list of all variables operating at a particular point in your code, insert all the functions below at the top of your code and type 'make_table(dir())' at the point where you want to see a table.

'''

def working_var(all_var, unwanted_var):
    ''' working_var takes a parameter 'all_var' which is a list of all variables operating in the environment where the print_table function is called.  The parameter 'unwanted_var' is a list of variable names to be removed from the list of all variables.  This is currently set to remove all 'magic' variables with __ in the name"
    '''
    for x in unwanted_var:
        if x in all_var:
            all_var.remove(x)

    return all_var

def make_new_entry(eval_var):
    '''This function returns a dictionary of the type and value for each variable.
    '''
    return {
            'type': type(eval_var),
            'value': eval_var
        }

def make_table(clean_list):
    '''This function returns a dictionary of each variable in the environment at which the make_table function is called, along with the type and value of each variable.
    '''
    table = {}

    for x in (clean_list):
         table[x] = make_new_entry(eval(x))

    return table

def print_table(vars):
    '''This function returns a tab separated table of the names, types and values of each variable operating in the environment where it is called.  Note that these variables include the functions above.
    '''
    remove = ['__builtins__', '__doc__', '__name__', '__package__', '__file__',]
    clean_list = working_var(vars, remove)
    col_values = make_table(clean_list)

    col_titles = ["name space", "type", "value"]
    print "\t".join(col_titles)
    for i in col_values:
        print i + '\t' + str(col_values[i]["type"]) + '\t' + str(col_values[i]['value'])
