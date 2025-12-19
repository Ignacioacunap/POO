import pwinput
import sys
from negocio import *

# Constantes de configuración
URLS = {
    'users': 'https://jsonplaceholder.typicode.com/users',
    'posts': 'https://jsonplaceholder.typicode.com/posts',
    'comments': 'https://jsonplaceholder.typicode.com/comments'
}

def mostrar_menu_inicio():
    print("\n" + "█"*30)
    print("   SISTEMA DE GESTIÓN API")
    print("█"*30)
    print("1. Acceder (Login)")
    print("2. Registrar Admin")
    print("0. Salir")
    return input(">> Opción: ")

def mostrar_menu_admin():
    print("\n--- PANEL DE ADMINISTRACIÓN ---")
    print("1. Sincronizar Todo (Users -> Posts -> Comments)")
    print("2. Ver Usuarios (BD Local)")
    print("3. Ver Publicaciones (BD Local)")
    print("4. Ver Comentarios (BD Local)")
    print("5. Crear Usuario API (POST)")
    print("6. Editar Usuario API (PUT)")
    print("7. Borrar Usuario API (DELETE)")
    print("9. Cerrar Sesión")
    return input(">> Acción: ")

def ejecutar_app():
    sesion_activa = False

    while True:
        if not sesion_activa:
            opc = mostrar_menu_inicio()
            if opc == '1':
                u = input("Usuario: ")
                p = pwinput.pwinput("Clave: ", mask="*")
                if autenticar(u, p):
                    sesion_activa = True
            elif opc == '2':
                print("\n[REGISTRO]")
                n = input("Nombre: ")
                u = input("Usuario: ")
                e = input("Email: ")
                p = pwinput.pwinput("Clave: ", mask="*")
                registrar_admin(n, u, e, p)
            elif opc == '0':
                print("Hasta luego.")
                sys.exit()
            else:
                print("Opción no válida.")
        else:
            # Lógica del usuario logueado
            accion = mostrar_menu_admin()
            try:
                if accion == '1':
                    print("\n🚀 Iniciando carga masiva...")
                    sincronizar_usuarios(URLS['users'])
                    sincronizar_posts(URLS['posts'])
                    sincronizar_comentarios(URLS['comments'])
                elif accion == '2':
                    listar_usuarios_local()
                elif accion == '3':
                    listar_posts_local()
                elif accion == '4':
                    listar_comentarios_local()
                elif accion == '5':
                    api_crear_usuario(URLS['users'])
                elif accion == '6':
                    api_modificar_usuario(URLS['users'])
                elif accion == '7':
                    api_eliminar_usuario(URLS['users'])
                elif accion == '9':
                    sesion_activa = False
                    print("Sesión cerrada.")
                else:
                    print("Comando desconocido.")
            except Exception as e:
                print(f"❌ Ocurrió un error inesperado: {e}")