def add1(f):

    def add2(g):
        return add1(lambda x:f(g(x)))  
    return add2 

add_one = lambda x:x+1
mul_three = lambda x:x*3

add1
