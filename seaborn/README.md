# Seaborn: statistical data visualization

- Official site: http://seaborn.pydata.org/
- API: http://seaborn.pydata.org/api.html

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
[`seaborn.jointplot()`](http://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot) | Draw a plot of two variables with bivariate and univariate graphs. (Scatter, Hexbin, KDE, Regression)
[`seaborn.pairplot()`](http://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn.pairplot) | Plot pairwise relationships in a dataset.

```
import seaborn as sns; sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")
g = sns.pairplot(iris, hue="species"))
```
![](http://seaborn.pydata.org/_images/seaborn-pairplot-2.png)

## [线性关系可视化](http://seaborn.pydata.org/tutorial/regression.html)

函数 | 说明
---|---
[`seaborn.regplot()`](http://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot) | Plot data and a linear regression model fit.
[`seaborn.lmplot()`](http://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot) | Plot data and regression model fits across a FacetGrid.
[`seaborn.residplot()`](http://seaborn.pydata.org/generated/seaborn.residplot.html#seaborn.residplot) | Plot the residuals of a linear regression.

## [分类数据可视化](http://seaborn.pydata.org/tutorial/categorical.html)

函数 | 说明
---|---
[`seaborn.stripplot()`](http://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot) | Draw a scatterplot where one variable is categorical.
[`seaborn.swarmplot()`](http://seaborn.pydata.org/generated/seaborn.swarmplot.html#seaborn.swarmplot) | Draw a categorical scatterplot with non-overlapping points.
[`seaborn.boxplot()`](http://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot) | Draw a box plot to show distributions with respect to categories.
[`seaborn.violinplot()`](http://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot) | Draw a combination of boxplot and kernel density estimate.
[`seaborn.barplot()`](http://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn.barplot) | Show point estimates and confidence intervals as rectangular bars.
[`seaborn.pointplot()`](http://seaborn.pydata.org/generated/seaborn.pointplot.html#seaborn.pointplot) | Show point estimates and confidence intervals using scatter plot glyphs.
[`seaborn.factorplot()`](http://seaborn.pydata.org/generated/seaborn.factorplot.html#seaborn.factorplot) | Draw a categorical plot onto a FacetGrid.

## [格状子图](http://seaborn.pydata.org/tutorial/axis_grids.html)

函数 | 说明
---|---
[`seaborn.FacetGrid()`](http://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid) | Subplot grid for plotting conditional relationships.
[`seaborn.PairGrid()`](http://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid) | Subplot grid for plotting pairwise relationships in a dataset.

```
g = sns.FacetGrid(tips, col="sex", hue="smoker")
g.map(plt.scatter, "total_bill", "tip", alpha=.7)
g.add_legend();
```
![](http://seaborn.pydata.org/_images/axis_grids_12_0.png)

```
g = sns.PairGrid(iris)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot, cmap="Blues_d")
g.map_diag(sns.kdeplot, lw=3, legend=False);
```
![](http://seaborn.pydata.org/_images/axis_grids_50_0.png)
