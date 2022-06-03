def arithmetic_arranger(problems, result = False):
    list_line = list(map(lambda i: i.split(), problems))
    symbol = list(map(lambda i: i.split()[1], problems))
    line1, line2, line3, line4 = "", "", "", ""
    arranged_problems, error = "", ""
    permission = False

    if(len(problems) > 5):
        error = "Error: Too many problems."
        permission = True

    correct_operation = list(filter(lambda i: i[1] != "+" and i[1] != "-", list_line))
    if(correct_operation != []):
        error = "Error: Operator must be '+' or '-'."
        permission = True

    correct_length = list(filter(lambda i: len(i[0]) > 4, list_line)) + list(filter(lambda i: len(i[2]) > 4, list_line))
    if(correct_length != []):
        error = "Error: Numbers cannot be more than four digits."
        permission = True

    for i in list_line:
        try:
            correct_type = int(i[0])
        except Exception:
            error = "Error: Numbers must only contain digits."
            permission = True
        try:
            correct_type = int(i[2])
        except Exception:
            error = "Error: Numbers must only contain digits."
            permission = True      

    if(permission):
        arranged_problems = error
        permission = False
        return arranged_problems

    for index, value in enumerate(list_line):
        longest = max(len(value[0]), len(value[2]))
        spacing = longest + 2
        line1 += f"{value[0]:>{spacing}}" + (" " * 4)
        line2 += f"{value[1]}{value[2]:>{spacing - 1}}" + (" " * 4)
        line3 += "-" * spacing + (" " * 4)
        operation = int(value[0]) + int(value[2]) if(value[1] == "+") else int(value[0]) - int(value[2])
        line4 += f"{operation:>{spacing}}" + (" " * 4)

    line1 = line1[0: len(line1) - 4]
    line2 = line2[0: len(line2) - 4]
    line3 = line3[0: len(line3) - 4]
    line4 = line4[0: len(line4) - 4]

    arranged_problems = f"{line1}\n{line2}\n{line3}"
    if(result):
        arranged_problems = f"{line1}\n{line2}\n{line3}\n{line4}"

    return arranged_problems
