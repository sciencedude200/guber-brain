from timeit import repeat

output = 1
bias = 5

input1 = 1
input1value = 2.9
input2 = 0
input2value = 0.9
input3 = 1
input3value = -0.1

while True:
    input1sum = input1 * input1value
    input2sum = input2 * input2value
    input3sum = input3 * input3value
    sum = input1sum + input2sum + input3sum
    print(input1value,input2value,input3value)

    if (sum > bias):
        print("1")
    else:
        print("0")

    i1 = input ("was it right or wrong ")

    if (i1 == "w"):
        i2 = input ("to high or too low ")
        if (i2 == "h"):
            input1value = input1value - 0.10
            input2value = input2value - 0.10
            input3value = input3value - 0.10
            print (input1value,input2value,input3value)
        else:
            input1value = input1value + 0.10
            input2value = input2value + 0.10
            input3value = input3value + 0.10
            print (input1value,input2value,input3value)
    
