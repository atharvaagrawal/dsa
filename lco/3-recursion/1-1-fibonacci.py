# Fibonaci using Diary:

n = int(input("Enter the Fibo Number:"))


def findfbth(N, diary={1: 0, 2: 1}):
    if N in diary:
        return diary[N]

    else:
        diary[N] = findfbth(N-1, diary) + findfbth(N-2, diary)
        return diary[N]


print(findfbth(n))
