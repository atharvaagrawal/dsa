i=0
def hanoi(disks, source, auxiliary, target):
    global i
    if disks == 1:
        i=i+1
        print(i,' Move disk 1 from peg {} to peg {}.'.format(source, target))
        return
 
    hanoi(disks - 1, source, target, auxiliary)
    i=i+1
    print(i,'Move disk {} from peg {} to peg {}.'.format(disks, source, target))
    hanoi(disks - 1, auxiliary, source, target)
 
 
disks = int(input('Enter number of disks: '))
hanoi(disks, 'A', 'B', 'C')