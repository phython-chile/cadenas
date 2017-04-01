

def comprobar_rut(int_rut):
    rut = int_rut[:-1]
    dig = int_rut[-1]

    # Multiplicamos cada posicion
    n1 = rut[0]
    m1 = int(n1)*3

    n2 = rut[1]
    m2 = int(n2)*2

    n3 = rut[2]
    m3 = int(n3)*7

    n4 = rut[3]
    m4 = int(n4)*6

    n5 = rut[4]
    m5 = int(n5)*5

    n6 = rut[5]
    m6 = int(n6)*4

    n7 = rut[6]
    m7 = int(n7)*3

    n8 = rut[7]
    m8 = int(n8)*2

    suma = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8
    resto = suma / 11
    resto = 11 - ( suma - resto * 11 )

    if resto == 10:
        resto = 'K'

    ok = False
    if dig == str(resto):
        ok = True

    return ok


print comprobar_rut('240638886')
