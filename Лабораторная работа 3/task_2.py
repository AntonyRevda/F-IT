# TODO Напишите функцию find_common_participants
def find_common_participants(first_, second_, separator = ','):
    first_usual = first_.split(separator)
    second_usual = second_.split(separator)
    intersection_list = list(set(first_usual).intersection(second_usual))
    intersection_list.sort()
    return intersection_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, ))


#Для того, чтобы код сработал c предложенными строками, необходимо прописать разделитель, стоящий в них
print(find_common_participants(participants_first_group, participants_second_group, '|'))