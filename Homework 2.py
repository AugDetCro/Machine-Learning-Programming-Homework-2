# Machine Learning
# Homework Assignment #2

if __name__ == '__main__':
    # QUESTION 1:
    # Use a for loop to produce a sideways pyramid using "*"
    print("Question 1: Pyramid\n")

    maxHeight = 5
    totalWidth = (maxHeight*2) - 1

    n = 5
    for i in range(0, totalWidth):
        if(i < maxHeight):
            for j in range(0, i + 1):
                print("*", end = " ")
            print()
        else:
            for j in range(0, maxHeight - 1):
                print("*", end = " ")
            maxHeight -= 1
            print()


    # QUESTION 2
    # Print out the odd indexes of a list
    print("\nQuestion 2: Odd Indexes\n")

    print("All odd-indexed entities in the given list:")

    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    for x in range(len(my_list)):
        if x % 2 == 0:
            continue
        else:
            print(my_list[x])

    # QUESTION 3
    # Write a code that appends the type of elements from a given list

    print("\nQuestion 3: list and its types:\n")

    list_x = [23, 'Python', 23.98]

    print(list_x)

    list_x_types = []

    for x in range(len(list_x)):
        list_x_types.append(type(list_x[x]))

    print(list_x_types)

    # QUESTION 4
    # Input a list and output a list with only unique instances of the input
    print("\nQuestion 4: Unique listing\n")

    sample_list = [1, 2, 3, 3, 3, 3, 4, 5]

    print("Unrefined list: ", sample_list)

    output_list = []

    observed = 0

    output_list.append(sample_list[0])

    for x in range(len(sample_list)):
        observed = 0
        for y in range(len(output_list)):
            if output_list[y] == sample_list[x]:
                observed = 1
        if observed == 0:
            output_list.append(sample_list[x])

    print("Refined list: ", output_list)


    # QUESTION 5
    # Write a function that accepts a string and calculate the number of upper-case letters and lower-case
    # letters
    print("\nQuestion 5: Counting upper/lowercase chars\n")

    input_string = ("The quick Brow Fox")

    uppercase_letters = 0
    lowercase_letters = 0

    for x in input_string:
        if x.isupper():
            uppercase_letters += 1
        if x.islower():
            lowercase_letters += 1
    print("Given list:", input_string)
    print(f"No. of Upper-case characters:", uppercase_letters)
    print(f"No. of Lower-case characters:", lowercase_letters)