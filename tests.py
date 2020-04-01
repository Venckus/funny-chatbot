# def boxBlur(image):

#     threeMatrix = []
#     threeBlur = []
#     blurredImage = []

#     for i in range(1, len(image) - 1):
#         for j in range(1, len(image) - 1):
#             threeMatrix.append(
#                 [image[i - 1][j - 1], image[i - 1][j], image[i - 1][j + 1],
#                  image[i][j - 1],     image[i][j],     image[i][j + 1],
#                  image[i + 1][j - 1], image[i + 1][j], image[i + 1][j + 1]]
#             )
#     for x in range(len(threeMatrix)):
#         threeBlur.append(int(sum(threeMatrix[x]) / len(threeMatrix[x])))

#     for z in range(0, len(threeBlur), (len(image[0]) - 2)):
#         blurredImage.append(threeBlur[z:z + (len(image[0]) - 2)])
    
#     return blurredImage

def pixel(matrix,i,j):
    total = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            total += matrix[x][y]
    return total//9

def boxBlur(image):
    sol = []
    row = len(image)
    col = len(image[0])
    for i in range(1, row - 1):
        temp = []
        for j in range(1, col - 1):
            temp.append(pixel(image, i, j))
        sol.append(temp)
    
    return sol
print(boxBlur([[1,1,1], 
               [1,7,1], 
               [1,1,1]]), 'result should be: [[1]]')
print(boxBlur([[36,0,18,9], 
                [27,54,9,0], 
                [81,63,72,45]]), 'result should be: [[40,30]]')