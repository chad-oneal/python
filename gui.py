import functions
import PySimpleGUI as simple

label = simple.Text('Enter a To-Do')
input_box = simple.InputText(tooltip='Enter todo')
add_button = simple.Button('Add')


window = simple.Window('To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()


