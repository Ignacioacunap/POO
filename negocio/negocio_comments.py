from prettytable import PrettyTable
from modelos import Comment, Post
from datos import guardar_cambios, buscar_uno, traer_todos
from .api_handler import peticion_api

def sincronizar_comentarios(url):
    resp = peticion_api('GET', url)
    if resp and resp.status_code == 200:
        comms = resp.json()
        guardados = 0
        for c in comms:
            if buscar_uno(Post, id=c['postId']):
                if not buscar_uno(Comment, id=c['id']):
                    nuevo = Comment(id=c['id'], name=c['name'], email=c['email'], body=c['body'], postId=c['postId'])
                    guardar_cambios(nuevo)
                    guardados += 1
        print(f"✅ {guardados} comentarios importados.")

def listar_comentarios_local():
    data = traer_todos(Comment)
    t = PrettyTable(['ID', 'Post', 'Email', 'Contenido'])
    t.align = "l"
    for c in data[-15:]: # Solo los ultimos 15
        t.add_row([c.id, c.postId, c.email, c.body[:30]])
    print(t)
    print("(Mostrando últimos 15 registros)")