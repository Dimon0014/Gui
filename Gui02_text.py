import wx

class MyFrame(wx.Frame):

 def __init__(self):
               wx.Frame.__init__(self, None, -1, "My Frame", size=(350, 300))
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
               self.text1 = wx.TextCtrl(panel, -1, "Dockable",size = (330,150), style=wx.NO_BORDER | wx.TE_MULTILINE)

               hbox2.Add(self.text1, 1, wx.EXPAND| wx.ALIGN_LEFT | wx.ALL, 5)
               self.text1.Bind(wx.EVT_MOTION, self.OnMove)
               vbox.Add(hbox2)
               # wx.StaticText(panel, -1, "Pos:", pos=(10, 12))
               # self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(40, 10))
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