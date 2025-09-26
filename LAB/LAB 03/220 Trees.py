def postorder(inorder, preorder):
    if not inorder or not preorder:
        return []
    root=preorder[0]
    for i in range(len(inorder)):
        if inorder[i]==root:
            index=i
            break

    inorder_left=inorder[:index:1]
    inorder_right=inorder[index+1::1]

    length_inorder_left=len(inorder_left)
    length_inorder_right=len(inorder_right)

    preorder_left=preorder[1:1+length_inorder_left]
    preorder_right=preorder[1+length_inorder_left::1]

    postorder_left=postorder(inorder_left, preorder_left)
    postorder_right=postorder(inorder_right, preorder_right)

    tree=postorder_left+postorder_right+[root]

    return tree

N=int(input())

inorder=input().split(" ")
for i in range(len(inorder)):
    inorder[i]=int(inorder[i])

preorder=input().split(" ")
for i in range(len(preorder)):
    preorder[i]=int(preorder[i])

result=postorder(inorder, preorder)
for i in result:
    print(i, end=" ")