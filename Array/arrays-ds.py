def make_sum(arr,i,j):
    top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
    mid = arr[i+1][j+1]
    bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
    return top+mid+bottom
if __name__ == "__main__":
    matrix = []
    for _ in range(6):
        matrix.append(list(map(int, input().split())))

    print(matrix)
    maximum = -99999999
    for i in range(4):
        for j in range(4):
            maximum = max(make_sum(matrix, i, j),maximum)

    print(maximum)
