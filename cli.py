import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print('It is', now)

while True:
    user_action = input("Type add, show, edit, or complete for a to-do, or type exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos_list=todos, )

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.capitalize()
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos_list=todos)

        except ValueError:
            print("Your command is not recognized")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos_list=todos)
            message = f"Todo {todo_to_remove} has been removed from the list"
            print(message)

        except IndexError:
            print("'I'm sorry, I do not see an item with that number, please enter the correct #")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("This command is not recognized")

print("Have a great day!")





