from sympy.utilities.codegen import codegen
from sympy import symbols

def save_as_c_func(function,filename,var_name):
    """
    Saves a poly1d function as compilable C code
    """
    variable = symbols(var_name)
    [(c_name, c_code), (h_name, c_header)] = \
    codegen((var_name, function(variable)), "C99", filename,
             header=False, empty=False)

    with open(h_name, "w") as h_file:
        h_file.write(c_header)
    with open(c_name, "w") as c_file:
        c_file.write(c_code)
