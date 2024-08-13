def format_indian_currency(number):
    integer_part, fractional_part = str(number).split('.')

    integer_part_reversed = integer_part[::-1]

    indian_format = integer_part_reversed[:3] + ''.join(
        [',' + integer_part_reversed[i:i + 2] for i in range(3, len(integer_part_reversed), 2)]
    )
    formatted_integer_part = indian_format[::-1]
    formatted_number = formatted_integer_part + '.' + fractional_part

    return formatted_number

number = 123456.7891
formatted_number = format_indian_currency(number)
print(formatted_number)  
