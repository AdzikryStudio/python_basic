# tipedata 

# integer
data_integer = 1
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))
# float
data_float = 1.9
print("data : ", data_float)
print("- bertipe : ", type(data_float))
# string
data_string = "halo"
print("data : ", data_string)
print("- bertipe : ", type(data_string))
# biner / boolean
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

# tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data dari C
from ctypes import c_double
data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))

