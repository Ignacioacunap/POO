import re

def es_email_valido(email):
    # Regex simplificado pero efectivo
    return bool(re.search(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))

def leer_input(mensaje, validacion=None, error_msg="Entrada incorrecta"):
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("⚠️ El campo no puede estar vacío.")
            continue
        
        if validacion and not validacion(valor):
            print(f"⚠️ {error_msg}")
            continue
            
        return valor