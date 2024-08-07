#description for furniture
lovely_loveseat_description=("Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.\n")
#price of furniture
lovely_loveseat_price = 254.00

#another description of another peice
stylish_settee_description=("Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.\n")
#set price of settee
stylish_settee_price = 180.50

#one more
luxurious_lamp_description=("Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.\n")
#price of lamp
luxurious_lamp_price = 52.15

#sales tax of the store
sales_tax = .088

#values to use concatenation
#first customer is making there purchase
customer_one_total = 0
#list of the descriptions they buy
customer_one_itemization = ""

#customer buys loveseat here is their reciept
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

#buys lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

#ready to checkout...lets add that sales tax
customer_one_tax = customer_one_total*sales_tax
customer_one_total+=customer_one_tax

#here's their reciept
print("Customer One Items:", customer_one_itemization)
print("Customer One Total:", round(customer_one_total, 2))
