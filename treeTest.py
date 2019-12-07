from binarytree import Node
import math
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.right = Node(4)
#
# print(root)


testlist = [1,4,7,14,3,1,6,2,4,12]
def build_bst(list):
    list.sort()
    if not list:
        return None

    # find middle
    mid = math.floor(int(len(list)) / 2)

    # make the middle element the root
    root = (Node(list[mid]))
    root.left = (build_bst(list[:mid]))
    root.right = (build_bst(list[mid + 1:]))
    return root

print(build_bst(testlist))
print(build_bst(testlist).pprint(index=True))
