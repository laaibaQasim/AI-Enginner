# args
def sum_all(*args):
    tsum = 0
    for i in args:
        tsum += i
    return tsum

# kwargs
def print_user_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

# both
def fun(*args, **kwargs):
    # print("Args:", ", ".join(map(str, args)))
    print("Args:", *args)
    print(f"Kwargs: ", *[f"{kwarg}"for kwarg in kwargs])


print(sum_all(1,2,3,4))
print_user_info(name="ema", age=21, profession="SE")
fun(1,2,3, name="ema", age=21)

# module import
from utils.math_functions import multiply
print(multiply(1,2,3,4))
