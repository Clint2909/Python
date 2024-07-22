class MultipleFunctions():
    def subfields():
        print("sub-fields in AI are:")
        subfields =["Machine Learning", "Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for subcate in subfields:
            print(subcate)
    
    def OddEven():
        Number=int(input("Enter a number:"))
        print("Enter a number:",Number)
        if(Number%2)==0:
            print(f"{Number} is Even Number")
        else:
            print(f"{Number} is Odd Number")
    
    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        print("Your Gender:",gender)
        print("Your Age:",age)
        if gender =="Male" and age>=22:
            print("ElIGIBLE")
        elif gender=="Female" and age>=18:
            print("ElIGIBLE")
        else:
            print("Not ElIGIBLE")
    
    def percentage():
        Subject1=int(input("Enter the Mark:"))
        Subject2=int(input("Enter the Mark:"))
        Subject3=int(input("Enter the Mark:"))
        Subject4=int(input("Enter the Mark:"))
        Subject5=int(input("Enter the Mark:"))
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        Percentage=(Total/500)* 100
            
        print("Subject1=",Subject1)
        print("Subject2=",Subject2)
        print("Subject3=",Subject3)
        print("Subject4=",Subject4)
        print("Subject5=",Subject5) 
        print("Total:",Total)
        print("Percentage:",Percentage)
    
    def triangle():
        Height=int(input("Enter the Height:"))
        Breadth=int(input("Enter the Breadth:"))
        Area=(Height*Breadth)/2
        print("Height:",Height)
        print("Breadth:",Breadth)
        print("Area formula:(Height*Breadth)/2")
        print("Area of Triangle:",Area)
        Height1=int(input("Enter the Height1:"))
        Height2=int(input("Enter the Height2:"))
        Breadth1=int(input("Enter the  Breadth:"))
        Breadth=Breadth1
        Perimeter_formula=Height1+Height2+Breadth1
        print("Height1:",Height1)
        print("Height2:",Height2)
        print("Breadth:",Breadth)
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",Perimeter_formula)
           