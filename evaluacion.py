saldo = 0
saldoDep = 0
saldoGi = 0
saldoTras = 0
saldoCom = 0
saldoPag = 0

montoDep = 0
montoGi = 0
montoTras = 0
montoCom = 0
montoPag = 0

def depositar(saldo,monto):
    if monto <= 100000:
        saldo += monto
        return saldo
    else:
        print("El monto excede el limite permitido de $100000")
        return saldo

def girar(saldo,monto):
    if monto <= 200000:
        saldo -= monto
        return saldo
    else:
        print("El monto excede el limite permitido de $200000")
        return saldo

def transferir(saldo,monto,user):
    if monto <= 250000:
        if monto <= saldo:
            saldo -= monto
            print("Transferencia a {} de ${} realizada con exito".format(user, monto))
            print("")
        else:
            print("Saldo insuficiente")
    else:
        print("El monto excede el limite permitido de $250000")
    return saldo

def comprar(saldo,monto):
    if monto <= saldo:
        saldo -= monto
    else:
        print("Saldo insuficiente")
    return saldo

def pagar(saldo,monto):
    if monto <= saldo:
        saldo -= monto
    else:
        print("Saldo insuficiente")
    return saldo

def menuPagar():
    print("===============================")
    print("Ingrese la opcion que desea pagar")
    print("1. Agua")
    print("2. Telefonia")
    print("3. Electricidad")
    print("4. Gas")
    print("5. Volver")
    print("")
    opcion = int(input("→ "))
    if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
        return opcion
    else:
        print("Opcion incorrecta")

def menuTrans():
    print("===============================")
    print("")
    print("Que tipo de transaccion desea realizar")
    print("")
    print("Su saldo actual es de: $",saldo)
    print("")
    print("1. Depositar")
    print("2. Girar")
    print("3. Transferir")
    print("4. Comprar")
    print("5. Pagar")
    print("6. Volver")
    print("")
    num = input("→ ")
    return num

def mostrarTrans():
    print("===============================")
    print("Depositos | Monto: {} | Saldo: ${} ".format(montoDep, saldoDep))
    print("Giros | Monto: {} | Saldo: ${} ".format(montoGi, saldoGi))
    print("Transferencias | Monto: {} | Saldo: ${} ".format(montoTras, saldoTras))
    print("Compras | Monto: {} | Saldo: ${} ".format(montoCom, saldoCom))
    print("Pago cuenta {} | Monto: {} | Saldo: ${} ".format(cuenta, montoPag, saldoPag))
    print("===============================")

def login():
    print("===============================")
    print("Ingrese un usuario para su cuenta")
    nombre = input("→ ")
    print("Ingrese una contraseña para su cuenta")
    contraseña = input("→ ")
    # validar usuario
    contador = 4
    while contador >= 1:
        print("===============================")
        print("Ingrese su usuario")
        validarUsuario = input("→ ")
        print("Ingrese su contraseña")
        validarContraseña = input("→ ")
        if validarUsuario == nombre and validarContraseña == contraseña:
            contador = 0
            return True
        else:
            print("===============================")
            print("USUARIO/CONTRASEÑA INCORRECTA")
            if contador == 1:
                print("TU CUENTA AH SIDO BLOQUEADA")
                break
            else:
                contador -= 1
                print("Te quedan {} intentos".format(contador))

def menu():
    print("===============================")
    print("BIENVENIDO A PYTHON BANK")
    print("")
    print("Su saldo actual es de: $",saldo)
    print("")
    print("1. Menú transacciones")
    print("2. Mostrar Transacciones")
    print("3. Salir")
    print("")
    print("Que opcion desea escojer")
    opcion = int(input("→ "))
    if opcion == 1 or opcion == 2 or opcion == 3:
        return opcion
    else:
        print("Opcion incorrecta")

# PP
if login() == True:
    while True:
        menuP = menu()
        if menuP == 1:
            while True:
                menuTransacciones = menuTrans() # DEPOSITO
                if menuTransacciones == '1':
                    print("===============================")
                    print("Ingrese el monto que desea depositar")
                    monto = int(input("→ "))
                    saldo = depositar(saldo, monto)
                    montoDep = monto
                    saldoDep = saldo
                elif menuTransacciones == '2': # GIRO
                    print("===============================")
                    print("Ingrese el monto que desea girar")
                    monto = int(input("→ "))
                    saldo = girar(saldo, monto)
                    montoGi = monto
                    saldoGi = saldo
                elif menuTransacciones == '3': # TRANSFERENCIA
                    print("===============================")
                    print("Ingrese al usuario que desea transferir")
                    user = input("→ ")
                    print("Ingrese el monto que desea transferir")
                    monto = int(input("→ "))
                    saldo = transferir(saldo, monto, user)
                    montoTras = monto
                    saldoTras = saldo
                elif menuTransacciones == '4': # COMPRA
                    print("===============================")
                    print("Ingrese el monto que desea comprar")
                    monto = int(input("→ "))
                    print("")
                    saldo = comprar(saldo, monto)
                    montoCom = monto
                    saldoCom = saldo
                elif menuTransacciones == '5': # PAGAR
                    menuPag = menuPagar()
                    while True:
                        if menuPag == 1 or menuPag == 2 or menuPag == 3 or menuPag == 4:
                            if menuPag == 1:
                                cuenta = "Agua"
                            if menuPag == 2:
                                cuenta = "Telefonia"
                            if menuPag == 3:
                                cuenta = "Electricidad"
                            if menuPag == 4:
                                cuenta = "Gas"
                            print("===============================")
                            print("Ingrese el monto que desea pagar de su cuenta de", cuenta)
                            monto = int(input("→ "))
                            print("")
                            saldo = pagar(saldo, monto)
                            montoPag = monto
                            saldoPag = saldo
                            break
                        elif menuPag == 5:
                            break
                        else:
                            print("El numero ingresado es incorrecto")
                elif menuTransacciones == '6':
                    break
                else:
                    print("El numero ingresado es incorrecto")
        elif menuP == 2:
            mostrarTrans()
        elif menuP == 3:
            break
        else:
            print("El numero ingresado es incorrecto")

