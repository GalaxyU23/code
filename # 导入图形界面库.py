# 范佩阳_2024020805 电气工程及其自动化1班
import tkinter as tk #制作窗口
from tkinter import messagebox #错误提示
def calculate():
    try:
        num1 = float(entry1.get())#获取读数
        num2 = float(entry2.get())
        op = var_op.get() #获取运算符号
        res = 0#结果暂存
        if op == "+":
            res = num1 + num2
        elif op == "-":
            res = num1 - num2
        elif op == "*":
            res = num1 * num2
        elif op == "/":
            if num2 == 0:
                messagebox.showerror("运算错误", "除数不能为0！")
                return
            res = num1 / num2
        label_result.config(text=f"计算结果：{res}")

    except ValueError:
        messagebox.showerror("输入错误", "请输入有效的数字！")
root = tk.Tk()#建立主窗口
root.title("简易四则计算器范佩阳_202402080505")#设置标题
root.geometry("420x220")#窗口像素大小
var_op = tk.StringVar()#获取运算
var_op.set("+")#默认加
tk.Label(root, text="第一个数字：", font=("Arial", 11)).place(x=40, y=30)#标签+输入框
entry1 = tk.Entry(root, width=20, font=("Arial", 11))
entry1.place(x=140, y=30)
tk.Label(root, text="第二个数字：", font=("Arial", 11)).place(x=40, y=70)
entry2 = tk.Entry(root, width=20, font=("Arial", 11))
entry2.place(x=140, y=70)
tk.Label(root, text="选择运算：", font=("Arial", 11)).place(x=40, y=110)
tk.Radiobutton(root, text="加法 +", variable=var_op, value="+").place(x=140, y=110)#运算符号按钮 单选按钮
tk.Radiobutton(root, text="减法 -", variable=var_op, value="-").place(x=220, y=110)
tk.Radiobutton(root, text="乘法 ×", variable=var_op, value="*").place(x=300, y=110)
tk.Radiobutton(root, text="除法 ÷", variable=var_op, value="/").place(x=370, y=110)
btn_calc = tk.Button(root, text="开始计算", command=calculate,
                     width=12, height=1, font=("Arial", 11))
btn_calc.place(x=160, y=150)#开始计算按钮 command=calculate 表示点击按钮就执行 calculate 函数
label_result = tk.Label(root, text="计算结果：", font=("Arial", 12), fg="blue")#结果按钮
label_result.place(x=40, y=190)
root.mainloop()#窗口主循环