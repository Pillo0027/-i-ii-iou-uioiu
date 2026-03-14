def pri():
    print("Bienvenido, para registrarse ingrese usuario y cree una contraseña.")
    us = input("Ingrese el usuario: ")
    con = input("Ingrese su contraseña: ")
    con2 = input("Repita la contraseña: ")
    
    if con == con2:
        print("Las contraseñas han sido validadas, puede continuar")
        return us, con
    else:
        print("Contraseñas inválidas, el programa se reiniciará")
        return pri()

def pinpon(us, con):
    while True:
        print("Bienvenido, para entrar ingrese su contraseña y usuario")
        us_ans = input("Ingrese su usuario: ")
        con_ans = input("Ingrese su contraseña: ")

        if us == us_ans and con == con_ans:
            print("Has ingresado correctamente")
            break
        elif us == us_ans and con != con_ans:
            print("Contraseña incorrecta, se redirige al inicio del programa")
            break
        elif us != us_ans and con == con_ans:
            print("Usuario incorrecto, se redirige al inicio del programa")
            break

        elif us != us_ans and con != con_ans:
            print("Usuario y contraseña incorrectos, se redirige al inicio del programa")
            break
        
        err = input("¿Desea continuar con el código? (poner 'continuar' para seguir, 'exit' para salir): ")
        if err == "exit":
            break

usr, contraseña = pri()
pinpon(usr, contraseña)
print("Programa finalizado")