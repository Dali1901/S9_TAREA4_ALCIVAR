class Menu:
    def __init__(self):
        pass

    def menu_principal(self,opciones_A,titulo_A):
        print("-----",titulo_A,"-----")
        for opcion_A in opciones_A:
            print(opcion_A)
        print("----------")
        opc_A = input("Escoja una opción[1 - {}]: ".format(len(opciones_A)))
        return opc_A