import tkinter as tk


def grid_update():
    global lines, grid
    lines = [grid[i:i+3] for i in range(0, 9, 3)]\
        + [[grid[i+j] for i in range(0, 9, 3)] for j in range(3)]\
        + [[grid[i] for i in range(2, 7, 2)], [grid[i] for i in range(0, 9, 4)]]

def click(i):
    global turn, grid
    buttons[i].config(text=["x", "o"][turn % 2], state='disabled', relief=tk.SUNKEN)
    grid[i] = ["x", "o"][turn % 2]
    l1.config(text = f'it\'s {["x", "o"][(turn + 1) % 2]}\'s turn')
    grid_update()
    turn += 1
    if any(map(lambda line: all(map(lambda cell: cell == 'o', line)) or\
               all(map(lambda cell: cell == 'x', line)), lines)):
        l1.config(text = f'{["x", "o"][(turn + 1) % 2]} won!')
        for button in buttons:
            button.config(state='disabled')      
        
    elif all(map(lambda x: x != '0', ''.join([''.join(map(str, line)) for line in lines]))):
        l1.config(text = f'draw! again?')

def generate():
    global grid, turn, buttons
    turn = 0
    buttons = []
    for buttonid in range(9):
        b = tk.Button(f1, text = "*", command = lambda name=buttonid: click(name))
        b.config(height = 1, width = 3, relief=tk.GROOVE)
        b.grid(row=buttonid // 3, column=buttonid % 3)  
        buttons.append(b)
    l1.config(text=f'it\'s {["x", "o"][(turn) % 2]}\'s turn')    
    grid = [0 for _ in range(9)]
turn = 0
grid = [0 for _ in range(9)]
lines = [grid[i:i+3] for i in range(0, 9, 3)]\
    + [[grid[i+j] for i in range(0, 9, 3)] for j in range(3)]\
    + [[grid[i] for i in range(2, 7, 2)], [grid[i] for i in range(0, 9, 4)]]
    
root = tk.Tk()
root.geometry('480x320')
root.title('TicTacToe')
container = tk.Frame(root, background="bisque")
container.pack(fill="both", expand=True)
l1 = tk.Label(container, text='it\'s TTT', background="bisque")
l1.pack(side=tk.TOP, pady=10)
f1 = tk.Frame(container, background = "bisque", borderwidth = 5)
f1.pack(side=tk.LEFT, padx=50)
f2 = tk.Frame(container, background = "bisque", borderwidth = 5)
f2.pack(side=tk.LEFT, padx=10)
l1 = tk.Label(f2, text=f'it\'s {["x", "o"][(turn) % 2]}\'s turn', background="bisque", borderwidth = 25)
l1.pack(side=tk.TOP)
restart = tk.Button(f2, text='restart', command = generate)
restart.pack(side=tk.LEFT)
close = tk.Button(f2, text='quit', command = root.destroy)
close.pack(side=tk.RIGHT)
generate()
root.mainloop()
