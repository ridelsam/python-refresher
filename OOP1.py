

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    #self is the instance variable!
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format (self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee('Test', 'User', 5000)
emp_2 = Employee('admin', 'nistrator', 5000)

print(emp_1.__dict__)
print(Employee.__dict__)

print(emp_1.email)
print(emp_2.email)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.num_of_emps)


'''
print(emp_1.fullname())
print(emp_2.fullname())

#why need self keyword as argument when creating methods?
#instance are getting passed on the methoda automatically: in line emp_2.fullname(), emp_2 is getting passed on fullname() method
#these two lines here does the exact same thing
print(Employee.fullname(emp_1))
print(emp_1.fullname())
'''