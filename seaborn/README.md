# Seaborn: statistical data visualization

Official site: http://seaborn.pydata.org/

```
import seaborn as sns
```

## 控制图片外观

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

## 选择调色板

函数 | 说明
---|---
`seaborn.color_palette()` | 设定调色板，返回定义的颜色
`seaborn.set_palette()` | 使用 seaborn 调色板当做 matplotlib 的颜色

