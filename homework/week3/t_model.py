import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def train_model(X_train, y_train, learning_rate=0.05, epochs=10000, lambda_l2=0.05):
    """
    训练逻辑回归模型
        X_train         训练特征（已标准化和偏置项）
        y_train         训练标签（0/1）
        learning_rate   学习率
        epochs          迭代次数
        lambda_l2       L2正则系数
    返回：
        w: 训练好的权重
    """
    # 初始化权重
    w = np.zeros(X_train.shape[1])
    n_samples = len(y_train)

    # 迭代训练
    for epoch in range(epochs):
        # 前向传播
        z = np.dot(X_train, w)
        y_pred = sigmoid(z)
        
        # 梯度计算
        dw = np.dot(X_train.T, (y_pred - y_train)) / n_samples
        dw[1:] += lambda_l2 * w[1:]  # L2 正则（不惩罚偏置项）
        
        # 更新权重
        w -= learning_rate * dw

        # 打印日志
        if epoch % 1000 == 0:
            loss = -np.mean(y_train * np.log(y_pred + 1e-8) + (1 - y_train) * np.log(1 - y_pred + 1e-8))
            acc = np.mean((y_pred > 0.5) == y_train)
            print(f"Epoch {epoch:4d} | Loss: {loss:.4f} | Acc: {acc:.4f}")
    
    return w