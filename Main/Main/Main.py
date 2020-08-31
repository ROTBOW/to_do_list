# to do list
import tkinter as tk
from functools import partial
import time, os, sys

prog_loca = os.path.join(sys.path[0])

todo_list = list()

font = 'berlin_sans_fb'

# Functions

# exits the program, should also log what was completed and save what still needs to be done
def escape():
    ts = time.gmtime()
    prog_loca = os.path.join(sys.path[0])
    prog_loca = prog_loca[:-10]
    prog_loca = prog_loca + '/logs/'
    print(prog_loca)
    # this will be a loop that list the tasks complete and the tasks yet to complete
    with open(prog_loca + str(time.strftime('%Y-%m-%d', ts) + '.txt'), 'w+') as file:
        pass

    main_window.destroy()

def check_list_num():
    return(len(todo_list))

# to be run at the start of the program
# Will pull up the tasks that have yet to be completed
def update_tasks():
    num_tasks = str(check_list_num())
    for i in range(num_tasks):
        task = 'task_' + i
        todo_list.append(tk.Checkbutton(m_frame,))
        todo_list[-1].grid(row = i, column = 0)


# called on by the "add" button, will allow the user to add a task
def add_tasks():
    num_tasks = str(check_list_num())

    def check_chn():
        t_frame.destroy()
        temp_get.destroy()
        yes_info.destroy()
        no_info.destroy()

    def get_info():
        var1 = tk.IntVar()
        infor = temp_get.get()
        t_frame.destroy(); temp_get.destroy(); yes_info.destroy(); no_info.destroy()
        todo_list.append(tk.Checkbutton(m_frame, text = f'{infor}', font = font, variable = var1))
        todo_list[-1].grid(row = int(num_tasks), column = 0)
        
    t_frame = tk.Frame(m_frame); t_frame.grid(row = int(num_tasks), column = 0)
    temp_get = tk.Entry(t_frame, width = 10); temp_get.grid(row = 0, column = 0)
    yes_info = tk.Button(t_frame, text = '✓', command = get_info); yes_info.grid(row = 0, column = 1)
    no_info = tk.Button(t_frame, text = '✕', command = check_chn ); no_info.grid(row = 0, column = 2)

    



# GUI
main_window = tk.Tk(); main_window.title('To Do List'); main_window.geometry('150x300')


t_frame = tk.Frame(master = main_window); t_frame.pack(fill = tk.BOTH)
#t_frame = tk.Frame(master = main_window); t_frame.grid(row = 0, column = 0, pady = 10)

top_label = tk.Label(master = t_frame, text = 'To Do', font = font, width = 17); top_label.grid(row = 0, column = 0)



m_frame = tk.Label(master = main_window); m_frame.pack(fill = tk.BOTH)
#m_frame = tk.Label(master = main_window); m_frame.grid(row = 1, column = 0, pady = 10)



b_frame = tk.Label(master = main_window); b_frame.pack(side = 'bottom', fill = tk.BOTH)
#b_frame = tk.Label(master = main_window); b_frame.grid(row = 2, column = 0, pady = 10, sticky = 'S')

escape = tk.Button(master = b_frame, text = 'Escape', font = font, command = escape); escape.grid(row = 0, column = 1, sticky = 'WE')

add_button = tk.Button(master = b_frame, text = 'Add', font = font, command = add_tasks); add_button.grid(row = 0, column = 0)



while True:
    main_window.update()
    main_window.update_idletasks()