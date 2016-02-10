from __future__ import print_function # noslide
## <h1>how decorators work</h1>
## <ul class="incremental">
##   <li>Fibonacci!</li>
## </ul>

def fib(x):
    if x in [1, 2]:
        return 1
    return fib(x - 1) + fib(x - 2)
#!
print(fib(3))
print(fib(10))
## show-output
