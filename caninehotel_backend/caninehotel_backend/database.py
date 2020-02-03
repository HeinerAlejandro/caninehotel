from mongoengine import connect

from .config import MONGODB_NAME

def connect_to_mongodb():
	connect(MONGODB_NAME)

