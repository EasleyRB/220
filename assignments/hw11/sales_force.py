from sales_person import SalesPerson

class SalesForce:
    def __init__(self):
        self.sales_people = []
        self.report = []

    def add_data(self, file_name):
        infile = open(file_name, 'r')
        lines = infile.readlines()
        for line in lines:
            self.sales_people.append(line)

    def quota_report(self, quota):
        id = []
        employee = []
        sales = []
        total = []
        list = []
        nlist = []
        olist = []
        for i in self.sales_people:
            sales_list = i.split(', ')
            id.append(sales_list[0])
            employee.append(sales_list[1])
            sales.append(sales_list[2])
        for j in sales:
            sales_spl = j.split(' ')
            acc = 0
            for a in sales_spl:
                acc += float(a)
            total.append(acc)
        for k in total:
            if k >= quota:
                list.append(bool(1))
        for l in range(4):
            nlist.append(int(id[l]))
            nlist.append(employee[l])
            nlist.append(total[l])
            nlist.append(list[l])
            olist.append(nlist)

    def top_seller(self):
        pass

    def individual_sales(self, employee_id):
        for i in range(len(self.sales_people)):
            sales_spl = i.split(", ")
            if employee_id == sales_spl[0]:
                return sales_spl[2]
            else:
                return None

    def get_sale_frequencies(self):
        pass



