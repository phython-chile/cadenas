a = "240638886"

def rut_mod(mystring):
    position = len(mystring)-1
    longi = len(mystring)
    mystring   =  mystring[:position] + '-' + mystring[position:]
    return mystring

b = rut_mod(a)
print b
