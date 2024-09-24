class Provedores:
        id=0
        nombre=""
        apellido=""
        telefono=0
        edad=0
        ine=""
        permiso=""
    # zona de funciones
        def mostrar_datos(self):
            print("estos son los datos de mi provedor")
            print(f"id :{Proovedor.id}")
            print(f"ine:  {Proovedor.ine}")
            print(f"telefono :{Proovedor.telefono}")
            print(f"Edad :{Proovedor.edad}")
            print(f"Nombre :{Proovedor.nombre}")
            print(f"Permiso :{Proovedor.permiso}")
            print(f"Apellido :{Proovedor.apellido}")
        def lista_Drogin(self):
            list_mercaDrogin=("fenta","mota","cristal","cocodrile","verde")
            for x in list_mercaDrogin:
                print(x)
        def tupla_Drogin(self):
            tupla_colores_cristal=("Rosa", "Negro", "Blanco","Azul cielo","amarillo")
            for x in tupla_colores_cristal:
                print(x)
        def diccionario_Drogin(self):
            diccionario = {"fenta": "$430","mota": "$376","cristal": "$600",
"cocodrile": "$830", "verde": "$190",}
            for x, y in diccionario.items():
                print(x,":",y)
# zona de creacion de objetos
Proovedor=Provedores()
#zona de usando objeto
Proovedor.id=70
Proovedor.nombre="Carlos"
Proovedor.edad=23
Proovedor.telefono=6565901005
Proovedor.ine="67d36f858k3"
Proovedor.permiso="si"
Proovedor.apellido="Melgar"
Proovedor.mostrar_datos()
datos=Provedores()
print("\nlistado de mercancia vendida\n")
datos.lista_Drogin()
print("\ncolores del cristal\n")
datos.tupla_Drogin()
print("\nprecios de la merca\n")
datos.diccionario_Drogin()