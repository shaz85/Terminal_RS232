import tkinter as tk
from tkinter import ttk

from tkinter import scrolledtext


win = tk.Tk()
win.title("Termnial")



top_row_frame = ttk.LabelFrame(win)
top_row_frame.grid(column =0 , row = 0, padx = 2, pady = 2, sticky = 'E')
frame_top_left_1 = ttk.LabelFrame(top_row_frame)
frame_top_left_1.grid(column =0 , row = 0, padx = 2, pady = 2)

ttk.Button(frame_top_left_1, text = 'Conenect').grid(column = 0, row = 1)
ttk.Button(frame_top_left_1, text = 'Rescan').grid(column = 0 , row = 2)
#ttk.Button(frame_top_left_1, text = 'Help').grid(column = 0, row = 3)
ttk.Button(frame_top_left_1, text = 'About').grid(column = 0, row = 4)
ttk.Button(frame_top_left_1, text = 'Quit').grid(column = 0, row = 5)
for child in frame_top_left_1.winfo_children(): 
    child.grid_configure(padx=1, pady=1)



frame_top_left_2 = ttk.LabelFrame(top_row_frame, text = 'COM Port')
frame_top_left_2.grid(column =1 , row = 0, padx = 2, pady = 2, sticky = 'N' + 'S')

baud_rate_lable = ttk.Label(frame_top_left_2, text = 'Select Port')
baud_rate_lable.grid(column =0 , row = 0, padx = 2, pady = 2 )

number_choosen = ttk.Combobox(frame_top_left_2, width = 12 , state = 'readonly')
number_choosen['values'] = (600, 1200, 2400, 4800, 9600, 19200, 28800, 38400, 56000, 57600, 115200, 128000, 256000)
number_choosen.grid(column = 0, row = 1, sticky = tk.E)
number_choosen.current()


baud_rate_lable = ttk.Label(frame_top_left_2, text = 'Baudrate')
baud_rate_lable.grid(column =0 , row = 2, padx = 2, pady = 2 )

baud_rate = ttk.Combobox(frame_top_left_2, width = 12 , state = 'readonly')
baud_rate['values'] = (600, 1200, 2400, 4800, 9600, 19200, 28800, 38400, 56000, 57600, 115200, 128000, 256000)
baud_rate.grid(column = 0, row = 3, sticky = tk.E)
baud_rate.current(4)

for child in frame_top_left_2.winfo_children(): 
    child.grid_configure(padx=2, pady=2)


# Data bits frame

frame_top_left_data_bits = ttk.LabelFrame(top_row_frame, text = ' Data bits')
frame_top_left_data_bits.grid(column = 3 , row = 0, padx = 2, pady = 2, sticky = 'N' + 'S')

ttk.Radiobutton(frame_top_left_data_bits, text='5' ).grid(column = 0, row = 0)
ttk.Radiobutton(frame_top_left_data_bits, text='6' ).grid(column = 0, row = 1)
ttk.Radiobutton(frame_top_left_data_bits, text='7' ).grid(column = 0, row = 2)

ttk.Radiobutton(frame_top_left_data_bits, text='8' ).grid(column = 0, row = 3)

for child in frame_top_left_data_bits.winfo_children(): 
    child.grid_configure(padx=2, pady=2)

# Parity bits
frame_top_left_pairity_bits = ttk.LabelFrame(top_row_frame, text = ' Parity')
frame_top_left_pairity_bits.grid(column = 4 , row = 0, padx = 2, pady = 2, sticky = 'N' + 'S')

ttk.Radiobutton(frame_top_left_pairity_bits, text='none' ).grid(column = 0, row = 0, sticky='W')
ttk.Radiobutton(frame_top_left_pairity_bits, text='odd' ).grid(column = 0, row = 1, sticky='W')
ttk.Radiobutton(frame_top_left_pairity_bits, text='even' ).grid(column = 0, row = 2, sticky='W')

ttk.Radiobutton(frame_top_left_pairity_bits, text='space' ).grid(column = 0, row = 3, sticky='W')

for child in frame_top_left_pairity_bits.winfo_children(): 
    child.grid_configure(padx=2, pady=2)

# stop bits
frame_top_left_stop_bits = ttk.LabelFrame(top_row_frame, text = ' Stop bits')
frame_top_left_stop_bits.grid(column = 5 , row = 0, padx = 2, pady = 2, sticky = 'N' + 'S')

ttk.Radiobutton(frame_top_left_stop_bits, text='1' ).grid(column = 0, row = 0, sticky='W')
ttk.Radiobutton(frame_top_left_stop_bits, text='1.5' ).grid(column = 0, row = 2, sticky='W')
ttk.Radiobutton(frame_top_left_stop_bits, text='2' ).grid(column = 0, row = 5, sticky='W')



for child in frame_top_left_stop_bits.winfo_children(): 
    child.grid_configure(padx=2, pady=2)

# HandShaking
frame_top_left_hand_shaking = ttk.LabelFrame(top_row_frame, text = ' HandShaking')
frame_top_left_hand_shaking.grid(column = 5 , row = 0, padx = 2, pady = 2, sticky = 'N' + 'S')

ttk.Radiobutton(frame_top_left_hand_shaking, text='none' ).grid(column = 0, row = 0, sticky='W')
ttk.Radiobutton(frame_top_left_hand_shaking, text='RTS/CTS' ).grid(column = 0, row = 1, sticky='W')
ttk.Radiobutton(frame_top_left_hand_shaking, text='XON/XOFF' ).grid(column = 0, row = 2, sticky='W')


for child in frame_top_left_hand_shaking.winfo_children(): 
    child.grid_configure(padx=2, pady=2)


'''
labelsFrame = ttk.LabelFrame(win, text=' Labels in a Frame ')
labelsFrame.grid(column=0, row=7, padx=20, pady=40)
 
# Place labels into the container element - vertically
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)
'''




second_row_frame = ttk.LabelFrame(top_row_frame, text ='Settings')
second_row_frame.grid(column =6 , row = 0, padx = 2, pady = 2, sticky = 'W' + 'E' +'N' + 'S')

ttk.Button(second_row_frame, text = 'Font', width = 12).grid(column = 0, row = 0 , sticky ='N' + 'S' )
tk.Checkbutton(second_row_frame, text="Time").grid(column = 1, row = 0, sticky = 'W')
tk.Checkbutton(second_row_frame, text="CR=LF").grid(column = 1, row = 1, sticky = 'W')

tk.Checkbutton(second_row_frame, text="Start log").grid(column = 2, row = 0, sticky = 'W')



for child in second_row_frame.winfo_children(): 
    child.grid_configure(padx=4, pady=4)


#text1.pack(side=LEFT)

third_row_text = ttk.LabelFrame(top_row_frame, text ='Read text')
third_row_text.grid(column =0 , row = 2, padx = 2, pady = 2, sticky = 'W' + 'E' +'N' + 'S')
tk.Text(third_row_text, text = 'Font', width = 12).grid(column = 0, row = 0 , sticky ='N' + 'S' )

win.mainloop()



'''

Exit or quit functionality implemented time 54.30 to 55.20
file menu also on 53
creating tabs 56.55
'''