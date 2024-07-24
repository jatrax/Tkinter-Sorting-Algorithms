from tkinter import *
from tkinter import ttk
import random

SIZE = 150
PIXEL_SIZE = 8
SELECTED_FUNCTION = 0
array = [i for i in range(SIZE)]

def swap(a,b):
    array[a], array[b] = array[b], array[a]

def update_UI():
    canvas.delete('all')
    draw()
    app.update_idletasks()

def shuffle():
    for i in range(SIZE):
        swap(i,random.randint(0,SIZE-1))
        update_UI()

def bubble_sort():
    for i in range(len(array)-1):
        update_UI()
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                swap(j,j+1)

def cocktail_sort():
    n = len(array)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        update_UI()
        swapped = False
        for i in range(start, end):
            if array[i] > array[i + 1]:
                swap(i, i + 1)
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end, start - 1, -1):
            if array[i] > array[i + 1]:
                swap(i, i + 1)
                swapped = True
        start += 1    


def selection_sort():
    for i in range(len(array)):
        update_UI()
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            swap(i, min_index)

def insertion_sort():
    for i in range(1, len(array)):
        update_UI()
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        update_UI()

def quick_sort(low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low < high:
        pivot_index = partition(low, high)
        quick_sort(low, pivot_index - 1)
        quick_sort(pivot_index + 1, high)

def partition(low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            swap(i, j)
            update_UI()
    swap(i + 1, high)
    update_UI()
    return i + 1

def heap_sort():
    def heapify(n, i):
        update_UI()
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and array[l] > array[largest]:
            largest = l
        if r < n and array[r] > array[largest]:
            largest = r
        if largest != i:
            swap(i, largest)
            heapify(n, largest)
    
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        swap(0, i)
        heapify(i, 0)

def radix_sort():
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1
        
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        
        for i in range(n):
            update_UI()
            arr[i] = output[i]
    
    max1 = max(array)
    exp = 1
    while max1 // exp > 0:
        counting_sort(array, exp)
        update_UI()
        exp *= 10
        
def shell_sort():
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            update_UI()
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    update_UI()
       
def counting_sort():
    if len(array) == 0:
        return

    max_val = max(array)
    min_val = min(array)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(array)

    for num in array:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(array) - 1, -1, -1):
        output[count[array[i] - min_val] - 1] = array[i]
        count[array[i] - min_val] -= 1

    for i in range(len(array)):
        array[i] = output[i]
        update_UI()

functions      = [ bubble_sort , cocktail_sort , selection_sort , insertion_sort , quick_sort , heap_sort , radix_sort , shell_sort , counting_sort]
function_names = ['bubble_sort','cocktail_sort','selection_sort','insertion_sort','quick_sort','heap_sort','radix_sort','shell_sort','counting_sort']

bg = "#1c1c1c"

app = Tk()  
app.config(background=bg)
canvas = Canvas(app,width=SIZE*PIXEL_SIZE,height=SIZE*PIXEL_SIZE,background=bg)
canvas.pack()

def startCommand():
    try:SELECTED_FUNCTION = function_names.index(chc.selection_get())
    except:SELECTED_FUNCTION = 0
    functions[SELECTED_FUNCTION]()
    update_UI()

def shuffleCommand():
    shuffle()
    update_UI()

bottom_bar = Frame(app,background=bg)
chc = ttk.Combobox(bottom_bar, values=function_names)
chc.grid(column=0, row=0, padx=5, pady=5)
chc.current(0)

startButton = Button(bottom_bar, command=startCommand, text="SORT")
startButton.grid(column=1, row=0, padx=5, pady=5)

shuffleButton = Button(bottom_bar, command=shuffleCommand, text="SHUFFLE")
shuffleButton.grid(column=2, row=0, padx=5, pady=5)

bottom_bar.pack()
color = 'white'
def draw():
    for x in range(len(array)):
        color = "#"+str(int(array[x]/SIZE*9))+str(int(array[x]/SIZE*9))+'77'+str(9-int(array[x]/SIZE*9))+str(9-int(array[x]/SIZE*9))
        canvas.create_oval(x*PIXEL_SIZE, SIZE*PIXEL_SIZE - array[x]*PIXEL_SIZE, x*PIXEL_SIZE + PIXEL_SIZE, SIZE*PIXEL_SIZE - array[x]*PIXEL_SIZE -PIXEL_SIZE, fill=color)

shuffle()
draw()

app.mainloop()