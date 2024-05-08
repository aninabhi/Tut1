product  = input("enter the product name")
price = input("enter the price of product")

total_len = len(product) + len(price)

dots = "." * (25 - total_len)

print(product+dots+"Rs",price)



