from draftsman.data import recipes, entities, items

class ratio:
	def __init__(self, item=None, ips=None, assembler=None, recurse=False):
		self.item=item
		self.goal_items_per_second=ips
		self.item=self.set_item()
		if 'category' in recipes.raw[self.item].keys() and recipes.raw[self.item]['category'] == 'smelting':
			del self
			return
		self.goal_items_per_second=self.set_goal_ips()
		self.made_in=self.get_made_in(self.item)
		self.assembler=assembler if assembler else self.set_assembler() if 'assembling-machine-3' in self.made_in else self.made_in[0]
		self.assembler_craft_speed=entities.raw[self.assembler]['crafting_speed']
		self.actual_production=self.get_real_production()
		self.items_per_second=self.get_ips()
		self.assemblers_needed=self.get_assemblers_needed()
		self.ingredients=self.get_ingredients(self.item)
		self.show()
		if recurse:
			for x in self.ingredients:
				self.dive=ratio(x[0], self.goal_items_per_second*x[1], self.assembler, True)

	def show(self):
		print('-'*50)
		print(self.item, '@', str(self.goal_items_per_second)+'/s', 'in', self.assembler)
		print(self.items_per_second, 'items/sec from 1')
		print(self.assemblers_needed, 'needed to satisfy')
		print('ingredients', self.ingredients)

	def set_item(self):
		item=self.item
		while not item or not items.raw[item]:
			item=input('item: ')
		return item

	def set_goal_ips(self):
		goal_items_per_second=self.goal_items_per_second
		while not goal_items_per_second:
			goal_items_per_second=input('item/s: ')
		return float(goal_items_per_second)

	def set_assembler(self):
		assembler_lvl=self.assembler
		assembling_machines=['assembling-machine', 'assembling-machine-2', 'assembling-machine-3']
		print('[1]', 'assembling machine,')
		print('[2]', 'assembling machine 2, or')
		print('[3]', 'assembling machine 3')
		assembler_lvl=int(input('assembling machine lvl: ')) if not assembler_lvl else assembler_lvl
		if not assembler_lvl or assembler_lvl not in [1, 2, 3]:
			assembler_lvl=self.set_assembler()
		return assembling_machines[assembler_lvl-1]

	def get_ingredients(self, item):
		if recipes.raw[item]:
			ingredients=recipes.get_recipe_ingredients_and_counts(item)
			return ingredients

	def get_made_in(self, item):
		made_in=[k for k in recipes.for_machine.keys() if item in recipes.for_machine[k]]
		return made_in

	def get_real_production(self):
		item_base_craft_speed=recipes.raw[self.item]['energy_required'] if 'energy_required' in recipes.raw[self.item].keys() else 0.5
		actual_production_speed=item_base_craft_speed/self.assembler_craft_speed
		return actual_production_speed

	def get_ips(self):
		items_created_per_craft=recipes.raw[self.item]['result_count'] if 'result_count' in recipes.raw[self.item].keys() else 1
		items_per_second=1/(self.actual_production/items_created_per_craft)
		return items_per_second

	def get_assemblers_needed(self):
		assemblers_needed=self.goal_items_per_second/self.items_per_second
		return assemblers_needed

new=ratio('advanced-circuit', 10, 'assembling-machine-2', True)