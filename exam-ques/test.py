# Python3 program to print postorder
# traversal from preorder and inorder
# traversals

# A utility function to search x in
# arr[] of size n
def search(arr, x, n):

    for i in range(n):
        if (arr[i] == x):
            return i

    return -1

# Prints postorder traversal from
# given inorder and preorder traversals


def printPostOrder(In, pre, n):

    # The first element in pre[] is always
    # root, search it in in[] to find left
    # and right subtrees
    root = search(In, pre[0], n)

    # If left subtree is not empty,
    # print left subtree
    if (root != 0):
        printPostOrder(In, pre[1:n], root)

    # If right subtree is not empty,
    # print right subtree
    if (root != n - 1):
        printPostOrder(In[root + 1: n],
                       pre[root + 1: n],
                       n - root - 1)

    # Print root
    print(pre[0], end=" ")


# Driver code
In = [17, 22, 24, 27, 30, 34, 38, 48]
pre = [30, 22, 17, 27, 24, 38, 34, 48]
n = len(In)

print("Postorder traversal ")

printPostOrder(In, pre, n)

# This code is contributed by avanitrachhadiya2155
