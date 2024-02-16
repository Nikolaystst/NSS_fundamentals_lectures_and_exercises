price = 0
taxes = 0
type_of_customer = ''

while True:
    current = input()

    if current in ['special', 'regular']:
        type_of_customer = current
        break

    if float(current) < 0:
        print('Invalid price!')
        continue

    price += float(current)
    taxes += 0.2 * float(current)

total_price = price + taxes

if type_of_customer == "special":
    total_price -= 0.1 * total_price

if total_price == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_price:.2f}$")
