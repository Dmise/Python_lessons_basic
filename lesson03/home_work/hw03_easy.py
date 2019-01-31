# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number_str = str(number)
    fraction_str = number_str.split('.')[1]
    fraction_list = list(map(lambda x: int(x), fraction_str))
    whole_part_str = number_str.split('.')[0]
    whole_part_int = int(whole_part_str)
    counter = ndigits
    if fraction_list[counter] > 5:
        fraction_list[counter - 1] += 1
    while counter > 0:
        if fraction_list[counter-1] == 10:
            fraction_list[counter-1] = 0
            if counter == 1:
                whole_part_int += 1
            else:
                fraction_list[counter - 2] += 1
        counter -= 1

    final_value = str(whole_part_int) + '.'
    counter2 = 0
    while counter2 < ndigits:
        final_value = final_value + str(fraction_list[counter2])
        counter2 += 1

    return float(final_value)

print("Задание 1.  Без использования встроенных функций, нарисуйте костыли.... Я нарисовал, я молодец. Но мне не понравилось это задание")
print(my_round(2.1234567, 3))
print(my_round(2.1999967, 1))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number_str = str(ticket_number)
    if len(ticket_number_str) != 6:
        return False
    summ1 = int(ticket_number_str[0]) + int(ticket_number_str[1]) + int(ticket_number_str[2])
    summ2 = int(ticket_number_str[3]) + int(ticket_number_str[4]) + int(ticket_number_str[5])
    if summ1 == summ2:
        return True
    else:
        return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
