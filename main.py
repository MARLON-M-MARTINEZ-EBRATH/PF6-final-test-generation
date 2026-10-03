'''# Instrucciones
¡Ahora tienes la oportunidad de crear un menú de platos típicos de nuestro país! Tu menú puede funcionar como tú quieras.

Primero, vamos a separar la lógica *interactiva* en la función `main()`, de la siguiente manera:

```
def main():
print("¡Hola, estudiantes!")

if __name__=="__main__":
main()
```

Este es código de Python reutilizable que solo se ejecutará cuando alguien invoque el programa. Todo tu código debe estar dentro de una función, ya sea esta función `main()` (donde puedes incluir elementos como instrucciones de entrada de datos) u otra función.

La calificación automática se basará en la funcionalidad de la siguiente función (que debe estar incluida en tu programa):

* `dish_fetch(num)`: Esta función debe existir en tu programa. Debe recibir un número como entrada y generar un diccionario con la información del plato correspondiente a ese número.

**Recuerda**: Este proyecto se calificará automáticamente, ¡y las computadoras son muy literales!
**Nota:** ¡Utiliza las pruebas! No hay nada malo en repetirlas hasta aprobar. ¡No es hacer trampa!'''



import requests

def dish_fetch(num):
    """
    Esta función busca un plato por su número (ID) en la API de Colombia
    y devuelve un diccionario con su información.
    """
    url = f"https://api-colombia.com{num}"
    try:
        response = requests.get(url)
        # Si la API responde correctamente (Código 200)
        if response.status_code == 200:
            data = response.json()
            
            # Construimos y retornamos el diccionario con la información del plato
            platillo = {
                "id": data.get("id"),
                "name": data.get("name"),
                "description": data.get("description"),
                "ingredients": data.get("ingredients")
            }
            return platillo
        else:
            # Si el número no existe o hay error, devolvemos un diccionario vacío o mensaje
            return {"error": f"No se encontró el plato con el número {num}"}
            
    except Exception:
        return {"error": "Error de conexión con la API"}

def main():
    print("--- ¡Bienvenido al Menú de Platos Típicos de Colombia! ---\n")
    print("Ingresa un número para buscar un plato típico (Ejemplos: 1, 2, 5, 10)")
    
    try:
        opcion = input("Introduce el número del plato: ")
        # Convertimos la entrada a número entero
        num_plato = int(opcion)
        
        # Llamamos a la función obligatoria
        resultado = dish_fetch(num_plato)
        
        # Mostramos el diccionario resultante de forma ordenada
        if "error" not in resultado:
            print("\n____________________________________________")
            print(f"🍽️  PLATO: {resultado['name']}")
            print("___________________________________________")
            print(f"Descripción: {resultado['description']}\n")
            print(f"Ingredientes: {resultado['ingredients']}")
            print("__________________________________________")
        else:
            print(f"\n{resultado['error']}")
            
    except ValueError:
        print("\nPor favor, introduce un número válido.")

if __name__ == "__main__":
    main()
