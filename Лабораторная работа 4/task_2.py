# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(csv_file: str, delimiter: str = ',') -> str:
    # TODO считать содержимое csv файла
    json_data = []

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=delimiter)

        for row in reader:
            json_data.append(row)

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as output_file:
        json.dump(json_data, output_file, indent=4)
    return json.dumps(json_data, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
