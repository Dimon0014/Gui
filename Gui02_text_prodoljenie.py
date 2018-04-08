import wx

class MyFrame(wx.Frame):

 def __init__(self):
               wx.Frame.__init__(self, None, -1, "My Frame", size=(500, 600))
               panel = wx.Panel(self, -1)
               vbox = wx.BoxSizer(wx.VERTICAL)

               hbox1 = wx.BoxSizer(wx.HORIZONTAL)
               l1 = wx.StaticText(panel, -1, "Text Field")
               hbox1.Add(l1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

               self.t1 = wx.TextCtrl(panel)

               hbox1.Add(self.t1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
               # self.t1.Bind(wx.EVT_TEXT, self.OnKeyTyped)
               vbox.Add(hbox1)

               hbox2 = wx.BoxSizer(wx.HORIZONTAL)
               self.text1 = wx.TextCtrl(panel, -1, "Dockable",size = (480,450), style=wx.NO_BORDER | wx.TE_MULTILINE)

               hbox2.Add(self.text1, 1, wx.EXPAND| wx.ALIGN_LEFT | wx.ALL, 5)
               self.text1.Bind(wx.EVT_MOTION, self.OnMove)
               vbox.Add(hbox2)
               # wx.StaticText(panel, -1, "Pos:", pos=(10, 12))
               # self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(40, 10))
               hbox3 = wx.BoxSizer(wx.HORIZONTAL)
               self.btn0 = wx.Button(panel, label="-0-")
               self.btn1 = wx.Button(panel, label="-1-")
               self.btn2 = wx.Button(panel, label="-2-")
               self.btn3 = wx.Button(panel, label="-3-")
               hbox3.Add(self.btn0, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 15)
               hbox3.Add(self.btn1, 1, wx.EXPAND| wx.ALIGN_LEFT  | wx.ALL, 15)
               hbox3.Add(self.btn2, 1, wx.EXPAND| wx.ALIGN_LEFT| wx.ALL, 15)
               hbox3.Add(self.btn3, 1, wx.EXPAND| wx.ALIGN_LEFT  | wx.ALL, 15)

               vbox.Add(hbox3)
               panel.SetSizer(vbox)
               self.Centre()
               self.Show()
               self.Fit()
 def OnMove(self, event):
              pos = event.GetPosition()
              self.text1.SetValue("%s, %s" % (pos.x, pos.y))
              # self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))

if __name__ == '__main__':
           app = wx.App() # OLD style -> wx.PySimpleApp()
           frame = MyFrame()
           frame.Show(True)
           app.MainLoop(

           )