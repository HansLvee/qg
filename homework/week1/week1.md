# 第一周

## 作业目标

导入JSON并完成向量运算，将向量封装

## 相关数学公式

### 坐标轴投影长度

$\displaystyle Proj_\vec{a}\vec{v} = \frac{\vec{v} \cdot \vec{a}} {\|\vec{a}\|}$

### 向量夹角

$\displaystyle\cos\theta = \frac{\vec{v} \cdot \vec{a}} {\|\vec{v}\| \cdot \|\vec{a}\|}$

### 坐标系变换

$
\begin{align}
&对新坐标系，设基向量 \vec{v_1}, \vec{v_2}, \vec{v_3}... \\
&有基变换矩阵A= 
\begin{bmatrix}
\vec{v_1} \ 
\vec{v_1} \
\vec{v_1} \
... \\
\end{bmatrix} \\
&旧坐标V\rightarrow 新坐标V'：  V' = A^{-1} V \\
&新坐标V\rightarrow 旧坐标V \ ：V \ \ = AV' \\ \\
&以二维直角坐标系为例：\\
&对于向量：\vec{v} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}，
转移至新坐标系：\vec{x}= \begin{bmatrix} 1 \\ 0 \end{bmatrix}，
\vec{y}= \begin{bmatrix} 1 \\ 1 \end{bmatrix} \\
&设新坐标：\vec{v'} = \begin{bmatrix} a \\ b \end{bmatrix}，
由变换公式可建立方程：a \begin{bmatrix} 1 \\ 0 \end{bmatrix} + 
b \begin{bmatrix} 1 \\ 1 \end{bmatrix} =
\begin{bmatrix} 1 \\ 1 \end{bmatrix} \\
&合并：\begin{bmatrix} a+b \\ b \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \end{bmatrix} \\
&解得：\vec{v'} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
\end{align}
$

### 坐标系变换缩放倍数

$
\begin{align}
&设基变换矩阵A= 
\begin{bmatrix}
\vec{v_1} \ 
\vec{v_1} \
\vec{v_1} \
... \\
\end{bmatrix} \\
&则缩放倍数=|det A| \\
&当detA > 0时，坐标系方向不变；否则方向反向.
\end{align}
$

### 矩阵行列式

$
\begin{align}
&对于基变换矩阵，有如下性质 \\
&detA \neq 0 \Rightarrow 坐标系合法(线性无关) \\
&detA = 0 \Rightarrow 坐标系不合法(线性相关) \\
&detA > 0 \Rightarrow 右手坐标系 \\
&detA < 0 \Rightarrow 左手坐标系
\end{align}
$

## Python相关

### NumPy

| 函数/运算符   | 功能                            |
| :------------ | ------------------------------- |
| array()       | 列表转NumPy数组，可指定数据类型 |
| norm()        | 计算向量范数，默认二范数        |
| inv()         | 计算可逆方阵的逆矩阵            |
| det()         | 计算方阵的行列式                |
| dot()         | 计算矩阵/向量的点积             |
| clip(x, a, b) | 限制数组范围在[a, b]            |
| arr1 @ arr2   | 矩阵/向量乘法                   |
| arr.T         | 矩阵转置                        |

 ### Pandas

| 函数/运算符   | 功能                            |
| ------------- | ------------------------------- |
| read_json()   | 读取JSON文件为DataFrame         |
| df.iterrows() | 遍历DataFrame的行(索引和行数据) |

