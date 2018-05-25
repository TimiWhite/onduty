# -*- coding: UTF-8 -*-
import tkinter as tk
import time
import datetime
from future.moves.tkinter import ttk

__author__ = 'wangjinxin'

#2018-4-16初始列表
data = [["邢娜娜","张笑铜","董一俏","汪秀凤","劳燚玲"],
        ["杨洋","郑小芳","余勇","林宏燊","高国芳"],
        ["刘颖","倪明","彭春花","牛丽","陈丽"],
        ["蔡姣姣","王金鑫","张超","黄禄权","梁健培"],
        ["张超","张宏伟","张宏伟","黄子权","黄禄权"],
        ["杨振威","梁健培","黄子权","","杨振威"]]

class OnDutyTkinter():

    local_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))

    #计算两个日期相差天数，自定义函数名，和两个日期的变量名。
    def Caltime(date1,date2):
        #%Y-%m-%d为日期格式，其中的-可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
        #date1=time.strptime(date1,"%Y-%m-%d %H:%M:%S")
        #date2=time.strptime(date2,"%Y-%m-%d %H:%M:%S")
        date1=time.strptime(date1,"%Y-%m-%d")
        date2=time.strptime(date2,"%Y-%m-%d")
        #根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
        #date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
        #date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
        date1=datetime.datetime(date1[0],date1[1],date1[2])
        date2=datetime.datetime(date2[0],date2[1],date2[2])
        #返回两个变量相差的值，就是相差天数
        return date2-date1

    #计算过去多少周
    def passWeek(m_pass_data):
        pass_week = m_pass_data / 7
        return int(pass_week)

    pass_data = Caltime("2018-4-16",local_time).days
    pass_week = passWeek(pass_data)

    def __init__(self, m_data=data, m_pass_week=pass_week):

        root = tk.Tk()
        #设置窗口大小和位置
        root.geometry('520x300+800+300')
        #不允许改变窗口大小
        root.resizable(False, False)
        #设置窗口标题
        root.title("Who are on Duty ?")

        #使用Treeview组件实现表格功能
        self.frame = tk.Frame(root)
        self.frame.place(x=0, y=50, width=520, height=280)

        x = time.localtime(time.time())
        label = tk.Label(root,text = 'Today is '+ time.strftime("%A",x))
        label.pack()

        m_columns = ("a","b","c","d","e")
        tree=ttk.Treeview(self.frame,columns=m_columns,show="headings")

        for item in m_columns:
            tree.column(item,width=100,anchor='center')   #表示列,不显示

        tree.heading("a",text="Monday")  #显示表头
        tree.heading("b",text="Tuesday")
        tree.heading("c",text="Wednesday")
        tree.heading("d",text="Thursday")
        tree.heading("e",text="Friday")
        # tree.pack(side=Tkinter.LEFT, fill=Tkinter.Y)

        # 用过去多少周换算成员 对应初始列表中的下标位置，实际使用n需要再-1
        def pass_n(m_pass_week,n):
            n_p = n-m_pass_week+5*(int((n-m_pass_week)%5)+1)
            if n_p>5:
                return int((n_p)%5)
            else:
                return int(n_p)

            # if n-m_pass_week<=0:
            #
            #     return int((m_pass_week-n)%5)
            # else:
            #     return int(m_pass_week-n)

        for item in range(6):
            tree.insert("",item,values=(m_data[item][pass_n(m_pass_week,1)-1],
                                        m_data[item][pass_n(m_pass_week,2)-1],
                                        m_data[item][pass_n(m_pass_week,3)-1],
                                        m_data[item][pass_n(m_pass_week,4)-1],
                                        m_data[item][pass_n(m_pass_week,5)-1],
                                        m_data[item][pass_n(m_pass_week,6)-1],
                                        )) #插入数据

        tree.pack()
        root.mainloop()


if __name__ == '__main__':
    OnDutyTkinter()
