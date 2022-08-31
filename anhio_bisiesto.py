numero = int(input("Ingrese su año de nacimiento o el año actual: "));

if ((numero % 4) == 0 and (numero % 100) != 0 or (numero % 100) == 0 and (numero % 400) == 0):
    print("El año es bisiesto");
else:
    print("El año no es bisiesto");
