import wx
import time
from amcp_pylib.module.template import CG_ADD, CG_PLAY, CG_STOP, CG_CLEAR
import json
from casparlibs import Connector

class MainFrame(wx.Frame):
    """
    Main application frame
    """

    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)
        self.Bind(wx.EVT_CLOSE, self.onClose, self)

        self._pnlMain = wx.Panel(self)

        szLabel = wx.Size(100, 20)
        stText1 = wx.StaticText(self._pnlMain, label="Text 1", style=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, size=szLabel)

        szrText1 = wx.BoxSizer(wx.HORIZONTAL)
        szrText1.Add(stText1, wx.SizerFlags().Border(wx.LEFT, 10))
        
        szText = wx.Size(300, 20)
        self._txtText1 = wx.TextCtrl(self._pnlMain, size=szText)
        szrText1.Add(self._txtText1, wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 10))


        szLabel = wx.Size(100, 20)
        stText2 = wx.StaticText(self._pnlMain, label="Text 2", style=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, size=szLabel)

        szrText2 = wx.BoxSizer(wx.HORIZONTAL)
        szrText2.Add(stText2, wx.SizerFlags().Border(wx.LEFT, 10))
        
        szText = wx.Size(300, 20)
        self._txtText2 = wx.TextCtrl(self._pnlMain, size=szText)
        szrText2.Add(self._txtText2, wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 10))


        stLabel = wx.StaticText(self._pnlMain, label="Lower Third", style=wx.ALIGN_CENTER, size=wx.Size(400, 50))
        font = stLabel.GetFont()
        font.PointSize += 10
        font = font.Bold()
        stLabel.SetFont(font)


        szButton = wx.Size(100, 100)
        btnLoad1 = wx.Button(self._pnlMain, label="Show 1", size=szButton)
        self.Bind(wx.EVT_BUTTON, self.onShow1, btnLoad1)

        szButton = wx.Size(100, 100)
        btnLoad2 = wx.Button(self._pnlMain, label="Show 2", size=szButton)
        self.Bind(wx.EVT_BUTTON, self.onShow2, btnLoad2)


        szrButtons = wx.BoxSizer(wx.HORIZONTAL)
        szrButtons.Add(btnLoad1, wx.SizerFlags().Border(wx.LEFT, 10))
        szrButtons.Add(btnLoad2, wx.SizerFlags().Border(wx.LEFT, 10))

        szrMain = wx.BoxSizer(wx.VERTICAL)
        szrMain.Add(stLabel, wx.SizerFlags().Border(wx.TOP, 20))
        szrMain.Add(szrText1, wx.SizerFlags().Border(wx.TOP, 10))
        szrMain.Add(szrText2, wx.SizerFlags().Border(wx.TOP, 10))
        szrMain.Add(szrButtons, wx.SizerFlags().Border(wx.TOP, 10))
        self._client = Connector.getConnector()
        self._pnlMain.SetSizerAndFit(szrMain)

    def onShow1(self, event):
        self._show(self._txtText1.GetLineText(0))

    def onShow2(self, event):
        self._show(self._txtText2.GetLineText(0))
    
    def _show(self, text):
        jsn = json.dumps({'f0': text})
        response = self._client.send(CG_ADD(video_channel=1, layer=21, cg_layer=21, template="UBSMS/LOWERTHIRD", play_on_load=1, data=jsn))
        time.sleep(7)
        response = self._client.send(CG_STOP(video_channel=1, layer=21, cg_layer=21))
    
    def onClose(self, event):
        self.Destroy()

class DataLabel():
    def __init__(self, parent, width=200, height=40, label="Label:", data="data"):
        szLabel = wx.Size(100, height)

        self._stLabel = wx.StaticText(parent, label=label, style=wx.ALIGN_RIGHT, size=szLabel)
        font = self._stLabel.GetFont()
        font.PointSize += 10
        font = font.Bold()
        self._stLabel.SetFont(font)

        szData = wx.Size(300, height)

        self._stData = wx.StaticText(parent, label=data, size=szData)
        font = self._stData.GetFont()
        font.PointSize += 10
        self._stData.SetFont(font)

        self._szrMain = wx.BoxSizer(wx.HORIZONTAL)

        self._szrMain.Add(self._stLabel)
        self._szrMain.Add(self._stData, wx.SizerFlags().Border(wx.LEFT, 10))
        
    def getBoxSizer(self):
        return self._szrMain
    
    def setLabel(self, label):
        self._stLabel.SetLabel(label)

    def setData(self, label):
        self._stData.SetLabel(label)