from employee import Employee

class Sale(Employee):
    __department = 'sale'
    def __init__(self,area):
        super().__init__()
        self.showDepartment(self.__department)
        super().setAge(25)
        self.area = '51'
    def showData(self):
        print("name : {}".format(self.name) )
        print("age : {}".format(self.getAge()) )
        print("salary : {} income : {}".format(self._salary,self.incomeSalary()) )
        print("area : {}".format(self.area) )
        