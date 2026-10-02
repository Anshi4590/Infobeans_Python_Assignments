class Employee:


      def __init__(self,employee_id,name ,salary ,dept):

            self.employee_id = employee_id
            self.salary = salary 
            self.name = name
            self.dept = dept


      def display_details(self):

          print(f"{self.employee_id} {self.name} {self.salary} {self.dept}")

      def check_salary(self):

           if self.salary>40000:
                self.display_details()

      def check_dept(self):

           if self.dept =="IT":
                self.display_details()

      def highest_salary(self,high):
            return self.salary>high.salary
                  

      def total_salary(self,total):
        total+=self.salary
        return total
     


      def average(self,employee_db):
          total=0

          for emp in employee_db:

            total+=emp.salary
            return total/len(employee_db)
        

           

              
           
         
                  
            




