from abc import ABC, abstractmethod

class Platter:
	def __init__(self, baverage = None):
		self.baverage = baverage

	@abstractmethod
	def platter_price(self):
		pass


class Beverage:
	@abstractmethod
	def baverage_price(self):
		pass

class Coke(Beverage):

	def __init__(self):
		self.name = 'CocaCola'
		self.unit_price = 15

	def baverage_price(self):
		return self.unit_price



class HandiBiriyani(Platter):
	_name = 'Handi Biriyani'
	_unit_price = 150

	def platter_price(self):
		if self.baverage:
			return self._unit_price + self.baverage.baverage_price()
		return self._unit_price



handi_biriyani = HandiBiriyani()
print(f"Handi Biriyani without coke {handi_biriyani.platter_price()}")

coke = Coke()
handi_with_code = HandiBiriyani(coke)
print(f"Handi Biriyani with coke {handi_with_code.platter_price()}")

# Now any new baverage item can be easily combined with any new Platter easily