import functions
import PySimpleGUI as sg

sg.theme('DefaultNoMoreNagging')
label = sg.Text('Enter a To-Do', font=('Karma', 20))
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add', font='Karma, 14')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                     enable_events=True, size=[45, 10])

edit_button = sg.Button('Edit', font='Karma, 15')

window = sg.Window('To-Do App', layout=[[label], [input_box, add_button],
                                        [list_box], [edit_button]],
                                        font=('Karma', 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
