
class Employee:
    def detail(self,name,salary):
        self.name = name
        self.salaly = salary
    def showData(self):
        print('Employee : {} '.format(self.name) + 'salary : {}'.format(self.salaly))


class Animal:
    pass

emp1 = Employee()
emp1.detail('ABC',20000)
emp1.showData()
print (isinstance(emp1,Employee))
print (isinstance(emp1,Animal))
print(dir(emp1))
print(emp1.__class__)