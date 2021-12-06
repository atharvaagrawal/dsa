from binarytree import tree


def height(root):
    if root is None:
        return 0

    left = height(root.left)
    right = height(root.right)

    return 1 + max(left, right)


# Create a random binary
# tree of any height
root = tree()
print("Binary tree of any height :")
print(root)

print("Height: ", height(root))
