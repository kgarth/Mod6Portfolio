from Product import Product

class ShoppingCart:
	customer_name = ''
	current_date = ''
	cart_items = []

	def __init__(self, name = 'none', date = 'January 1, 2020'):
		self.customer_name = name
		self.current_date = date

	def set_name(self, name = ''):
		self.customer_name = name

	def set_date(self, date = ''):
		self.current_date = date

	def get_name(self):
		return self.customer_name

	def get_date(self):
		return self.current_date

	def get_item(self, pos = 0):
		return self.cart_items[pos]

	def get_cart_items(self):
		return self.cart_items

	def add_item(self, ItemToPurchase):
		self.cart_items.append(ItemToPurchase)

	def remove_item(self, ItemToRemove):
		del self.cart_items[ItemToRemove]

	def modify_item(self, ItemToModify):
		for pos, item in enumerate(self.cart_items):
			if item.get_name == ItemToModify.get_name():
				if item.get_quanity() != ItemToModify.get_quantity():
					self.item_list[pos].set_quantity(ItemToModify.get_quantity())
				if item.get_cost() != ItemToModify.get_cost():
					self.item_list[pos].set_cost(ItemToModify.get_cost())
				if item.get_description() != ItemToModify.get_description():
					self.item_list[pos].set_description(ItemToModify.get_description())
				break
		else:
			print('Item not found in cart. Nothing modified.')

	def list_items(self):
		for pos, item in enumerate(self.cart_items):
			print(f'{pos+1} - {item.get_name()}')

	def get_num_items_in_cart(self):
		return len(self.cart_items)

	def get_cost_of_cart(self):
		total = 0
		for pos, item in enumerate(self.cart_items):
			total += item.get_total()
		return total

	def print_total(self):
		print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
		print(f'Number of Items: {self.get_num_items_in_cart()}')
		for item in self.cart_items:
			print('{} {} @ ${:.0f} = ${:.0f}'.format(item.get_name(), item.get_quantity(), item.get_cost(), item.get_total()))
		print(f'Total: ${self.get_cost_of_cart()}')

	def print_descriptions(self):
		print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
		print('Item Descriptions')
		for item in self.cart_items:
			print('{}: {}'.format(item.get_name(), item.get_description()))