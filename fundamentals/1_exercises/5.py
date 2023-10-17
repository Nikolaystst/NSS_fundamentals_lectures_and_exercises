orders = int(input())
total_price = 0

for i in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    caps_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= caps_per_day <= 2000:
        todays_order = price_per_capsule * days * caps_per_day
        print(f"The price for the coffee is: ${todays_order:.2f}")
        total_price += todays_order

print(f"Total: ${total_price:.2f}")
