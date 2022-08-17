from draftsman.data import recipes, entities, items

class ratio:
	def __init__(self, item=None, ips=None):
		self.get_inputs()
		self.item=item
		self.goal_items_per_second=ips
		self.item=self.set_item()
		self.goal_items_per_second=self.set_goal_ips()
		self.made_in=self.get_made_in(self.item)
		self.assembler=self.set_assembler() if 'assembling-machine-3' in self.made_in else self.made_in[0]
		self.assembler_craft_speed=entities.raw[self.assembler]['crafting_speed']
		self.real_production=self.get_real_production()
		self.ips=self.get_ips()
		self.assemblers_needed=self.get_assemblers_needed()
		self.show()

	def show(self):
		print(self.item, str(self.goal_items_per_second)+'/s')
		print(self.assembler, self.assembler_craft_speed)
		print(self.ips, 'for one')
		print(self.assemblers_needed, 'needed')

	def set_item(self):
		item=self.item
		while not item or not items.raw[item]:
			item=input('item: ')
		return item

	def set_goal_ips(self):
		goal_items_per_second=self.goal_items_per_second
		while not goal_items_per_second or not goal_items_per_second.isnumeric():
			goal_items_per_second=float(input('item/s: '))
		return goal_items_per_second

	def get_made_in(self, item):
		made_in=[k for k in recipes.for_machine.keys() if item in recipes.for_machine[k]]
		return made_in

	def set_assembler(self):
		assembling_machines=['assembling-machine', 'assembling-machine-2', 'assembling-machine-3']
		print('[1]', 'assembling machine,')
		print('[2]', 'assembling machine 2, or')
		print('[3]', 'assembling machine 3')
		assembler_lvl=int(input('assembling machine lvl: '))
		if not assembler_lvl or assembler_lvl not in [1, 2, 3]:
			assembler_lvl=get_issembler()
		return assembling_machines[assembler_lvl-1]

	def get_real_production(self):
		item_base_craft_speed=recipes.raw[self.item]['energy_required'] if 'energy_required' in recipes.raw[self.item].keys() else 0.5
		actual_production_speed=self.item_base_craft_speed/self.assembler_craft_speed
		return actual_production_speed

	def get_ips(self):
		items_created_per_craft=recipes.raw[self.item]['result_count'] if 'result_count' in recipes.raw[self.item].keys() else 1
		items_per_second=1/(self.actual_production_speed/items_created_per_craft)
		return items_per_second

	def get_assemblers_needed(self):
		assemblers_needed=self.goal_items_per_second/self.items_per_second
		return assemblers_needed

new=ratio('electronic-circuit', 10)