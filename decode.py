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

def convert_to_letter(matrix):
    converted_matrix = []
    for row in matrix:
        converted_row = []
        for element in row:
            if element >= 0 and element <= 25:
                converted_row.append(chr(element + 65))
            else:
                if element > 25:
                    remainder = element % 26
                    converted_row.append(chr(65 + remainder))
                else:
                    remainder = abs(element) % 26
                    converted_row.append(chr(90 - remainder + 1))
        converted_matrix.append(converted_row)
    return converted_matrix

def convert_to_word(converted_matrix):
    word = ''
    for row in converted_matrix:
        for element in row:
            word += element
    return word

# input first matrix
print("Enter the decoding matrix (2x2):")
first_matrix = []
for i in range(2):
    row = input(f"Enter row {i + 1} (space-separated values): ")
    first_matrix.append([int(x) for x in row.split()])

# input word
word = input("Enter a word: ")
word_matrix = word_to_matrix(word)

# multiply matrices
result_matrix = matrix_multiplication(first_matrix, word_matrix)
convertedMatrix = convert_to_letter(result_matrix)
convertedWord = convert_to_word(convertedMatrix)

print("Multiplied matrix:", result_matrix)
print("Converted matrix:", convertedMatrix)
print("Decoded word:", convertedWord)