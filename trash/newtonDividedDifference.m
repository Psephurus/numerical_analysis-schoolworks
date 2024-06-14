function coefficients = newtonDividedDifference(x, y, numPoints)
    % 牛顿差商插值法
    % 计算插值多项式的系数
    % 输入: x 和 y 是包含 n 个数据点的 x 坐标和 y 坐标的向量
    % 输出: 插值多项式的系数，使用嵌套形式
    
        % 初始化差商表
        dividedDifferences = zeros(numPoints, numPoints);
        dividedDifferences(:, 1) = y(:);
        
        % 计算差商表的其它列
        for col = 2:numPoints
            for row = 1:numPoints - col + 1
                numerator = dividedDifferences(row + 1, col - 1) - dividedDifferences(row, col - 1);
                denominator = x(row + col - 1) - x(row);
                dividedDifferences(row, col) = numerator / denominator;
            end
        end
        
        % 从差商表的顶端读取系数
        coefficients = dividedDifferences(1, 1:numPoints);
        
        % 示例评估多项式的值
        testX = 1.5; % 修改为所需的 x 值
        polynomialValue = nestedMultiplication(numPoints - 1, coefficients, testX, x);
        disp(['The polynomial value at x = ', num2str(testX), ' is ', num2str(polynomialValue)]);
    end
    
    function y = nestedMultiplication(d, c, x, b)
    % 嵌套乘法法计算多项式值
    % 输入: 多项式的度数 d,
    %       多项式的系数数组 c (常数项在前),
    %       评估点 x,
    %       基点数组 b (如果需要)
    % 输出: 多项式在 x 处的值 y
    
        if nargin < 4, b = zeros(d, 1); end
        y = c(d + 1);
        for i = d:-1:1
            y = y .* (x - b(i)) + c(i);
        end
    end
    