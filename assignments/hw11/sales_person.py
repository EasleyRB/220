class SalesPerson:
    def __init__(self, employee_id, name):
        self.id = employee_id
        self.name = name
        sale_list = []
        self.sales = sale_list

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for i in range(len(self.sales)):
            total = total + i
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        other = SalesPerson
        if other.total_sales() > self.total_sales():
            return -1
        elif other.total_sales() < self.total_sales():
            return 1
        else:
            return 0

    def __str__(self):
        return "{}-{}: {}".format(self.id, self.name, self.total_sales())

