class Employee:
    Emp_id = 111
    Emp_name = "Nitesh"
    Emp_salary = 50000
    Emp_dept = "IT"
    Emp_age = 20
    
    def salary(self):
        print("Salary of Employee is",self.Emp_salary)
    def name(self):
        print("Employee name is ",self.Emp_name)
    def detail(self):
        print(self.Emp_id,self.Emp_name,self.Emp_salary,self.Emp_dept,self.Emp_age)
        
c = Employee()
d = Employee()
print("Calling object 1......")
c.salary()     
c.name()
c.detail()
print("calling object 2.......")
d.salary()
d.name()
d.detail()       