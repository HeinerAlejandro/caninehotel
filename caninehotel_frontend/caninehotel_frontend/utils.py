from datetime import datetime

def obj_to_str(date_obj):
	
	value = date_obj.value

	date = datetime.strptime(value, "%Y%m%dT%H:%M:%S")

	return date