# Классы: Список дел (To-Do List)

## Классы

| Класс | Атрибуты | Методы | Назначение |
|---|---|---|---|
| Task | title: str, deadline: str, done: bool | mark_done(), __str__() | Одно дело: название, срок и статус. Название проверяется в конструкторе. |
| TaskManager | tasks: list[Task] | add_task(), remove_task(), mark_done(), get_all(), get_pending(), count(), find_by_title() | Управление списком дел. |
| TaskStorage | filename: str | load(), save() | Чтение и запись списка в файл (будет реализован позже). |
| ConsoleUI | manager: TaskManager | run(), print_menu(), add_flow(), mark_flow(), remove_flow(), show_all(), show_pending(), search_flow() | Меню, ввод и вывод в консоли. |

## Связи
- ConsoleUI → TaskManager: ассоциация. Интерфейс хранит ссылку на менеджера (поле manager) и обращается к нему.
- TaskManager ◇— Task: агрегация, один менеджер содержит много дел (1 к 0..*).
- TaskManager ┄> TaskStorage: зависимость (пунктир). Менеджер использует хранилище при загрузке и сохранении, но не владеет им.
- TaskStorage не связана с ConsoleUI: зависимость идёт только вниз (интерфейс → логика → хранение).

## Соответствие коду
Классы Task, TaskManager (logic.py) и ConsoleUI (ui.py) реализованы и совпадают с диаграммой по именам, параметрам и результатам методов. TaskStorage будет реализован в следующих лабораторных работах. Если код меняется, диаграмму нужно обновить (и наоборот).

## Наследование хранилищ (задел на будущее)
На диаграмме class_diagram_storage.puml класс TaskStorage становится базовым классом Storage с методами load() и save(). От него наследуются FileStorage (хранение в файле, поле filename) и MemoryStorage (хранение в памяти, поле data). TaskManager зависит только от Storage, поэтому способ хранения можно переключить, не меняя менеджер и интерфейс.
