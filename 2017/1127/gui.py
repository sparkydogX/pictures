import tkinter as tk
from tkinter import messagebox

#调用chatbot核心交互模块，获得输出
def add_text(mw,st,imsg):
    message_send_by_bot=''
    message_send_by_human=''
    if(imsg.get().strip()==''):
        pass
    else:
        message_send_by_human='Human:\n\t'+imsg.get()+'\n'
        message_send_by_bot='ChatBot:\n\t'+'stupid\n'
        mw.config(state='normal')
        mw.insert('end',message_send_by_human)
        mw.insert('end',message_send_by_bot)
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')

#显示作者信息
def show_author():
    messagebox.showinfo("作者信息","xxx")

window = tk.Tk()
#input_message为消息框中的文字
input_message=tk.StringVar(window)
input_message.set("")
#输入回车键发送消息
window.bind('<Return>',lambda x:add_text(message_window,input_entry,input_message))
window.title('AI Chatbot')
window.geometry('600x600')
window['bg'] = 'white'
fram1 = tk.Frame(height=60, width=100, bg='white')
fram2 = tk.Frame(height=400, width=100, bg='blue')
fram3 = tk.Frame(height=80, width=100, bg='red')
#聊天机器人名字
bot_name = tk.Label(fram1,
                    text='ChatBot',

                    bg='white',
                    font=('Arial', 12),
                    width=15, height=2
                    )
bot_name.pack(side='left')
#作者信息button
about_button = tk.Button(fram1,
                         text='作者信息',
                         width=10, height=2,
                         relief='groove',
                         bg='white',
                         command=show_author)
about_button.pack(side='right')

#输入栏
input_entry=tk.Entry(fram3,width=10,
                     bg='white',textvariable=input_message)
input_entry.pack(side='left',expand='YES',fill='both')
#初始化消息框
message_window=tk.Text(fram2,bg='white',yscrollcommand='YES')
message_window.insert('end','ChatBot:\n\t'+'hello\n')
message_window.config(state='disabled')
message_window.pack(side='top',expand='YES',fill='both')
#发送按钮
send_button = tk.Button(fram3,text='发送(Enter)',
                        width=10,
                        height=2,
                        relief='groove',
                        bg='white',
                        state='active',
                        command=lambda :add_text(message_window,input_entry,input_message)
                        )
send_button.pack(side='right')

fram1.pack(fill='x', side='top')
fram2.pack(fill='both', expand='YES')
fram3.pack(fill='x', side='bottom')
window.mainloop()
