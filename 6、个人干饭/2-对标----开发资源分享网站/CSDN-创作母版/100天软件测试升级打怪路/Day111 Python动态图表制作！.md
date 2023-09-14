# Day111 Python动态图表制作！



# 让数据“动”起来：Python动态图表制作！



*原文链接：https://towardsdatascience.com/learn-how-to-create-animated-graphs-in-python-fce780421afe*



在读技术博客的过程中，我们会发现那些能够把知识、成果讲透的博主很多都会做动态图表。他们的图是怎么做的？难度大吗？这篇文章就介绍了 Python 中一种简单的动态图表制作方法。



![图片](images/640.gif)



数据暴增的年代，数据科学家、分析师在被要求对数据有更深的理解与分析的同时，还需要将结果有效地传递给他人。如何让目标听众更直观地理解？当然是将数据可视化啊，而且最好是动态可视化。



**本文将以线型图、条形图和饼图为例，系统地讲解如何让你的数据图表动起来**。



![图片](images/640-169450270410214.gif)



**这些动态图表是用什么做的？**



接触过数据可视化的同学应该对 Python 里的 Matplotlib 库并不陌生。它是一个基于 Python 的开源数据绘图包，仅需几行代码就可以帮助开发者生成直方图、功率谱、条形图、散点图等。这个库里有个非常实用的扩展包——FuncAnimation，可以让我们的静态图表动起来。



FuncAnimation 是 Matplotlib 库中 Animation 类的一部分，后续会展示多个示例。如果是首次接触，你可以将这个函数简单地理解为一个 While 循环，不停地在 “画布” 上重新绘制目标数据图。



**如何使用 FuncAnimation？**



这个过程始于以下两行代码：



```
import matplotlib.animation as ani

animator = ani.FuncAnimation(fig, chartfunc, interval = 100)
```



从中我们可以看到 FuncAnimation 的几个输入：



- fig 是用来 「绘制图表」的 figure 对象；
- chartfunc 是一个以数字为输入的函数，其含义为时间序列上的时间；
- interval 这个更好理解，是帧之间的间隔延迟，以毫秒为单位，默认值为 200。



这是三个关键输入，当然还有更多可选输入，感兴趣的读者可查看原文档，这里不再赘述。



下一步要做的就是将数据图表参数化，从而转换为一个函数，然后将该函数时间序列中的点作为输入，设置完成后就可以正式开始了。



在开始之前依旧需要确认你是否对基本的数据可视化有所了解。也就是说，我们先要将数据进行可视化处理，再进行动态处理。



按照以下代码进行基本调用。另外，这里将采用大型流行病的传播数据作为案例数据（包括每天的死亡人数）。



```
import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import pandas as pdurl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
df = pd.read_csv(url, delimiter=',', header='infer')df_interest = df.loc[
    df['Country/Region'].isin(['United Kingdom', 'US', 'Italy', 'Germany'])
    & df['Province/State'].isna()]df_interest.rename(
    index=lambda x: df_interest.at[x, 'Country/Region'], inplace=True)
df1 = df_interest.transpose()df1 = df1.drop(['Province/State', 'Country/Region', 'Lat', 'Long'])
df1 = df1.loc[(df1 != 0).any(1)]
df1.index = pd.to_datetime(df1.index)
```



**绘制三种常见动态图表**



**动态曲线图**

**
**

![图片](images/640-169450267929012.gif)



如下所示，首先需要做的第一件事是定义图的各项，这些基础项设定之后就会保持不变。它们包括：创建 figure 对象，x 标和 y 标，设置线条颜色和 figure 边距等：



```
import numpy as np
import matplotlib.pyplot as pltcolor = ['red', 'green', 'blue', 'orange']
fig = plt.figure()
plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values
plt.subplots_adjust(bottom = 0.2, top = 0.9) #ensuring the dates (on the x-axis) fit in the screen
plt.ylabel('No of Deaths')
plt.xlabel('Dates')
```



接下来设置 curve 函数，进而使用 .FuncAnimation 让它动起来：



```
def buildmebarchart(i=int):
    plt.legend(df1.columns)
    p = plt.plot(df1[:i].index, df1[:i].values) #note it only returns the dataset, up to the point i
    for i in range(0,4):
        p[i].set_color(color[i]) #set the colour of each curveimport matplotlib.animation as ani
animator = ani.FuncAnimation(fig, buildmebarchart, interval = 100)
plt.show()
```



**动态饼状图**

**
**

![图片](images/640-169450266296310.gif)



可以观察到，其代码结构看起来与线型图并无太大差异，但依旧有细小的差别。



```
import numpy as np
import matplotlib.pyplot as pltfig,ax = plt.subplots()
explode=[0.01,0.01,0.01,0.01] #pop out each slice from the piedef getmepie(i):
    def absolute_value(val): #turn % back to a number
        a  = np.round(val/100.*df1.head(i).max().sum(), 0)
        return int(a)
    ax.clear()
    plot = df1.head(i).max().plot.pie(y=df1.columns,autopct=absolute_value, label='',explode = explode, shadow = True)
    plot.set_title('Total Number of Deaths\n' + str(df1.index[min( i, len(df1.index)-1 )].strftime('%y-%m-%d')), fontsize=12)import matplotlib.animation as ani
animator = ani.FuncAnimation(fig, getmepie, interval = 200)
plt.show()
```



主要区别在于，动态饼状图的代码每次循环都会返回一组数值，但在线型图中返回的是我们所在点之前的整个时间序列。返回时间序列通过 df1.head(i) 来实现，而. max()则保证了我们仅获得最新的数据，因为流行病导致死亡的总数只有两种变化：维持现有数量或持续上升。



```
df1.head(i).max()
```



**动态条形图**

![图片](images/640-16945026514668.gif)



![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)



创建动态条形图的难度与上述两个案例并无太大差别。在这个案例中，作者定义了水平和垂直两种条形图，读者可以根据自己的实际需求来选择图表类型并定义变量栏。



```
fig = plt.figure()
bar = ''def buildmebarchart(i=int):
    iv = min(i, len(df1.index)-1) #the loop iterates an extra one time, which causes the dataframes to go out of bounds. This was the easiest (most lazy) way to solve this :)
    objects = df1.max().index
    y_pos = np.arange(len(objects))
    performance = df1.iloc[[iv]].values.tolist()[0]
    if bar == 'vertical':
        plt.bar(y_pos, performance, align='center', color=['red', 'green', 'blue', 'orange'])
        plt.xticks(y_pos, objects)
        plt.ylabel('Deaths')
        plt.xlabel('Countries')
        plt.title('Deaths per Country \n' + str(df1.index[iv].strftime('%y-%m-%d')))
    else:
        plt.barh(y_pos, performance, align='center', color=['red', 'green', 'blue', 'orange'])
        plt.yticks(y_pos, objects)
        plt.xlabel('Deaths')
        plt.ylabel('Countries')animator = ani.FuncAnimation(fig, buildmebarchart, interval=100)plt.show()
```



**保存动画图**



在制作完成后，存储这些动态图就非常简单了，可直接使用以下代码：



```
animator.save(r'C:\temp\myfirstAnimation.gif')
```



感兴趣的读者如想获得详细信息可参考https://matplotlib.org/3.1.1/api/animation_api.html。

官网：

https://matplotlib.org/3.1.1/api/animation_api.html。