print("Today's sandwich orders:")
sandwich_orders = ['pastrami','cheese', 'grilled cheese', 
    'pastrami', 'tuna', 'roast beef', 'pastrami']
finished_sandwiches = []

for order_number, order in enumerate(sandwich_orders,1):
    print(f"Order {order_number}: {order}")

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")
