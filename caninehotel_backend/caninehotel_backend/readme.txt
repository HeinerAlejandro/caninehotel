Este es el paquete principal, te explicare resumidamente la estructura:

-modules : Son aplicaciones pequeñas que representan modulos rpc, por ejemplo:
	> dogs
	> room
	> users

	Por los momentos, cada modulo posee una estructura de modulos python como se -muestra a continuacion:
	rpc_module
		> models.py
		> operations.py
		> validators(opcional, estos ayudaran a validar los esquemas mongodb)

-tests : En esta carpeta agregaras tus pruebas, relacionadas a los modulos rpc.

config.py : Tiene constantes de configuracion del proyecto como entorno(desarrollo/produccion), que nos servira para desplegar a futuro(si es que es necesario 	    desplegar, que ya lo creo). Tambien, define una tupla, de rutas hacia los modulos que agregas al proyecto, ve las rutas, debes ingresarlas con ese formato.

database : Incluye logica de conexion con MongoDb, sin embargo, las constantes de configuracion se encuentran en config.py.

handler : Es un manejador de solicitudes, el cual puede mapear los metodos rpc que creamos, por los momentos los mapea el objeto servidor directamente, tal vez a futuro se modifique para hacer el codigo mas limpio.

utils : son utilidades a nivel general, por los momentos contiene 2 funciones:
	-register_rpc_operations : es el core de la automatizacion al registrar modulos en el config.py, toma las rutas de modules en config.py y obtiene dinamicamente          		  	   estos modulos, posteriormente obtiene las operaciones rpc de operations.py y las registrar como operaciones rpc con el objeto 			           	   server.

decorators : Aqui agregaras los decoradores a nivel general que creas convenientes, por los momentos hay uno:
	    -namespace_decorator: a cada operacion rpc(funcion), le agrega un atributo(las funciones se comportan como objetos), este atributo se llama namespace, y 	    			  nos permite modularizar mejor las operaciones rpc. ejemplo
				-dogs
					> operations.py
						-function add(...)
						-function modify(...)
						-function delete(...)
						-function find(...)

				-room
					> operations.py
						-function add(...)
						-function modify(...)
						-function delete(...)
						-function find(...)

	Si se registran estas operaciones rpc, se sobreescribiran porque tienen el mismo nombre. Este decorador, permite agregar en el momento de la definicion de una funcion un namespace para registrar la pertenencia de cada operacion a un espacion de nombre especifico. Ejemplo : 
	-dog.add(...)			room.add(...)
	-dog.find(...)			room.find(...)
	-dog.modify(...)		room.modify(...)

	Los ultimos accesos que has visto, son la forma en las que se registran los servicios en el server, y la cual es usada por el stub del cliente para hacer sus metodos.

	NOTA: por los momentos, esto es todo, falta acomodar lo de mongo, instala sciter y a echarle pichon			



