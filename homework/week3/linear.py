import pandas as pd
import numpy as np

"""数据读取"""
df_train = pd.read_csv("QG_train.csv")
X_train = df_train.drop("target", axis=1).values
y_train = df_train["target"].values
y_train = np.where(y_train == -1, 0, 1)

df_test = pd.read_csv("QG_test.csv")
X_test = df_test.drop("target", axis=1).values
y_test = df_test["target"].values
y_test = np.where(y_test == -1, 0, 1)

"""标准化"""
X_mean = np.mean(X_train, axis=0)
X_std = np.std(X_train, axis=0)
X_std[X_std == 0] = 1

X_train = (X_train - X_mean) / X_std
X_train = np.c_[np.ones(X_train.shape[0]), X_train]

"""sigmoid"""
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

"""训练模型"""
w = np.zeros(X_train.shape[1])
learning_rate = 0.05
epochs = 10000
lambda_l2 = 0.05

for epoch in range(epochs):
    z = np.dot(X_train, w)
    y_pred = sigmoid(z)
    
    """交叉熵损失"""
    loss = -np.mean(y_train * np.log(y_pred + 1e-8) + (1 - y_train) * np.log(1 - y_pred + 1e-8))
    
    """梯度"""
    dw = np.dot(X_train.T, (y_pred - y_train)) / len(y_train)
    dw[1:] += lambda_l2 * w[1:]
    
    """权重更新"""
    w -= learning_rate * dw

    """打印"""
    if epoch % 1000 == 0:
        acc = np.mean((y_pred > 0.5) == y_train)
        print(f"Epoch {epoch:4d} | Loss: {loss:.4f} | Acc: {acc:.4f}")

"""测试集"""
X_test = (X_test - X_mean) / X_std
X_test = np.c_[np.ones(X_test.shape[0]), X_test]

"""测试集预测"""
z_test = np.dot(X_test, w)
y_test_pred = sigmoid(z_test)
y_test_pred_class = (y_test_pred > 0.5).astype(int)

"""结果输出"""
test_acc = np.mean(y_test_pred_class == y_test)
print(f"\nrate:{learning_rate}\tepochs:{epochs}\tl2:{lambda_l2}")
print("="*50)
print(f"训练集准确率: {np.mean((sigmoid(np.dot(X_train, w))>0.5)==y_train):.4f}")
print(f"测试集准确率: {test_acc:.4f}")
print("="*50)