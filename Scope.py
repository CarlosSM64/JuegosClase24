# 3.1 Global and local Variables in Python
# 3.2 Global and local functions

valor = 80

def presentacionnumerica():
    print(valor)

def presentacionadicional():
    print("Entonces el valor es ", valor)

def presentarnuevovalor():
    print(90)
    
    def muestraholatodos():
        print("Esta es una ejecución desde la función interna")
        
        muestraholatodos()
        
presentacionnumerica()
presentarnuevovalor() # muestraholatodos está dentro, no existe para el scope
