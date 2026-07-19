# 数学建模 完整测试代码（.py 文件 100% 能跑）
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 生成数据
x = np.linspace(1, 3, 100)
y = np.piecewise(x, [x <= 2, x > 2],
                [lambda x: 4 + 1*(x-1),
                 lambda x: 5 - 4*(x-2)])

# 数据统计
df = pd.DataFrame({'x': x, 'y': y})
print("数据基本统计：")
print(df.describe())

# 线性拟合（上升段）
from scipy.stats import linregress
x_rise = x[x <= 2]
y_rise = y[x <= 2]
slope, intercept, r_value, p_value, std_err = linregress(x_rise, y_rise)
print(f"上升段拟合结果：y = {slope:.2f}x + {intercept:.2f}")
print(f"拟合优度 R² = {r_value**2:.4f}")

# ✅ 画图（关键！你之前缺了这个！）
plt.figure(figsize=(8, 5))
plt.plot(x, y, linewidth=3, label="分段函数")
plt.grid(True)
plt.legend()
plt.title("数学建模绘图测试")
plt.show()  # 必须加！弹出图片
