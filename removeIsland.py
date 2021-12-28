import numpy as np

def matrix_rand(n):
    return np.random.randint(2, size=(n,n))
def get_corner(matrix):
    n,m = matrix.shape
    n,m = n-1, m-1
    for i in range(m):
        if matrix[0,i] == 1:
            matrix[0,i] = -1
        if matrix[n,i] ==1:
            matrix[n,i] = -1
    for i in range(n):
        if matrix[i,0] ==1:
            matrix[i,0]= -1
        if matrix[i, m] ==1:
            matrix[i,m]= -1
    return matrix
        
def main():
    matrix = matrix_rand(10)
    print(matrix)
    matrix = get_corner(matrix)
    print(matrix)


if __name__ == "__main__":
    main()

# matrix(10)