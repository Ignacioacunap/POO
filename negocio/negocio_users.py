from prettytable import PrettyTable
from modelos import User, Address, Geo, Company
from datos import guardar_cambios, traer_todos, buscar_uno
from auxiliares import leer_input, es_email_valido
from .api_handler import peticion_api

def sincronizar_usuarios(url):
    resp = peticion_api('GET', url)
    if not resp or resp.status_code != 200:
        print("⚠️ No se pudo descargar usuarios.")
        return

    datos = resp.json()
    count = 0
    print("⏳ Procesando usuarios...")
    
    for u in datos:
        # Lógica compacta: Crear objetos anidados
        geo = Geo(lat=u['address']['geo']['lat'], lng=u['address']['geo']['lng'])
        guardar_cambios(geo)
        
        addr = Address(
            street=u['address']['street'], suite=u['address']['suite'],
            city=u['address']['city'], zipcode=u['address']['zipcode'],
            geoId=geo.id
        )
        guardar_cambios(addr)
        
        comp = Company(
            name=u['company']['name'], catchPhrase=u['company']['catchPhrase'],
            bs=u['company']['bs']
        )
        guardar_cambios(comp)
        
        # Verificar duplicados antes de insertar
        if not buscar_uno(User, email=u['email']):
            nuevo_user = User(
                name=u['name'], username=u['username'], email=u['email'],
                phone=u['phone'], website=u['website'],
                addressId=addr.id, companyId=comp.id
            )
            guardar_cambios(nuevo_user)
            count += 1
            
    print(f"✅ Sincronización finalizada. {count} usuarios nuevos.")

def listar_usuarios_local():
    lista = traer_todos(User)
    t = PrettyTable(['ID', 'Nombre', 'Email', 'Web'])
    for u in lista:
        t.add_row([u.id, u.name, u.email, u.website])
    print(t if lista else "📭 Base de datos vacía.")

# --- Funciones CRUD API ---
def api_crear_usuario(url):
    print("\n[NUEVO USUARIO REMOTO]")
    payload = {
        "name": leer_input("Nombre: "),
        "username": leer_input("Username: "),
        "email": leer_input("Email: ", es_email_valido, "Email inválido"),
        "phone": input("Teléfono: "),
        "website": input("Web: ")
    }
    
    resp = peticion_api('POST', url, data=payload)
    if resp:
        print(f"Status: {resp.status_code}")
        if resp.status_code == 201:
            print(f"✅ Creado: {resp.json()}")

def api_modificar_usuario(url):
    uid = leer_input("ID a modificar: ")
    nuevo_nombre = leer_input("Nuevo nombre: ")
    
    resp = peticion_api('PUT', f"{url}/{uid}", data={"name": nuevo_nombre})
    if resp:
        print(f"Status: {resp.status_code}")
        if resp.status_code == 200:
            print("✅ Actualizado correctamente.")

def api_eliminar_usuario(url):
    uid = leer_input("ID a eliminar: ")
    resp = peticion_api('DELETE', f"{url}/{uid}")
    if resp:
        print(f"Status: {resp.status_code}")
        if resp.status_code == 200:
            print("✅ Eliminado correctamente.")