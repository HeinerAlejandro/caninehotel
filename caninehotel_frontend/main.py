import xmlrpc.client

from caninehotel_frontend.config import(
	URL_SERVER
)

def main():

	with xmlrpc.client.ServerProxy(URL_SERVER) as client_stub:

		#solo operaciones de dog:

		print(client_stub.dog.add("algo"))
		print(client_stub.dog.find("algo"))
		print(client_stub.dog.modify("algo"))
		print(client_stub.dog.delete("algo"))

if __name__ == '__main__':
	main()