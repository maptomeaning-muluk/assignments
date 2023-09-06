def print_numbers_greater_than_50(integer_list):
    # an empty list for storing variables
    greater_than_50 = []

    for i in integer_list:
        if i > 50:
            greater_than_50.append(i)

    # Here we will check if  any numbers greater than 50
    if greater_than_50:
        return f"The numbers {', '.join(map(str, greater_than_50))} are greater than 50."
    else:
        return "There are no numbers greater than 50 in the list."


# Example usage
integer_list = [52, 2, 33, 79, 88]
print(print_numbers_greater_than_50(integer_list))
