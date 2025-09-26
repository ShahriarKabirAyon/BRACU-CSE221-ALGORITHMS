def preorder(inorder, postorder):
    if not inorder or not postorder:
        return []
    root=postorder[-1]
    for i in range(len(inorder)):
        if inorder[i]==root:
            index=i
            break

    inorder_left=inorder[:index:1]
    inorder_right=inorder[index+1::1]

    length_inorder_left=len(inorder_left)
    length_inorder_right=len(inorder_right)

    postorder_left=postorder[:length_inorder_left]
    postorder_right=postorder[length_inorder_left:-1]

    preorder_left=preorder(inorder_left, postorder_left)
    preorder_right=preorder(inorder_right, postorder_right)

    tree=[root]+preorder_left+preorder_right

    return tree

N=int(input())

inorder=input().split(" ")
for i in range(len(inorder)):
    inorder[i]=int(inorder[i])

postorder=input().split(" ")
for i in range(len(postorder)):
    postorder[i]=int(postorder[i])

result=preorder(inorder, postorder)
for i in result:
    print(i, end=" ")