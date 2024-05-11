date = input("enter the date in format dd/mm/yy ")


l = date.split("/")

if l[0] < "32" and l[1] <"13":
    print("Day", l[0])
    print("Month", l[1])
    print("Year", l[2])

else:
    print("invald date")



