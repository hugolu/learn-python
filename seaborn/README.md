# Seaborn: statistical data visualization

Official site: http://seaborn.pydata.org/

```
import seaborn as sns
```

## [控制图片外观](http://seaborn.pydata.org/tutorial/aesthetics.html)

函数 | 说明
---|---
[`sns.set_style()`](http://seaborn.pydata.org/generated/seaborn.set_style.html#seaborn.set_style) | Set the aesthetic style of the plots.（底图颜色）
[`sns.axes_style()`](http://seaborn.pydata.org/generated/seaborn.axes_style.html#seaborn.axes_style)| Return a parameter dict for the aesthetic style of the plots.
[`sns.despine()`](http://seaborn.pydata.org/generated/seaborn.despine.html#seaborn.despine) | Remove the top and right spines from plot(s).
[`sns.set_context()`](http://seaborn.pydata.org/generated/seaborn.set_context.html#seaborn.set_context) | Set the plotting context parameters.（图片尺寸）
[`sns.plotting_context()`](http://seaborn.pydata.org/generated/seaborn.plotting_context.html#seaborn.plotting_context) | Return a parameter dict to scale elements of the figure.

```
# 显示风格设定
sns.axes_style()

# 设定风格
sns.set_style("darkgrid", {"axes.facecolor": ".9"})
```

```
# 显示情景设定
sns.plotting_context()

# 设定情景
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
```

## [选择调色板](http://seaborn.pydata.org/tutorial/color_palettes.html)

调色系统 | 说明
---|---
Qualitative | 类别调色板 - 用来区别无次序性的离散数据
Sequential | 序列调色板 - 用来显示数据分布从相对低点到高点的变化、或从不感兴趣到感兴趣的变化
Diverging | 分叉调色板 - 用来显示数据分布从相对低点到高点，并包含中间值的变化，例如温度

函数 | 说明
---|---
[`seaborn.palplot()`](http://seaborn.pydata.org/generated/seaborn.palplot.html?highlight=palplot#seaborn.palplot) | Plot the values in a color palette as a horizontal array.
[`seaborn.color_palette()`](http://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette) | Return a list of colors defining a color palette.
[`seaborn.hls_palette()`](http://seaborn.pydata.org/generated/seaborn.hls_palette.html#seaborn.hls_palette) | Get a set of evenly spaced colors in HLS hue space.
[`seaborn.xkcd_palette`](http://seaborn.pydata.org/generated/seaborn.xkcd_palette.html#seaborn.xkcd_palette) | Make a palette with color names from the xkcd color survey.
[`seaborn.cubehelix_palette()`](http://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html#seaborn.cubehelix_palette) | Make a sequential palette from the cubehelix system.
[`seaborn.light_palette()`](http://seaborn.pydata.org/generated/seaborn.light_palette.html#seaborn.light_palette) | Make a sequential palette that blends from light to color.
[`seaborn.dark_palette()`](http://seaborn.pydata.org/generated/seaborn.dark_palette.html#seaborn.dark_palette) | Make a sequential palette that blends from dark to color.
[`seaborn.diverging_palette()`](http://seaborn.pydata.org/generated/seaborn.diverging_palette.html#seaborn.diverging_palette) | Make a diverging palette between two HUSL colors.
[`seaborn.set_palette()`](http://seaborn.pydata.org/generated/seaborn.set_palette.html#seaborn.set_palette) | Set the matplotlib color cycle using a seaborn palette.

## [离散数据可视化](http://seaborn.pydata.org/tutorial/distributions.html)

函数 | 说明
---|---
[`seaborn.distplot()`](http://seaborn.pydata.org/generated/seaborn.distplot.html#seaborn.distplot) | Flexibly plot a univariate distribution of observations.
[`seaborn.kdeplot()`](http://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot) | Fit and plot a univariate or bivariate kernel density estimate.
[`seaborn.rugplot`](http://seaborn.pydata.org/generated/seaborn.rugplot.html#seaborn.rugplot) | Plot datapoints in an array as sticks on an axis.
[`seaborn.jointplot()`](http://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot) | Draw a plot of two variables with bivariate and univariate graphs. (Scatter, Hexbin, KDE)
[`seaborn.pairplot()`](http://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn.pairplot) | Plot pairwise relationships in a dataset.
