# Tea =0 Coffe= 1 Milk=2
# array = [2,1,2,2,0,1]

def sortRestroOrder(array):
    tea, coffee, milk = 0, 0, 0

    for i in array:
        if i == 0:
            tea += 1

        if i == 1:
            coffee += 1

        if i == 2:
            milk += 1

    array[:] = [0]*tea + [1]*coffee + [2]*milk

    print(array)


array = [2, 1, 2, 2, 0, 1]

sortRestroOrder(array)
