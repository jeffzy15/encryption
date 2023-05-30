import math

def word_to_matrix(word):
    word = word.upper() # convert to uppercase
    matrix = []
    row = []
    num_columns = math.ceil(len(word) / 2)
    for i, letter in enumerate(word):
        if letter.isalpha(): # only consider letters
            char_num = ord(letter) - 65 # convert letter to number, A = 0, B = 1, ...
            row.append(char_num)
        if (i + 1) % num_columns == 0 or i == len(word) - 1: # create a new row after every num_columns characters
            matrix.append(row)
            row = []
    if len(row) > 0: # add remaining characters to a new row if necessary
        matrix.append(row + [0] * (num_columns - len(row)))
    
    print("Word matrix:", matrix)
    return matrix
    

def matrix_multiplication(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        result_row = []
        for j in range(len(matrix2[0])):
            result_num = 0
            for k in range(len(matrix2)):
                result_num += matrix1[i][k] * matrix2[k][j]
            result_row.append(result_num)
        result.append(result_row)
    return result

def matrix_to_word(matrix):
    word = ""
    for row in matrix:
        for num in row:
            while num > 26: # divide by 26 until num is <= 26
                num = num % 26
            letter = chr(num + 65) # convert number to letter, 0 = A, 1 = B, ...
            word += letter
    return word

# input first matrix
print("Enter the encoding matrix (2x2):")
first_matrix = []
for i in range(2):
    row = input(f"Enter row {i + 1} (space-separated values): ")
    first_matrix.append([int(x) for x in row.split()])

# input word
word = input("Enter a word: ")
word_matrix = word_to_matrix(word)

# multiply matrices
result_matrix = matrix_multiplication(first_matrix, word_matrix)

# convert result to word
result_word = matrix_to_word(result_matrix)

# output result
print("Multiplied matrix:", result_matrix)
print("Result word:", result_word)
