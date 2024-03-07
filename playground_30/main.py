import my_functions


def get_total(orders):
  # Tu código aquí 👇
  keys, values = my_functions.calc_total()
  print(keys, values)

  result = my_functions.calc_total(orders, total)
  print(result)


orders = [{
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
}, {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
}, {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
}]

total = get_total(orders)
print(total)

print(my_functions.calc_total)


-----
# Solución No.2

from my_functions import get_totals, calc_total

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_totals(orders)
result = calc_total(total)
print(result)