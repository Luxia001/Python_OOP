
class Employee:
    _employee = []
    def __init__(self):
        self.name = 'no name'
        self._salary = 0
        self.__age = 20
        
    def setAge(self, age):
        self.__age = age
    def getAge(self):
        return self.__age
    def detail(self,name,salary):
        self.name = name
        self._salary = salary
    def showData(self):
        print('Employee : {} '.format(self.name) )
        print('salary : {}'.format(self._salary))
        print('age: {}'.format(self.__age))
    
    def showDepartment(self,department):
        print('Department : {}'.format(department))
        
    def incomeSalary(self):
        return self._salary * 12
