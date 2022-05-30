import re
import sys
import tkinter as tk
import tkinter.messagebox as msgbox

import you_get

"""
视频下载类
"""


class DownloadApp:  # 定义一个类，用于控制窗口的显示
    # 构建
    def __init__(self, width=400, height=100):  # 初始化
        self.w = width  # 宽
        self.h = height  # 高
        self.title = 'you-get--GUI'  # 标题
        self.root = tk.Tk(className=self.title)  # 创建窗口
        self.root.iconbitmap('D:\Project\Pycharm\dl\you-get\GUI\logo.ico')   # 设置图标
        self.root.config(bg='#E6E6FA')  # 设置背景颜色
        self.url = tk.StringVar()  # 视频地址
        self.start = tk.IntVar()  # 开始位置
        self.end = tk.IntVar()  # 结束位置
        self.path = tk.StringVar()  # 输出地址
        self.path.set(r"D:\xasu\视频\bilibili")  # 输出地址

        # 定义框架
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        # 设置 frame_1
        label1 = tk.Label(frame_1, text='输入视频链接：')
        entry_url = tk.Entry(frame_1, textvariable=self.url, highlightthickness=1, width=35)

        # 设置 frame_2
        label2 = tk.Label(frame_2, text='视频输出地址：')  # 输出地址
        entry_path = tk.Entry(frame_2, textvariable=self.path, highlightthickness=1, width=35)  # 输出地址
        down = tk.Button(frame_2, text='下载', font=('楷体', 12), fg='green', width=6, height=-8,
                         command=self.video_download)  # 下载按钮

        # 布局
        frame_1.pack()
        #  设置 frame_1的颜色
        frame_1.config(bg='#E6E6FA')
        frame_2.pack()
        #  设置 frame_2的颜色
        frame_2.config(bg='#E6E6FA')

        label1.grid(row=0, column=0)  # 设置标签位置
        entry_url.grid(row=0, column=1)  # 设置输入框位置

        label2.grid(row=4, column=0)  # 设置标签位置
        entry_path.grid(row=4, column=1)  # 设置输入框位置
        #  设置按钮位置靠右
        down.grid(row=4, column=1, sticky=tk.E)

    """
    视频下载
    """

    def video_download(self):  # 视频下载
        # 正则表达是判定是否为合法链接
        url = self.url.get()  # 获取输入的视频链接
        path = self.path.get()  # 获取输入的输出地址
        if re.match(r'^https?:/{2}\w.+$', url):  # 判断是否为合法链接
            if path != '':  # 判断输出地址是否为空
                msgbox.showwarning(title='警告', message='下载过程中窗口如果出现短暂卡顿说明文件正在下载中！')  # 提示
                try:  # 尝试下载
                    sys.argv = ['you-get', '-o', path, url]  # 设置命令行参数
                    you_get.main()  # 调用下载函数
                except Exception as e:  # 如果下载失败
                    print(e)  # 打印错误信息
                    msgbox.showerror(title='error', message=e)  # 提示错误
                msgbox.showinfo(title='info', message='下载完成！')  # 提示
            else:  # 如果输出地址为空
                msgbox.showerror(title='error', message='输出地址错误！')  # 提示错误
        else:  # 如果输入的链接不合法
            msgbox.showerror(title='error', message='视频地址错误！')  # 提示错误

    def center(self):  # 居中
        ws = self.root.winfo_screenwidth()  # 获取屏幕宽度
        hs = self.root.winfo_screenheight()  # 获取屏幕高度
        x = int((ws / 2) - (self.w / 2))  # 计算x坐标
        y = int((hs / 2) - (self.h / 2))  # 计算y坐标
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))  # 设置窗口大小及坐标

    def event(self):  # 事件
        self.root.resizable(False, False)  # 禁止改变窗口大小
        self.center()  # 居中
        self.root.mainloop()  # 进入消息循环


if __name__ == '__main__':  # 判断是否为主程序
    app = DownloadApp()  # 实例化主程序
    app.event()  # 进入消息循环
