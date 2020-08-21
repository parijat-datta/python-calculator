class Calculator: 
    def __init__(self, number1:int,number2:int):
        self.num1=number1
        self.num2=number2

    def add(self):
        return (self.num1+self.num2)

    def subtract(self):
        if (self.num2>self.num1):
            return (self.num2-self.num1)
        return (self.num1-self.num2)


    def multiplication(self):
        return (self.num1*self.num2)

    def division (self):
        if (self.num2>self.num1):
            return (self.num2/self.num1)
        return (self.num1/self.num2)

    def modulus (self):
        return round(self.num1%self.num2,2) 

    def percentage (self):
        return round(((self.num1/self.num2)*100),2) 
    
    def __call__(self):
        return self.add(), self.subtract()
       

if __name__ == "__main__":

    # userinput=input("Please enter two comma separated numbers: ")
    # data=userinput.split(',')
    # calculator=Calculator(number1=int (data[0]),number2=int (data[1]))
    # print ("Choose an Option")
    # option= input("1. Add 2. Sub 3. Multiplication 4. Division 5. Percentage 6. Modulus\n")
    # input_data=int(option)
    n=1
while(n!=0):
    userinput=input("Please enter two comma separated numbers: \n")
    data=userinput.split(',')
    calculator=Calculator(number1=int (data[0]),number2=int (data[1]))
    # print(f'{calculator()}')
    print ("Choose an Option")
    option= input("1. Add 2. Sub 3. Multiplication 4. Division 5. Percentage 6. Modulus\n\n")
    input_data=int(option)

    if (input_data==1):
        print (f'Addition of the Given Numbers is: {calculator.add()}')
                
    if (input_data==2):
        print (f'Subtraction of the Given Numbers is: {calculator.subtract()}')

    if (input_data==3):
        print (f'Multiplication of the Given Numbers is: {calculator.multiplication()}')

    if (input_data==4):
        print (f'Division of the Given Numbers is: {calculator.division()}')

    if (input_data==5):
        print (f'Percentage of the Given Numbers is: {calculator.percentage()}')

    if (input_data==6):
        print (f'Modulus of the Given Numbers is: {calculator.modulus()}')

    another_operation=input("Do you want to do another operation: Press 1 for yes & 0 for no\n\n")
    n=int(another_operation)

    if(n==0):
        print("Calculator is closing")



