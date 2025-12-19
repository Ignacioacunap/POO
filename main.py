from interfaces_usuario import ejecutar_app

if __name__ == "__main__":
    try:
        ejecutar_app()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")