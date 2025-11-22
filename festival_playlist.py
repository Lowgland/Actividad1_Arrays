def menu():
    print("\n MENU PLAYLIST")
    print("1. agregar canciones")
    print("2. Ver reportes")
    print("3. Buscar canciones")
    print("4. Playlist recomendada")
    print("5. salir")

def main():
    nombres=[]
    artistas=[]
    duraciones=[]
    popularidades=[]

    while True:
        menu()
        opcion=int(input("Escoge una opcion del 1 al 5: "))
        if opcion==1:
            cancion=int(input("ingresa la cantidad de canciones para agregar: "))
            for i in range(cancion):
                nombre=input(f"Ingresa el nombre de la cancion {i+1}: ").title()
                artista=input(f"ingresa el nombre del artista de la cancion {i+1}: ").title()
                duracion=float(input(f"ingresa la duracion de la cancion {i+1} en minutos: "))
                popularidad=int(input(f"ingresa la popularidad de la cancion {i+1} en un rango del 1 al 100: "))
                nombres.append(nombre)
                artistas.append(artista)
                duraciones.append(duracion)
                popularidades.append(popularidad)
                print(f"La cancion {nombre} del artista {artista} ha sido agregada a la playlist correctamente.")

        elif opcion==2:
            if nombres:
                total_canciones=len(nombres)
                duracion_total=sum(duraciones)
                promedio=sum(popularidades)/len(popularidades)
                mas_popular= nombres[popularidades.index(max(popularidades))]
                menos_popular= nombres[popularidades.index(min(popularidades))]
                print("\n Reporte de la playlist")
                print(f"Total de canciones: {total_canciones}")
                print(f"Duracion total de la playlist: {duracion_total:.2f} minutos")
                print(f"Cancion mas popular: {mas_popular} con una popularidad de: {max(popularidades)}/100")
                print(f"Cancion menos popular: {menos_popular} con una popularidad de: {min(popularidades)}/100")
                print(f"Promedio de popularidad: {promedio:.2f}")
            else:
                print("No hay canciones registradas")

        elif opcion==3:
            if nombres:
                def menu_busqueda():
                    print("\n MENU BUSQUEDA")
                    print("1. Buscar por artista")
                    print("2. Buscar por rango de popularidad")
                    print("3. Volver al menu principal")
                while True:
                    menu_busqueda()
                    opcion_busqueda=int(input("Escoge una opcion del 1 al 3: "))
                    if opcion_busqueda==1:
                        artista=input("ingresa el artista a buscar: ").title()
                        encontrado=False
                        for i in range(len(artistas)):
                            if artista==artistas[i]:
                                encontrado=True
                                print(f"Cancion: {nombres[i]} | Artista: {artistas[i]} | Duracion: {duraciones[i]} minutos | Popularidad: {popularidades[i]}/100")
                        if encontrado == False:
                            print("Artista no encontrado")
                    
                    elif opcion_busqueda==2:
                        minimia_popularidad=int(input("ingresa la popularidad minima (1-100): "))
                        maxima_popularidad=int(input("ingresa la popularidad maxima (1-100): "))
                        encontrado=False
                        for i in range(len(popularidades)):
                            if minimia_popularidad<=popularidades[i]<=maxima_popularidad:
                                encontrado=True
                                print(f"Cancion: {nombres[i]} | Artista: {artistas[i]} | Duracion: {duraciones[i]} minutos | Popularidad: {popularidades[i]}/100")
                        if encontrado == False:
                            print("No se encontraron canciones en ese rango de popularidad")
                    
                    elif opcion_busqueda==3:
                        break
                    else:
                        print("Opcion no valida, intenta de nuevo...")
                        
        elif opcion==4:
            if nombres:
                print("\n Playlist recomendada (canciones con popularidad mayor al promedio)")
                promedio=sum(popularidades)/len(popularidades)
                encontrado=False
                for i in range(len(popularidades)):
                    if popularidades[i]>promedio:
                        encontrado=True
                        print(f"Cancion: {nombres[i]} | Artista: {artistas[i]} | Duracion: {duraciones[i]} minutos | Popularidad: {popularidades[i]}/100")
                if not encontrado:
                    print("No se encontraron canciones con popularidad mayor al promedio")
            else:
                print("No hay canciones registradas")

        elif opcion==5:
            print ("Gracias por pasar tu tiempo :D") 
            print("Saliendo del programa... ")
            break
        else:
            print("opcion no valida, intenta de nuevo...")
main()