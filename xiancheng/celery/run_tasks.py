from tasks import add, su
from random import randint

for i, v in enumerate([randint(1, 10) for i in range(10)]):
    result0 = su.delay(i, v)
    print("===========Is task ready1: ", result0.ready())

result = add.delay(1, 2)
print("Is task ready: ", result.ready())
run_result = result.get(timeout=1)
print("Task result: ", run_result)
print("Is task ready1: ", result.ready())