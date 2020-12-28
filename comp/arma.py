import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf  # 画图定阶
from statsmodels.tsa.arima_model import ARIMA  # 模型
from statsmodels.tsa.arima_model import ARMA  # 模型
from statsmodels.tsa.stattools import acf, pacf
from sklearn.metrics import mean_squared_error
from pandas.plotting import autocorrelation_plot
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error,r2_score
from math import sqrt
from tqdm import tqdm


def get_data():
    # 数据读取和预处理
    csv_path = '../../data/nanrui.csv'
    df = pd.read_csv(csv_path)
    data = df['intemp']
    train_data = data[0:23250]
    test_data = data[23250:29010]
    return train_data, test_data


if __name__ == '__main__':
    train_data, test_data = get_data()
    # diff1 = train_data.diff(1).dropna()
    # diff1.plot(title='diff 1', figsize=(10, 4))
    # plt.show()
    #
    # # 确定参数
    # lag_acf = acf(diff1, nlags=20)
    # lag_pacf = pacf(diff1, nlags=20, method='ols')
    # # q的获取:ACF图中曲线第一次穿过上置信区间.这里q取2
    # plt.subplot(121)
    # plt.plot(lag_acf)
    # plt.axhline(y=0, linestyle='--', color='gray')
    # plt.axhline(y=-1.96 / np.sqrt(len(diff1)), linestyle='--', color='gray')  # lowwer置信区间
    # plt.axhline(y=1.96 / np.sqrt(len(diff1)), linestyle='--', color='gray')  # upper置信区间
    # plt.title('Autocorrelation Function')
    # # p的获取:PACF图中曲线第一次穿过上置信区间.这里p取2
    # plt.subplot(122)
    # plt.plot(lag_pacf)
    # plt.axhline(y=0, linestyle='--', color='gray')
    # plt.axhline(y=-1.96 / np.sqrt(len(diff1)), linestyle='--', color='gray')
    # plt.axhline(y=1.96 / np.sqrt(len(diff1)), linestyle='--', color='gray')
    # plt.title('Partial Autocorrelation Function')
    # plt.tight_layout()
    # plt.show()

    train_data = train_data.values
    test_data = test_data.values

    # ARIMA
    history = [x for x in train_data]
    predictions = list()
    for t in tqdm(range(len(test_data))):
        model = ARMA(history[-10000:], order=(2, 2))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test_data[t]
        history.append(obs)
        # print('predicted=%f, expected=%f' % (yhat, obs))

    # test
    print('mae : %f' % mean_absolute_error(test_data, predictions))
    print('rmse : %f' % sqrt(mean_squared_error(test_data, predictions)))
    print('r2 : %f' % r2_score(test_data, predictions))

    # plot
    plt.plot(test_data[-1000:])
    plt.plot(predictions[-1000:], color='red')
    plt.show()