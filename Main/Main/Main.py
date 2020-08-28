# to do list
import tkinter as tk

todo_list = []

font = 'berlin_sans_fb'

# Functions

# exits the program, should also log what was completed and save what still needs to be done
def escape():
    main_window.destroy()










#GUI
main_window = tk.Tk(); main_window.title('To Do List'); main_window.geometry('150x300')


t_frame = tk.Frame(master = main_window); t_frame.grid(row = 0, column = 0, pady = 10)

top_label = tk.Label(master = t_frame, text = 'To Do', font = font, width = 17); top_label.grid(row = 0, column = 0)



m_frame = tk.Label(master = main_window); m_frame.grid(row = 1, column = 0, pady = 10)

placeholder = tk.Label(master = m_frame, text = 'PLACEHOLDER'); placeholder.grid(row = 0, column = 0)



b_frame = tk.Label(master = main_window); b_frame.grid(row = 2, column = 0, pady = 10)

escape = tk.Button(master = b_frame, text = 'Escape', font = font, command = escape) ;escape.grid(row = 0, column = 1, sticky = 'WE')

add_button = tk.Button(master = b_frame, text = 'Add', font = font, ); add_button.grid(row = 0, column = 0)



while True:
    main_window.update()
    main_window.update_idletasks()