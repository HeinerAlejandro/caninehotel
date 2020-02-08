import unittest

from caninehotel_backend.database import connect_to_mongodb
from caninehotel_backend.modules import room

connect_to_mongodb()

class TestRoomOperations(unittest.TestCase):

	def test_add(self):

		data = dict(
			number = 1,
			type_room = 'CLASICA',
			cost = 17.2
		)

		self.assertTrue(bool(room.operations.add(data)))

if __name__ == 'main':
	unittest.main()