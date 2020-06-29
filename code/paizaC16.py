input_line = input()
translate = input_line.translate(str.maketrans("AEGIOSZ", "4361052"))
print(translate)