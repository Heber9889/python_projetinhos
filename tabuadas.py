def tabuadas():
    print("#-----------------")
    for i in range(1, 11):
        print("#-----------------")
        for j in range(1, 11):
            print("#:""{} * {} = {}"" :#".format(i, j, i * j))
            
tabuadas()
