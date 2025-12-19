from prettytable import PrettyTable
from modelos import Post, User
from datos import guardar_cambios, buscar_uno, traer_todos
from .api_handler import peticion_api

def sincronizar_posts(url):
    resp = peticion_api('GET', url)
    if resp and resp.status_code == 200:
        posts = resp.json()
        guardados = 0
        for p in posts:
            # Integridad Referencial: Solo guardamos si tenemos al usuario
            if buscar_uno(User, id=p['userId']):
                # Evitar duplicados por ID
                if not buscar_uno(Post, id=p['id']):
                    nuevo = Post(id=p['id'], title=p['title'], body=p['body'], userId=p['userId'])
                    guardar_cambios(nuevo)
                    guardados += 1
        print(f"✅ {guardados} publicaciones importadas.")

def listar_posts_local():
    data = traer_todos(Post)
    t = PrettyTable(['ID', 'User', 'Título'])
    t.align = "l"
    for p in data:
        t.add_row([p.id, p.userId, p.title[:40]])
    print(t)