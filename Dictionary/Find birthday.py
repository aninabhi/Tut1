birthday= {
            "Sachin" : '02/11/1989' ,
            "Abhishek" : '31/07/1991' ,
            "Abhijeet" : '17/10/1993',
            "Ankit"   : '9/10/1992',
            "Himanshu" : '27/04/1998',
            "Ayush"  : '5/07/2008'
}

Name = input("Enter the name ")
if Name in birthday:
     print( "Mr. {} was born on {} " .format(Name, birthday[Name]))

else:
    print("Invalid entery")

