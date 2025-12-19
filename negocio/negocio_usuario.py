import bcrypt
from modelos import Usuario
from datos import guardar_cambios, buscar_uno

def registrar_admin(nombre, login, email, password):
    # Generamos la seguridad
    salt = bcrypt.gensalt()
    pw_hash = bcrypt.hashpw(password.encode(), salt)

    nuevo = Usuario(
        nombre=nombre, usuario=login, email=email,
        contrasena_hash=pw_hash.decode(),
        contrasena_salt=salt.decode()
    )
    
    if guardar_cambios(nuevo):
        print(f"✅ Admin '{login}' registrado.")
        return True
    return False

def autenticar(login, password):
    user_db = buscar_uno(Usuario, usuario=login)
    if not user_db:
        return False
    
    # Verificación
    if bcrypt.checkpw(password.encode(), user_db.contrasena_hash.encode()):
        print(f"👋 Hola de nuevo, {user_db.nombre}")
        return True
    return False