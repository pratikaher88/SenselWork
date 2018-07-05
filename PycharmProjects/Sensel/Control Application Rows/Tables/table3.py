import matplotlib
matplotlib.use('WXAgg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from matplotlib.offsetbox import AnnotationBbox,OffsetImage
from PIL import Image
import wx


from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
class Canvas(wx.Panel):
    def __init__(self,parent):
            wx.Panel.__init__(self, parent)
            self.fig=plt.figure()
            self.ax = plt.axes(projection=ccrs.PlateCarree())
            self.ax.coastlines()
            self.ax.stock_img()
            self.canvas = FigureCanvas(self, -1, self.fig)

            self.gl = self.ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                              linewidth=2, color='gray', alpha=15, linestyle='--')
            self.gl.xlabels_top = False
            self.gl.ylabels_left = False
            self.gl.xlines = False
            self.gl.xlocator = mticker.FixedLocator([-180, -45, 0, 45, 180])
            self.gl.xformatter = LONGITUDE_FORMATTER
            self.gl.yformatter = LATITUDE_FORMATTER
            self.gl.xlabel_style = {'size': 15, 'color': 'gray'}
            self.gl.xlabel_style = {'color': 'red', 'weight': 'bold'}
            self.sizer = wx.BoxSizer(wx.VERTICAL)
            self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
            self.SetSizer(self.sizer)
            self.Fit()
    def draw(self):
            img=Image.open(r'E:\python_file\untitled\p.png')
            imagebox=OffsetImage(img,zoom=0.05)
            imagebox.image.axes=self.ax
            ab=AnnotationBbox(imagebox,[55,10],pad=0,frameon=False)
            self.ax.add_artist(ab)



if __name__ == "__main__":
    app = wx.App()
    fr=wx.Frame(None,title='test')
    panel=Canvas(fr)
    print('fine')
    panel.draw()
    fr.Show()
    print('just')
    app.MainLoop()
