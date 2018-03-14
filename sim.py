from gpkit import Model, Variable, parse_variables

class Trip(Model):
	"""
	Variables
	---------
	cost		[-]		cost to the company of operating a trip
	t 			[min]	time for trip, from A to B
	total_cost	[-]		total cost for the trip
	"""

	def setup(self):
		exec parse_variables(Trip.__doc__)
		customer = Customer()
		constraints = [cost >= Variable('cost_lim',1,'-'),
					   t >= Variable('t_lim',10,'minutes'),
					   total_cost >= cost + t*customer.time_value]
		return constraints,customer

class Customer(Model):
	"""
	Variables
	---------
	time_value	23  [1/hr]	customer value of time
	"""
	def setup(self):
		exec parse_variables(Customer.__doc__)
		constraints = []
		return constraints
T = Trip()
T.cost = T.total_cost
sol = T.solve("mosek")
print sol.table()

