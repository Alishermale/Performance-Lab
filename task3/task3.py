import json


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def fill_values(tests, values_dict):
    for test in tests:
        test_id = test["id"]
        if "value" in test:
            test["value"] = values_dict.get(test_id, "")
        if "values" in test:
            fill_values(test["values"], values_dict)


values = input('Файл с наполнением результатов прохождения тестов: ')
tests = input('Файл с структурой для построения отчета на основе прошедших тестов: ')
result = input('Файл для сохрания результатов: ')

values_data = load_json(values)
tests_data = load_json(tests)

values_dict = {item["id"]: item["value"] for item in values_data["values"]}
fill_values(tests_data["tests"], values_dict)
save_json(result, tests_data)
