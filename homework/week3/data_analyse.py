"""
用于数据集的特征分析
"""

import pandas as pd
import numpy as np
import sys

# ==================== 数据读取 ======================
print("数据分析")

try:
    file_name = input("输入文件名: ")
    df = pd.read_csv(file_name, header=0)
except:
    file_name = "QG_train.csv"
    df = pd.read_csv(file_name, header=0)

X = df.copy()
y = X.pop(df.columns[-1])

n_samples, n_features = X.shape
n_total_features = X.shape[1]

print(f"\n基本信息")
print("-"*40)
print(f"   样本数量：\t{n_samples}")
print(f"   特征数量：\t{n_features}")
print(f"   标签列：\t{df.columns[-1]}")

# ======================= 标签 =============================
print(f"\n标签分布")
print("-"*40)
labels = y.value_counts().sort_index()
for k, v in labels.items():
    print(f"   标签 {k}：\t{v} 个 \t({v/len(y)*100:.1f}%)")

"""特征"""
zero_ratio = (X == 0).sum().sum() / (X.shape[0] * X.shape[1]) * 100
print(f"\n特征全局统计")
print("-"*40)
print(f"   特征均值：\t{X.mean().mean():.4f}")
print(f"   特征标准差：\t{X.std().mean():.4f}")
print(f"   最小值：\t{X.min().min()}")
print(f"   最大值：\t{X.max().max()}")
print(f"   零值比例：\t{zero_ratio:.2f}%")

# ===================== 零值和常数特征 =====================
print(f"\n零值和常数特征分析")
print("-"*40)

var_feats = np.var(X, axis=0)
constant_features = X.columns[var_feats < 1e-9].tolist()
constant_count = len(constant_features)

zero_features = X.columns[(X == 0).all()].tolist()
zero_count = len(zero_features)

print(f"   全零特征数量：\t{zero_count} 个")
print(f"   常数特征数量：\t{constant_count} 个")

if zero_count > 0:
    print(f"   全零特征列表：\t{zero_features[:]}")
if constant_count > 0:
    # 排除全零特征，只显示非零的常数特征
    non_zero_constant = [f for f in constant_features if f not in zero_features]
    print(f"   非零常数特征：\t{non_zero_constant[:]}")

# ===================== 稀疏性 =====================
print(f"\n特征稀疏性")
print("-"*40)
non_zero_per_row = (X != 0).sum(axis=1).mean()
print(f"   每行平均非零特征数：{non_zero_per_row:.1f} / {n_total_features}")

# ===================== 异常值 =====================
print(f"\n异常值概览")
print("-"*40)

def outlier_ratio(s):
    q25, q75 = np.percentile(s, [25,75])
    iqr = q75 - q25
    lower = q25 - 1.5*iqr
    upper = q75 + 1.5*iqr
    return np.sum((s < lower) | (s > upper)) / len(s) * 100

avg_outlier = np.mean([outlier_ratio(X[c]) for c in X.columns])
print(f"   平均异常值比例：{avg_outlier:.2f}%")

# ===================== 特征与标签相关性 =====================
print(f"\n特征-标签相关性（前20个最高相关）")
print("-"*40)

corr_results = []
np.seterr(invalid='ignore')

for col in X.columns:
    corr = np.corrcoef(X[col], y)[0,1]
    if not np.isnan(corr):
        corr_results.append({
            'feature': col,
            'correlation': corr,
            'abs_correlation': abs(corr)
        })

if corr_results:
    sorted_corrs = sorted(corr_results, key=lambda x: x['abs_correlation'], reverse=True)
    top20_corrs = sorted_corrs[:20]
    
    all_abs_corrs = [x['abs_correlation'] for x in corr_results]
    print(f"   平均绝对相关：\t{np.mean(all_abs_corrs):.4f}")
    print(f"   最高相关：\t\t{np.max(all_abs_corrs):.4f}")
    print(f"\n   前20个最高相关特征：")
    print("   \t特征名\t相关系数\t绝对相关系数")
    
    for i, item in enumerate(top20_corrs, 1):
        print(f"   {i:2d}\t{item['feature']}\t{item['correlation']:.4f}\t\t{item['abs_correlation']:.4f}")

# ===================== 关键特征 =====================
print(f"\n区分能力前 30 特征")
print("-"*40)

if len(y.unique()) >= 2:
    y1 = y.unique()[0]
    y2 = y.unique()[1]
    g1 = X[y == y1].mean(axis=0)
    g2 = X[y == y2].mean(axis=0)
    diff = abs(g1 - g2)
    top30 = diff.nlargest(30)
    print("   \t特征\t差异")
    for i, (feat, d) in enumerate(top30.items(), 1):
        print(f"   {i:2d}\t{feat}\t{d:.4f}")
else:
    print(f"   标签类别不足")

print("\n分析完成\n")