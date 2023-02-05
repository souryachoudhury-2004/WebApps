def getTodos():
    with open("todos.txt", "r") as file:
        todoList = file.readlines()
        return todoList


def writeTodos(todos_arg):
    with open("todos.txt", "w") as file:
        file.writelines(todos_arg)


