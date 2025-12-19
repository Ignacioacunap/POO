from decouple import config

# Cargo las variables de entorno con nombres genéricos
CREDS = {
    'user': config('DB_USER'),
    'pass': config('DB_PASSWORD', default=''),
    'host': config('DB_HOST'),
    'port': config('DB_PORT'),
    'db': config('DB_NAME')
}