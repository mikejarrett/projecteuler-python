# -*- coding: utf-8 -*-

def modified_fibonacci():
    """ Modified Fibonacci sequence where if the result is under 4000000
	and result is even yield the result. Else yield 0 (throw away odd results)
	"""
    a, b = 0, 1
    while True:
        if (a >= 4000000) :
            return
        if a % 2 == 0:
            yield a
        else:
            yield 0
        a, b = b, a + b

		
if __name__ == "__main__":
    result = sum(number for number in modified_fibonacci())
    assert result == 4613732
    print(result)