# Seaborn: statistical data visualization

Official site: http://seaborn.pydata.org/

```
import seaborn as sns
```

## [控制图片外观](http://seaborn.pydata.org/tutorial/aesthetics.html)

函数 | 说明
---|---
`sns.set_style()` | 设定图片风格 （底图颜色）
`sns.axes_style()` | 返回图片风格参数字典
`sns.despine()` | 移除图片上面、右边的外框
`sns.set_context()` | 设定绘画情景 （图片尺寸）
`sns.plotting_context()` | 返回绘图情景参数字典


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

函数 | 说明
---|---
[`seaborn.palplot()`](http://seaborn.pydata.org/generated/seaborn.palplot.html?highlight=palplot#seaborn.palplot) | Plot the values in a color palette as a horizontal array.
[`seaborn.color_palette()`](http://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette) | Return a list of colors defining a color palette.
[`seaborn.cubehelix_palette()`](http://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html#seaborn.cubehelix_palette) | Make a sequential palette from the cubehelix system.
[`seaborn.light_palette()`](http://seaborn.pydata.org/generated/seaborn.light_palette.html#seaborn.light_palette) | Make a sequential palette that blends from light to color.
[`seaborn.dark_palette()`](http://seaborn.pydata.org/generated/seaborn.dark_palette.html#seaborn.dark_palette) | Make a sequential palette that blends from dark to color.
[`seaborn.set_palette()`](http://seaborn.pydata.org/generated/seaborn.set_palette.html#seaborn.set_palette) | Set the matplotlib color cycle using a seaborn palette.