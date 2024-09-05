km = float(input("Enter the kilometers to drive: "))
liters_per_km = float(input("Enter the required litre per kilometer: "))
price_per_liter = float(input("Enter the price per litre of fuel: "))

total_liters = km * liters_per_km
total_cost = total_liters * price_per_liter
print(f"\nFor a trip of {km:.2f} kilometers, using {liters_per_km:.2f} liters per kilometer,")
print(f"at a fuel price of {price_per_liter:.2f} per liter, the total cost of the trip will be: ${total_cost:.2f}")