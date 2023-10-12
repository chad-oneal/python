import functions
import PySimpleGUI as sg

sg.theme('DefaultNoMoreNagging')
label = sg.Text('Enter a To-Do', font=('Karma', 20))
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add', font='Karma, 14')

window = sg.Window('To-Do App', layout=[[label], [input_box, add_button]],
                   font=('Karma', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break



window.close()
