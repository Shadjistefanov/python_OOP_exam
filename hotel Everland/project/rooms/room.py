
class Room:
    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        self.appliances = []
        self.count = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    def calculate_expenses(self, *args):
        self.expenses = sum(el.get_monthly_expense() for seq in args for el in seq)


    @property
    def cost(self):
        return self.expenses + self.room_cost

    def __str__(self):
        #self.count += sum(app.get_monthly_expense() for app in self.appliances)
        return '\n'.join([
            f'{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$'
        ] + [
            f'--- Child {idx + 1} monthly cost: {child.get_monthly_expense():.2f}$' for idx, child in enumerate(self.children)
        ] + [
            f'--- Appliances monthly cost: {sum(app.get_monthly_expense() for app in self.appliances)}$'
        ])

