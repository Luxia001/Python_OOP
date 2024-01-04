from employee import Employee
from sale import Sale

emp1 = Employee()
emp1.detail('Anna',20000)
emp1._employee.append(emp1.name)
emp1.showData()

emp2 = Employee()
emp2.name = 'Bob'
emp2._salary=200
emp2.__age = 12
emp2.setAge(30)
emp1._employee.append(emp2.name)
emp2.showData()
print('age emp2 : {}'.format(emp2.getAge()))


sale1 = Sale('51')
sale1.name = 'Catherine'
sale1._salary=20000
sale1._employee.append(sale1.name)
sale1.showData()

print('emp count: {}'.format(len(Employee._employee)))
print('emp list: {}'.format(Employee._employee))