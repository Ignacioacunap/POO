import requests

def peticion_api(metodo, url, data=None, timeout=15):
    """Wrapper para manejar errores HTTP de forma centralizada."""
    try:
        if metodo == 'GET':
            r = requests.get(url, timeout=timeout)
        elif metodo == 'POST':
            r = requests.post(url, json=data, timeout=timeout)
        elif metodo == 'PUT':
            r = requests.put(url, json=data, timeout=timeout)
        elif metodo == 'DELETE':
            r = requests.delete(url, timeout=timeout)
        
        return r
    except requests.RequestException as e:
        print(f"❌ Error de comunicación con API: {e}")
        return None