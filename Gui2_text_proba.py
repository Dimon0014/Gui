import wx


class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(350, 250))
############################### ПЕРВЫЙ ЭТАП
        panel = wx.Panel(self) # панель для размещения всего
#############################  ВТОРОЙ ЭТАП
        vbox = wx.BoxSizer(wx.VERTICAL) #нулевой бокс сайзер в нем разместяца все остальные сайзеры
############################# ТРЕТИЙ ЭТАП
        hbox1 = wx.BoxSizer(wx.HORIZONTAL) # первый бокс сайзер(горизонтальный (элементы в нем как строка))
        # один за другим будут
        l1 = wx.StaticText(panel, -1, "Text Field") # создаем первый элемент

        hbox1.Add(l1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5) # добавляем первый элемент в первый
                                            #  бокс сайзер (первый элемент в строке)
                                                      #
        self.t1 = wx.TextCtrl(panel) # создаем второй элемент с именем доступным для членов класса

        hbox1.Add(self.t1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5) # # добавляем второй элемент в
                                                # первый  бокс сайзер (второй элемент в строке)
        self.t1.Bind(wx.EVT_TEXT, self.OnKeyTyped) # связываем окно(второй элемент с обработчиком события)
        vbox.Add(hbox1) # добавляем первый бокс сайзер в нулевой
########################################################################################
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        l2 = wx.StaticText(panel, -1, "password field")

        hbox2.Add(l2, 1, wx.ALIGN_LEFT | wx.ALL, 5)
        self.t2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        self.t2.SetMaxLength(5)

        hbox2.Add(self.t2, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox2)
        self.t2.Bind(wx.EVT_TEXT_MAXLEN, self.OnMaxLen)
######################################################################################
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        l3 = wx.StaticText(panel, -1, "Multiline Text")

        hbox3.Add(l3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t3 = wx.TextCtrl(panel, size=(200, 100), style=wx.TE_MULTILINE)

        hbox3.Add(self.t3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox3)
        self.t3.Bind(wx.EVT_TEXT_ENTER, self.OnEnterPressed)
#####################################################################################
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        l4 = wx.StaticText(panel, -1, "Read only text")

        hbox4.Add(l4, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t4 = wx.TextCtrl(panel, value="ReadOnlyText",style = wx.TE_READONLY|wx.TE_CENTER)

        hbox4.Add(self.t4, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox4)
############################### ЗАКЛЮЧИТЕЛЬНЫЙ ЭТАП
        panel.SetSizer(vbox)

        self.Centre()
        self.Show()
        self.Fit()

    def OnKeyTyped(self, event):
        print
        event.GetString()

    def OnEnterPressed(self, event):
        print
        "Enter pressed"

    def OnMaxLen(self, event):
        print
        "Maximum length reached"


app = wx.App()
Mywin(None, 'TextCtrl demo')
app.MainLoop()