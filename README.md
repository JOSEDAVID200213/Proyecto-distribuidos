# CRUD RESTful API con Flask y MongoDB Atlas

Este proyecto implementa una API RESTful utilizando Flask para crear, leer, actualizar y eliminar (CRUD) productos almacenados en una base de datos MongoDB Atlas.

## Configuración


1. **Instalación de Librerias en python**: Asegúrate de tener Python y pip instalados en tu sistema. Luego, puedes instalar las dependencias del proyecto ejecutando el siguiente comando en tu terminal:

## Instalación de Dependencias


1. **Flask**:

![Ejemplo de imagen](https://miro.medium.com/v2/resize:fit:640/1*XzIRJGujfqAiOV2EIQgR_Q.png)

Flask es un framework web ligero y flexible para Python. Se utiliza para crear aplicaciones web, desde simples páginas estáticas hasta complejas API RESTful. Flask proporciona herramientas y bibliotecas para ayudar en la creación rápida de aplicaciones web, permitiendo la definición de rutas, manejo de solicitudes y respuestas, y la integración con otras herramientas y bibliotecas.

    Para instalar Flask, ejecuta el siguiente comando en tu terminal:

    ```
    pip install Flask
    ```

2. **pymongo**:

![Ejemplo de imagen](https://techcrunch.com/wp-content/uploads/2016/06/2016-06-27_1940.png)


pymongo es el controlador oficial de Python para MongoDB. Permite a los desarrolladores interactuar con bases de datos MongoDB desde aplicaciones Python. Con pymongo, puedes realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar), consultas avanzadas, agregar índices y más, todo desde Python. Facilita la integración de MongoDB en aplicaciones Python, lo que permite el almacenamiento y recuperación eficientes de datos en bases de datos MongoDB.

    Para instalar pymongo, ejecuta el siguiente comando en tu terminal:

    ```
    pip install pymongo
    ```


2. **Configuración de MongoDB Atlas**: Crea una cuenta en MongoDB Atlas si aún no la tienes. Luego, crea un clúster y obtén la URL de conexión. Reemplaza la variable `uri` en el archivo `CRUD.py` con tu propia URL de conexión en la linea de codigo:
```
uri = "mongodb+srv://jmunoz6:Rpg200213@cluster0.w3e20jx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
```

3. **Ejecución del servidor**: Ejecuta el siguiente comando en tu terminal para iniciar el servidor Flask:

    ```
    python app.py
    
    ```



## ¿Que es Rest full API?
![Ejemplo de imagen](https://www.astera.com/wp-content/uploads/2020/01/rest.png)

# API RESTful para Gestión de Productos

Este proyecto implementa una API RESTful utilizando Flask y MongoDB Atlas para la gestión de productos. Una API RESTful es una arquitectura de servicios web que sigue los principios de REST (Representational State Transfer). Permite a los clientes comunicarse con el servidor utilizando solicitudes HTTP (GET, POST, PUT, DELETE) para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en recursos.

# Descripción de RESTful API

Una API RESTful utiliza los siguientes principios:

- **Protocolo HTTP**: Utiliza el protocolo HTTP para la comunicación entre cliente y servidor.
- **URI (Identificador de Recurso Uniforme)**: Cada recurso tiene un URI único que lo identifica.
- **Operaciones CRUD**: Utiliza los métodos HTTP estándar (GET, POST, PUT, DELETE) para realizar operaciones CRUD en los recursos.
- **Representaciones de recursos**: Los recursos pueden tener diferentes representaciones, como JSON o XML.
- **Sin estado (Stateless)**: Cada solicitud del cliente al servidor debe contener toda la información necesaria para comprender la solicitud, sin necesidad de mantener el estado del cliente en el servidor.

# Implementación en este Proyecto

En este proyecto, la API RESTful se implementa utilizando Python con Flask y MongoDB Atlas:

- **Flask**: Flask es un framework web ligero para Python que se utiliza para crear aplicaciones web y API RESTful.
- **MongoDB Atlas**: MongoDB Atlas es un servicio de base de datos en la nube que se utiliza como base de datos para almacenar los productos.

La implementación de la API RESTful incluye las siguientes características:

- **Rutas para Operaciones CRUD**: Se definen rutas para las operaciones CRUD en los productos, incluyendo obtener todos los productos, obtener un producto por su ID, crear un nuevo producto, actualizar un producto existente y eliminar un producto.
- **Interacción con MongoDB Atlas**: Se utiliza pymongo, el controlador oficial de Python para MongoDB, para interactuar con la base de datos MongoDB Atlas y realizar operaciones CRUD en los productos.
- **Formato JSON**: Se utiliza JSON (JavaScript Object Notation) como formato de intercambio de datos para representar los recursos.

# Uso de la API

Para utilizar la API RESTful, se pueden realizar solicitudes HTTP utilizando herramientas como Postman o cURL. Consulta el apartado de "Uso" en el README.md para obtener ejemplos de cómo realizar diferentes operaciones CRUD utilizando la API.




## Uso de la API RESTful con Postman

Este documento explica cómo utilizar Postman para realizar solicitudes GET, POST, PUT y DELETE a la API RESTful implementada en este proyecto.

## Configuración inicial

Antes de comenzar, asegúrate de tener instalado Postman en tu sistema. Puedes descargarlo desde [este enlace](https://www.postman.com/downloads/).

## Solicitudes HTTP

### GET - Obtener todos los productos

1. Abre Postman.

2. En la barra de direcciones, ingresa la URL de la solicitud GET para obtener todos los productos:

```
GET http://localhost:5000/productos
```


3. Haz clic en el botón "Enviar" para enviar la solicitud.

- Deberías recibir una respuesta JSON que contiene todos los productos almacenados en la base de datos.

### GET - Obtener un producto por su ID

1. En Postman, ingresa la URL de la solicitud GET para obtener un producto por su ID:

```
GET http://localhost:5000/productos/{producto_id}
```

Reemplaza `{producto_id}` con el ID del producto que deseas obtener.

2. Haz clic en el botón "Enviar" para enviar la solicitud.

- Deberías recibir una respuesta JSON que contiene los detalles del producto con el ID especificado.

### POST - Crear un nuevo producto

1. En Postman, selecciona el método POST.

2. Ingresa la URL de la solicitud POST para crear un nuevo producto:

```
POST http://localhost:5000/productos
```


3. En la pestaña "Cuerpo", selecciona "raw" y luego el formato JSON.

4. En el cuerpo de la solicitud, proporciona los detalles del nuevo producto en formato JSON:

```
json
{
  "producto_id": 123,
  "nombre": "Nuevo Producto",
  "precio": 19.99
}
```

5. Haz clic en el botón "Enviar" para enviar la solicitud.
Deberías recibir una respuesta JSON que contiene los detalles del nuevo producto creado. 

### DELETE - Eliminar un producto
1. En Postman, selecciona el método DELETE.

2. Ingresa la URL de la solicitud DELETE para eliminar un producto existente:

```
DELETE http://localhost:5000/productos/{producto_id}

```
3. Reemplaza {producto_id} con el ID del producto que deseas eliminar.

4. Haz clic en el botón "Enviar" para enviar la solicitud ; Deberías recibir una respuesta JSON que confirma que el producto ha sido eliminado correctamente.