def exponent(base,pow):
    result=1
    for i in range(pow):
        result=result*base
    return result
print(exponent(2,4))