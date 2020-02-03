from xmlrpc.server import (
	SimpleXMLRPCServer,
	list_public_methods
)

from caninehotel_backend.utils import register_rpc_operations

from caninehotel_backend.handler import RequestHandler

from caninehotel_backend.config import (
	HOST,
	PORT,
) 

from caninehotel_backend.database import connect_to_mongodb

def main():
	
	with SimpleXMLRPCServer((HOST, PORT), requestHandler = RequestHandler) as server:

		server.register_introspection_functions()

		server = register_rpc_operations(server)

		connect_to_mongodb()

		try:
			print("INICIANDO SERVIDOR...")
			print("SERVIDOR CORRIENDO EN : {}:{}".format(HOST, PORT))

			server.serve_forever()


		except KeyboardInterrupt:
			print("\nInterrupcion de teclado detectada.")
			sys.exit(0)

if __name__ == '__main__':
	main()