# Практическое задание №6. Системы автоматизации сборки

Работа с утилитой Make.

Изучить основы языка утилиты make. Распаковать в созданный каталог [make.zip](make.zip), если у вас в в системе нет make.

Создать приведенный ниже Makefile и проверить его работоспособность.

dress: trousers shoes jacket
    @echo "All done. Let's go outside!"

jacket: pullover
    @echo "Putting on jacket."

pullover: shirt
    @echo "Putting on pullover."

shirt:
    @echo "Putting on shirt."

trousers: underpants
    @echo "Putting on trousers."

underpants:
    @echo "Putting on underpants."

shoes: socks
    @echo "Putting on shoes."

socks: pullover
    @echo "Putting on socks."


Визуализировать файл [civgraph.txt](civgraph.txt).

## Задача 1

Написать программу на Питоне, которая транслирует граф зависимостей civgraph в makefile в духе примера выше. Для мало знакомых с Питоном используется упрощенный вариант civgraph: [civgraph.json](civgraph.json).

Пример:

> make mathematics
mining
bronze_working
sailing
astrology
celestial_navigation
pottery
writing
code_of_laws
foreign_trade
currency
irrigation
masonry
early_empire
mysticism
drama_poetry
mathematics


## Решение:

import json

def parse_civgraph(civgraph_file):
    # Чтение JSON-файла
    with open(civgraph_file, 'r') as file:
        data = json.load(file)

    return data

def generate_makefile(data, output_file):
    with open(output_file, 'w') as file:
        for target, dependencies in data.items():
            # Формируем правило для Makefile
            dep_str = " ".join(dependencies) if dependencies else ""
            file.write(f"{target}: {dep_str}\n")
            file.write(f"\t@echo {target}\n\n")  # Простое действие для примера

def main():
    civgraph_file = "civgraph.json"  # Имя файла с графом зависимостей
    output_file = "Makefile"  # Имя итогового Makefile

    # Чтение данных из civgraph.json
    data = parse_civgraph(civgraph_file)

    # Генерация Makefile
    generate_makefile(data, output_file)
    print(f"Makefile был сгенерирован в {output_file}")

if __name__ == "__main__":
    main()


## Результат:

![image](https://github.com/user-attachments/assets/21070e62-e08a-4838-8556-5768d234efdd)

## Задача 2

Реализовать вариант трансляции, при котором повторный запуск make не выводит для civgraph на экран уже выполненные "задачи".

## Решение:

```Python
import json
import os

# Файл для сохранения завершенных задач
TASKS_FILE = "my_task2.txt"

# Загрузка списка завершенных задач из файла
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return set(f.read().splitlines())
    return set()

# Сохранение завершенных задач в файл
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        f.write('\n'.join(tasks))

# Загрузка графа зависимостей из JSON-файла
def load_dependency_graph(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Ошибка при загрузке файла {filename}: {e}")
        return {}

# Функция генерации Makefile с проверкой на уже выполненные задачи
def generate_makefile(dependency_graph, target_task):
    visited_tasks = set()
    tasks_to_process = []
    completed_tasks = load_tasks()

    def process_task(task):
        if task in visited_tasks or task in completed_tasks:
            return
        visited_tasks.add(task)
        for dependency in dependency_graph.get(task, []):
            process_task(dependency)
        tasks_to_process.append(task)

    process_task(target_task)

    if not tasks_to_process:
        print("Все задачи уже были выполнены.")
    else:
        for task in tasks_to_process:
            if task not in completed_tasks:
                print(f"{task}")
                completed_tasks.add(task)

        save_tasks(completed_tasks)

if name == 'main':
    # Загружаем граф з
