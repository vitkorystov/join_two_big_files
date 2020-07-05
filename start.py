import in_place
# используем библиотеку in_place
# https://pypi.org/project/in-place/
# для удобной работы с заменой строк, вместо стандартной fileinput


file1 = 'file1.txt'  # файл с уникальными ключами
file2 = 'file2.txt'  # файл с множеством повторяющихся ключей
file_merged = 'merged.txt'  # результат слияния


# обработка файла file2
def process_file2(key):
    result = []  # добавляем в этот список все найденные значения по заданному ключу 'key'
    with in_place.InPlace(file2) as file_2:
        for line_f2 in file_2:
            # ключ
            key_f2 = line_f2.split('-')[0]
            # значение
            value_f2 = line_f2.split('-')[1]
            if key_f2 == key:
                result.append(value_f2.replace('\n', ''))
                # строка из file2 удаляется. Это сократит время выполнения последующих запросов
                # т.о. постепенно file2 будет уменьшаться, пока в нем не останутся ключи,
                # которых нет в file1
                file_2.write('')
            else:
                file_2.write(line_f2)
    return result


# в один проход по файлу file1 и сразу записываем результат в file_merged
with open(file1) as file_1:
    with in_place.InPlace(file_merged) as f_merged:
        for i, line_f1 in enumerate(file_1):
            key_f1 = line_f1.split('-')[0]
            res = process_file2(key_f1)
            # формируем финальную строку с ключом и значениями
            if res:
                new_line_f1 = line_f1.replace('\n', '') + ',' + ','.join(res)+'\n'
                f_merged.write(new_line_f1)
