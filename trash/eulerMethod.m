function [times, values] = eulerMethod(interval, initialValue, numSteps)
    % 使用欧拉方法求解微分方程。
    %
    % 输入:
    %   interval - 时间区间 [开始, 结束]
    %   initialValue - 区间开始处的初始值
    %   numSteps - 时间区间的划分步数
    %
    % 输出:
    %   times - 时间点数组
    %   values - 每个时间点对应的解数组
    %
    % 示例用法:
    %   [times, values] = eulerMethod([0, 1], 1, 10);
    
        times = zeros(1, numSteps + 1);  % 预分配时间数组
        values = zeros(1, numSteps + 1); % 预分配值数组
        times(1) = interval(1);
        values(1) = initialValue;
        stepSize = (interval(2) - interval(1)) / numSteps;
    
        for i = 1:numSteps
            times(i + 1) = times(i) + stepSize;
            values(i + 1) = eulerStep(times(i), values(i), stepSize);
        end
        
        % 绘制解的图形
        plot(times, values);
        title('使用欧拉方法求解微分方程的结果');
        xlabel('时间');
        ylabel('解的值');
    end
    
    function nextValue = eulerStep(currentTime, currentValue, stepSize)
    % 单步欧拉法
    % 使用欧拉方法计算解的下一个值。
    %
    % 输入:
    %   currentTime - 当前时间
    %   currentValue - 当前的解值
    %   stepSize - 步长
    %
    % 输出:
    %   nextValue - 下一个时间步的解估计值
    
        nextValue = currentValue + stepSize * derivative(currentTime, currentValue);
    end
    
    function dydt = derivative(time, value)
    % 微分方程的导数函数
    % 例如，微分方程 dy/dt = t * y + t^3。
    %
    % 输入:
    %   time - 当前时间
    %   value - 当前解的值
    %
    % 输出:
    %   dydt - 给定时间和值的导数值
    
        dydt = time * value + time^3;
    end
    