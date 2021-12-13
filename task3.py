
def square_num():

    dict_num = dict()

    user_input = int(input("Please enter the value of x: "))

    for x in range(1,user_input+1):
        dict_num[x]=x**2

    for key, value in dict_num.items():
        print (str(key)+'**2 ='+str(value))

if __name__== "__main__":

    square_num()

