original_text = input('Введите сообщение:')
lenght_text = len(original_text)
print(f'Количество символов в строке: {lenght_text}')
print(f"Второй символ строки: {original_text[1]}")
print(f"Последний символ строки: {original_text[-1]}")
print(f"Первые 3 символа строки:{original_text[0:3]}")
print(f"Последние 3 символа строки:{original_text[-3:]}")
print("\u001b[33;1m")
print("\u001b[44m")
print(f"{original_text}")
print("\u001b[0m")
color_start = int(input('С какого символа начать покраску?'))
color_end = int(input('Каким символом закончить покраску?'))
color_name = input('В какой цвет радуги покрасить текст?')
if color_name == "красный":
    color_name = "\u001b[31m"
elif color_name == "оранжевый":
    color_name = "\u001b[38;5;202m"
elif color_name == "желтый":
    color_name = "\u001b[38;5;190m"
elif color_name == "зеленный":
    color_name = "\u001b[32m"
elif color_name == "голубой":
    color_name = "\u001b[38;5;117m"
elif color_name == "синий":
    color_name = "\u001b[34m"
else:
    color_name = "\u001b[38;5;90m"
if color_end == -1:
    colorized_text = original_text[color_start :]
    print(f'{original_text[0:color_start]}{color_name}{colorized_text}\u001b[0m')
else:    
    colorized_text = original_text[color_start : color_end]
    print(f'{original_text[0:color_start]}{color_name}{colorized_text}\u001b[0m{original_text[color_end:]}')
old_char = input('Введите символ который хотите заменить:')
new_char = input('Введите символ на который вы хотите заменить:')
modified_text = original_text.replace(f'{old_char}', f'{new_char}')
print(f'{modified_text}')
even_chars = (f"{original_text[::2]}")
odd_chars = (f"{original_text[1::2]}")
print(f"Нечетные символы:{even_chars}")
print(f"Четные символы:{odd_chars}")
reversed_text = (f"{original_text[::-1]}")
print(f"Текст с измененным порядком символов:{reversed_text}")
middle_index = len(original_text)//2
swapped_text = original_text[middle_index:] + original_text[:middle_index]
print(f"Текст с заменой местами левой и правой части:{swapped_text}")