print("Submitted by: NERIO, Shaira Joy B. (R14)")
print()
print("Order Calculator")
print()
cost_per_shirt = float(input("Shirt Price: "))
number_of_shirt = int(input("Quantity: "))
print()
print("Order Summary: ")
print()

#Calculate the total
subtotaL = number_of_shirt * cost_per_shirt
print("Total: ",subtotaL)
membership_discount = subtotaL * 0.2
print("Discount(0.2): ",membership_discount)
final_total = subtotaL - membership_discount

print("You ordered", number_of_shirt, "shirts @", cost_per_shirt, "pesos per shirt.")
print("Your total order is", final_total, "pesos.")
print()

cash_tendered = float(input("Cash Tendered: "))

#Calculate the change
change = cash_tendered - final_total

print("Change: ", change)
