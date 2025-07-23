from tkinter import *    # tkinter 패키지의 모든 변수, 함수, 클래스를 가져옴


def clicked(digit):
    if digit == '<-':
        input_entry.delete(len(input_entry.get())-1)
    else:
        input_entry.insert(END, digit)


def del_digit():
    input_entry.delete(0, END)
    

def calculate():

    try:
        result = eval(input_entry.get())      # eval 함수는 매개변수로 받은 식을 문자열로 받아서, 실행하는 함수 입니다. 
    except:
        result_label.config(text='계산식 오류')
    else:
        result_label.config(text=result)


cal = Tk()
cal.title('계산기')

digits = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['<-','0','.','+']
]


input_entry = Entry(cal, width = 30, borderwidth=7, justify= 'right', fg='blue')
input_entry.grid(column=0, row=0, columnspan=4)     


result_label = Label(cal, text='result', width=20)
result_label.grid(column=0, row=1, columnspan=4, pady=15)

for r in range(4):
    for c in range(4):
        digit = digits[r][c]
        button = Button(cal, text=digit, width=8, height=5, command=lambda x=digit: clicked(x))
        button.grid(row=r+2, column=c)


clear_button = Button(cal, text='C', width=20, height=5, command=del_digit)
clear_button.grid(column=0, row=6, columnspan=2)

cal_button = Button(cal, text='=', width=20, height=5, command=calculate)
cal_button.grid(column=2, row=6, columnspan=2)


cal.mainloop()