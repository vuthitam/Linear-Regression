#!/usr/bin/env python
# coding: utf-8

# # Bài tập vẽ đồ thị với Python sử dụng thư viện Matplotlib, Numpy
# ## Đề bài:
# Cho đồ thị hàm số $y= \dfrac{1}{4} x^3 - \dfrac{3}{2} x^2 +5$
# 1. Khảo sát sự biến thiên, vẽ đồ thị đã cho
# 2. Tìm giá trị của m để phương trình $x^3 - 6 x^2 +m = 0$ có 3 nghiệm phân biệt.
# 

# ## Bài làm
# 1. Vẽ đồ thị \
# Đầu tiên ta sử dụng thư viện hỗ trợ vẽ đồ thị trong Python nên cần import chúng vào

# In[50]:


import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# Sau đó tạo hàm khởi tạo hàm số $y= \dfrac{1}{4} x^3 - \dfrac{3}{2} x^2 +5$

# In[51]:


def f(x):
    return 1/4*x**3 - 3/2*x**2 + 5
#Make data
x_1 =np.linspace(start= -20, stop= 20, num=500)
x_1


# In[52]:


plt.figure(figsize=[15, 10])
plt.xlim(-5, 10)
plt.ylim(-20, 20)
plt.xlabel('X', fontsize=16)
plt.ylabel('f(X)', fontsize=16)
plt.plot(x_1, f(x_1))
plt.grid()
plt.show()


# # Vẽ đồ thị trong Matplotlib
# ## 1. Ví dụ về phân cấp đối tượng trong Matplotlib

# In[53]:


# This figure shows the name of several matplotlib elements composing a figure

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter


np.random.seed(19680801)

X = np.linspace(0.5, 3.5, 100)
Y1 = 3+np.cos(X)
Y2 = 1+np.cos(1+X/0.75)/2
Y3 = np.random.uniform(Y1, Y2, len(X))

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, aspect=1)


def minor_tick(x, pos):
    if not x % 1.0:
        return ""
    return "%.2f" % x

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.25')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Blue signal", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Red signal")
ax.plot(X, Y3, linewidth=0,
        marker='o', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Anatomy of a figure", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("X axis label")
ax.set_ylabel("Y axis label")

ax.legend()


def circle(x, y, radius=0.15):
    from matplotlib.patches import Circle
    from matplotlib.patheffects import withStroke
    circle = Circle((x, y), radius, clip_on=False, zorder=10, linewidth=1,
                    edgecolor='black', facecolor=(0, 0, 0, .0125),
                    path_effects=[withStroke(linewidth=5, foreground='w')])
    ax.add_artist(circle)


def text(x, y, text):
    ax.text(x, y, text, backgroundcolor="white",
            ha='center', va='top', weight='bold', color='blue')


# Minor tick
circle(0.50, -0.10)
text(0.50, -0.32, "Minor tick label")

# Major tick
circle(-0.03, 4.00)
text(0.03, 3.80, "Major tick")

# Minor tick
circle(0.00, 3.50)
text(0.00, 3.30, "Minor tick")

# Major tick label
circle(-0.15, 3.00)
text(-0.15, 2.80, "Major tick label")

# X Label
circle(1.80, -0.27)
text(1.80, -0.45, "X axis label")

# Y Label
circle(-0.27, 1.80)
text(-0.27, 1.6, "Y axis label")

# Title
circle(1.60, 4.13)
text(1.60, 3.93, "Title")

# Blue plot
circle(1.75, 2.80)
text(1.75, 2.60, "Line\n(line plot)")

# Red plot
circle(1.20, 0.60)
text(1.20, 0.40, "Line\n(line plot)")

# Scatter plot
circle(3.20, 1.75)
text(3.20, 1.55, "Markers\n(scatter plot)")

# Grid
circle(3.00, 3.00)
text(3.00, 2.80, "Grid")

# Legend
circle(3.70, 3.80)
text(3.70, 3.60, "Legend")

# Axes
circle(0.5, 0.5)
text(0.5, 0.3, "Axes")

# Figure
circle(-0.3, 0.65)
text(-0.3, 0.45, "Figure")

color = 'blue'
ax.annotate('Spines', xy=(4.0, 0.35), xycoords='data',
            xytext=(3.3, 0.5), textcoords='data',
            weight='bold', color=color,
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color=color))

ax.annotate('', xy=(3.15, 0.0), xycoords='data',
            xytext=(3.45, 0.45), textcoords='data',
            weight='bold', color=color,
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color=color))

ax.text(4.0, -0.4, "Made with http://matplotlib.org",
        fontsize=10, ha="right", color='.5')

plt.show()


# ## 2. Vẽ nhiều tập điểm phân tán trên cùng đồ thị

# In[54]:


import matplotlib.pyplot as plt
plt.figure(figsize=[15,10])
plt.plot([1990,2000,2010,2015,2020], [1,2,3,4,10], 'go--', label='Python')
plt.plot([1990,2000,2010,2015,2020], [10,4,3,2,1], 'r*-', label='C#')
plt.plot([1990,2000,2010,2015,2020], [1,3,5,7,10], 'bo-', label='Java')
plt.title('Vẽ đồ thị trong Python với Matplotlib', fontsize=16)
plt.xlabel('Năm',fontsize=16)
plt.ylabel('Y', fontsize=16)
plt.legend()
plt.show()


# ## 3. Vẽ nhiều đồ thị trong cùng một ảnh

# In[55]:


fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(10,4), sharey=True, dpi=120)

ax1.plot([0,1,2,3,4], [1,2,3,4,10], 'go-')
ax2.plot([0,1,2,3,4], [10,4,3,2,1], 'ro-')
ax3.plot([2.5,2.5,2.5,1.5,0.5], [1,3,5,7,10], 'bo-')

# Title, X and Y labels, X and Y Lim
ax1.set_title('Python'); 
ax2.set_title('C#')
ax3.set_title('Java')

ax1.set_xlabel('X');  ax2.set_xlabel('X');  ax3.set_xlabel('X'); # x label
ax1.set_ylabel('Y');  ax2.set_ylabel('Y');  ax3.set_ylabel('Y')  # y label
ax1.set_xlim(0, 6) ;  ax2.set_xlim(0, 6) ;  ax3.set_xlim(0, 6)   # x axis limits
ax1.set_ylim(0, 12);  ax2.set_ylim(0, 12);  ax3.set_ylim(0, 12)  # y axis limits

# ax2.yaxis.set_ticks_position('none') 
plt.tight_layout()
plt.show()


# ## 4.  Vẽ tập hợp điểm phân tán với scatter()
# Sự khác biệt giữa plot() và scatter():
# - plot() không có khả năng thay đổi màu và kích thước điểm trong tập hợp điểm ban đầu nhưng scatter() lại có thể.
# - plot() có thể vẽ các đường nối hai điểm liên tiếp, scatter() thì không.

# In[56]:


height = np.array([167,170,149,165,155,180,166,146,159,185,145,168,172,181,169])
weight = np.array([86,74,66,78,68,79,90,73,70,88,66,84,67,84,77])

colors = np.random.rand(15)
area = (30 * np.random.rand(15))**2 
plt.figure(figsize=(15,9))
plt.xlim(140,200)
plt.ylim(60,100)
plt.scatter(height,weight,s=area,c=colors)
plt.title("Chiều cao và cân nặng")
plt.xlabel("Chiều cao - cm")
plt.ylabel("Cân nặng - kg")

plt.show()


# ## 5. Tạo đồ thị ảnh động với Animation

# In[59]:


import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, frames=200, interval=20, blit=True)
anim.save('sin_wave.gif', writer='imagemagick')


# ![](sin_wave.gif)

# ## Cách khác
# 

# In[60]:


import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, frames=200, interval=20, blit=True)
HTML(anim.to_html5_video())

