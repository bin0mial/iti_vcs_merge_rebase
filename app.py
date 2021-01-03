class Person:
	__name = "Default"
	__age = None
	__title = None	
	
	def __init__(self):
		self.__title = "ABC"
	def set_name(self, name: str):
		self.__name = f"Emp: {name}"

	def set_age(self, age: int):
		self.__age = age
