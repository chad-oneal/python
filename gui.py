import functions
import PySimpleGUI as sg
import time

sg.theme('DefaultNoMoreNagging')
label = sg.Text('Enter a To-Do', font=('Karma', 20))
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add', font='Karma, 14')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))

edit_button = sg.Button('Edit', font='Karma, 15')
complete_button =sg.Button('Complete', font='Karma, 15')
clock = sg.Text('', key='clock', pad=((110,0),0))
exit_button = sg.Button('Exit', font='Karma, 15', pad=((140,0),0))
layout = [[label],
          [input_box, add_button],
          [list_box], [edit_button, complete_button, clock, exit_button]]

window = sg.Window('To-Do App',
                   layout=layout,
                   font=('Karma', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
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
            window['todo'].update(value='')

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select an item first', font=('Karma', 15))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select an item first', font=('Karma', 15))

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
