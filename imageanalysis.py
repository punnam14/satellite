#!/usr/bin/env python
# coding: utf-8

# In[40]:


import rasterio


# In[ ]:





# In[41]:


dataset = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B093_L1T.tif')


# In[42]:


dataset.count


# In[43]:


dataset.width


# In[44]:


dataset.height


# In[45]:


{i: dtype for i, dtype in zip(dataset.indexes, dataset.dtypes)}


# In[46]:


dataset.bounds


# In[47]:


dataset.transform


# In[48]:


dataset.transform * (0, 0)


# In[49]:


dataset.indexes


# In[50]:


dataset.xy(dataset.height // 2, dataset.width // 2)


# In[51]:


dataset.colorinterp[0]


# In[52]:


import rasterio
from matplotlib import pyplot
src = rasterio.open("C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B093_L1T.tif")
pyplot.imshow(src.read(1), cmap='pink')


# In[53]:


from rasterio.plot import show
show(dataset)
show(dataset.read(), transform=dataset.transform)


# In[54]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B093_L1T.tif')
xoff, yoff = 500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset)


# In[55]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B092_L1T.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset)


# In[56]:


src.tags()


# In[57]:


src.tags(ns='IMAGE_STRUCTURE')


# In[58]:


src.tags(ns='SUBDATASETS')


# In[59]:


src.tags(ns='RPC')


# In[60]:


import rasterio
from matplotlib import pyplot
src = rasterio.open("C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B093_L1T.tif")
pyplot.imshow(src.read(1), cmap='summer')


# In[61]:


import rasterio
from matplotlib import pyplot
src = rasterio.open("C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B092_L1T.tif")
pyplot.imshow(src.read(1), cmap='hsv')


# In[62]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B092_L1T.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='seismic')


# In[63]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B092_L1T.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='hsv')


# In[64]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B093_L1T.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='hsv')


# In[ ]:





# In[65]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B092_L1T.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='Accent')


# In[66]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B093_L1T.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='Accent')


# In[67]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B092_L1T.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='tab20b')


# In[68]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B093_L1T.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='tab20b')


# In[69]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B092_L1T.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='Paired')


# In[70]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B093_L1T.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='Paired')


# In[71]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B092_L1T.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[72]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B093_L1T.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[73]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B002_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[74]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B094_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[75]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B227_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[76]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B241_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[77]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B231_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[78]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B224_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[79]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B217_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[80]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B217_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[81]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B203_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[82]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B189_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[83]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B168_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[84]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B154_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[85]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B140_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[86]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B119_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[87]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B098_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[88]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B077_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[89]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B056_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[90]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B035_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[91]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B021_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[92]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B007_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[93]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B229_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[94]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B201_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[95]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B152_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[97]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B093_L1T.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='plasma')


# In[106]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B030_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[109]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B014_L1GST.tif')
xoff, yoff =500, 500
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[110]:


from rasterio.windows import Window
src = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H1480472016328110PZ_1GST\\EO1H1480472016328110PZ\\EO1H1480472016328110PZ_B050_L1GST.tif')
xoff, yoff =500, 500;/
xsize, ysize = 600, 600
subset = src.read(1, window=Window(xoff, yoff, xsize, ysize))
show(subset,cmap='brg')


# In[122]:


import rasterio
from matplotlib import pyplot
src = rasterio.open("C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B092_L1T.tif")
pyplot.imshow(src.read(1), cmap='seismic')


# In[128]:


src.indexes


# In[130]:


dataset = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B092_L1T.tif')


# In[141]:


dataset.width


# In[145]:


dataset.height


# In[148]:


band1 = dataset.read(1)


# In[174]:


img = band1[0:200,900:1191]


# In[175]:


pyplot.imshow(img)


# In[178]:


img = band1[200:300,900:1000]


# In[179]:


pyplot.imshow(img)


# In[180]:


img = band1[10:200,900:1191]
pyplot.imshow(img)


# In[240]:


img = band1[5:80,925:1025]
pyplot.imshow(img,cmap='plasma')


# #### band1.shape

# In[140]:


band1.dtype


# In[133]:


x, y = (dataset.bounds.left + 100000, dataset.bounds.top - 50000)


# In[134]:


row, col = dataset.index(x, y)


# In[135]:


row, col


# In[136]:


band1[row, col]


# In[241]:


from matplotlib import pyplot, image, transforms
dataset = rasterio.open('C:\\Users\\Punnam Satpathy\\Desktop\\satellite data\\EO1H0350252010205110KU_1T\\EO1H0350252010205110KU_B092_L1T.tif')
#img = image.imread('filename.png')

pyplot.ion()
fig = pyplot.figure()
ax = fig.add_subplot(111)

for degree in range(360):
    pyplot.clf()
    tr = transforms.Affine2D().rotate_deg(degree)

    ax.imshow(dataset, transform=tr)
    fig.canvas.draw()


# In[ ]:




