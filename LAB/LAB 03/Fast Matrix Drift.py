def multiplication(B, C):
    modulo=10**9+7
    result=[[None, None],[None, None]]

    result[0][0]=(B[0][0]*C[0][0]+B[0][1]*C[1][0])%modulo
    result[0][1]=(B[0][0]*C[0][1]+B[0][1]*C[1][1])%modulo
    result[1][0]=(B[1][0]*C[0][0]+B[1][1]*C[1][0])%modulo
    result[1][1]=(B[1][0]*C[0][1]+B[1][1]*C[1][1])%modulo

    return result

def fastmatrix(matrix, X):
    if X==1:
        return matrix
    
    dc_matrix=fastmatrix(matrix, X//2)

    if X%2==0:
        even_multiplication=multiplication(dc_matrix, dc_matrix)
        return even_multiplication
    else:
        even_multiplication=multiplication(dc_matrix, dc_matrix)
        odd_multiplication=multiplication(even_multiplication, matrix)
        return odd_multiplication
    
T=int(input())
for i in range(T):
    matrix=input().split(" ")
    X=int(input())
    for j in range(len(matrix)):
        matrix[j]=int(matrix[j])

    matrix=[matrix[0:2:1], matrix[2::1]]

    answer=fastmatrix(matrix, X)
    print(f"{answer[0][0]} {answer[0][1]}")
    print(f"{answer[1][0]} {answer[1][1]}")