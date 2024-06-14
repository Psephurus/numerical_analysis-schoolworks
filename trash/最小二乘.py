import numpy as np

def main():
    # 定义输入数据
    x = np.array([[-1], [0], [1], [2]])
    y = np.array([1, 0, 0, -2])
    
    # 构建设计矩阵A，包括常数项、x和x的平方
    A = np.hstack([np.ones((x.shape[0], 1)), x, x**2])
    
    # 计算A的转置乘以A，和A的转置乘以y
    A_transpose_A = np.dot(A.T, A)
    A_transpose_y = np.dot(A.T, y)
    
    # 解线性方程组得到最小二乘解
    coefficients = np.linalg.solve(A_transpose_A, A_transpose_y)
    
    # 输出结果
    print("最小二乘估计得到的参数:", coefficients)
    
    # 计算并输出矩阵的条件数
    condition_number = np.linalg.cond(A_transpose_A)
    print("条件数:", condition_number)

if __name__ == '__main__':
    main()
