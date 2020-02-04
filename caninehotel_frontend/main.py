import xmlrpc.client
from sciter.window import Window

from caninehotel_frontend.config import(
	URL_SERVER
)

client_stub = xmlrpc.client.ServerProxy(URL_SERVER)

def main():

	frame = Window(ismain = True, uni_theme = True)

	frame.load_file('./statics/html/index.html')

	frame.expand ()
	frame.run_app ()
	"""print(client_stub.dog.add("algo"))
	print(client_stub.dog.find("algo"))
	print(client_stub.dog.modify("algo"))
	print(client_stub.dog.delete("algo"))"""

if __name__ == '__main__':
	main()