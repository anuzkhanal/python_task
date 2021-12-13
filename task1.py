def divisible_number():
    output = []
    for x in range ( 2000, 3200 ):
        if (x % 7 == 0) and (x % 5 != 0):
            output.append(x)
    return output

if __name__== "__main__":

    print("list of numbers divisible by 7 and not by 5 between 200 and 3200 are: \n\n",divisible_number())
