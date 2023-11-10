# Matplotlib

matplotlib，python 绘图库，可以用于辅助我们进行数据分析。大致内容如下：

- 基本概念
  - `Figure` 画布
  - `Axes` 画布上的图形
- 主要内容

1. [matplotlib 图表组成元素](./chatper01/index.ipynb)

   - `scatter()`，**点**，用来寻找变量之间的相关性
   - `plot()`，**线**，用来展现变量的趋势变化
   - `legend()` 添加不同图形的文本标签**图例**
   - `title()` 添加图形内容的**标题**
   - `text()` 添加**注释文本**，用于描述图形内容细节
   - `annotate()` 添加**带箭头的注释文本**，用于描述图形内容细节
   - `xlim() & ylim()` 设置**坐标轴数值显示范围**
   - `xlabel() & ylabel()` 设置**坐标轴标签文本**
   - `axhline() & axvline()` 绘制**参考线**（horizontal 水平线 & vertical 垂直线）
   - `axhspan() & axvspan()` 绘制**参考区间**（horizontal 水平区间 & vertical 垂直区间）

2. matplotlib 图形
   - `arrow 箭头`(./chatper02/arrow.ipynb)
   - `polygon 多边形`(./chatper02/polygon.ipynb)
   - 统计图形
     - `bar 柱状图`(./chatper02/bar.ipynb)
3. matplotlib 坐标轴
4. matplotlib 配置
   1. [如何在图形中支持中文字符？](./chatper04/chinese.ipynb)

想要了解更多的话，请移步[matplotlib 官网](https://matplotlib.org/stable/tutorials/introductory/quick_start.html)
