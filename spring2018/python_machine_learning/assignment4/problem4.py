"""
Implement your own logistic regression and classify the iris data into setosa or non-setosa. You are
supposed to write your own logit function and implement gradient descent to learn optimal weights. Then
using this weight classify the entire data set as setosa or non-setosa. We encourage you not to use
logistic regression implementation of scikit learn package. (If you are facing too much difficulty during
implementation you can use packages no marks will be deducted for that. However, please try your best
to avoid using packages. ) Report how much accuracy you got. You can try your logistic regression code
on some other dataset as well for binary classification.

author: Averill Cate, Jr <acate@iu.edu>
"""
import numpy as np
import pandas as pd


def zscore_normalize(df):
    """ Computes a z-score normalization.  We are only using
    the 'class' column for now.
    """

    columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    data = df[columns]

    for i in data.columns:
        mean = data[i].mean()
        std = data[i].std()
        zscore = df[i].apply(lambda d: float(d - mean) / float(std))
        df[i] = zscore

    return df


if __name__ == '__main__':
    df = pd.read_csv('iris.csv')
    df_normalized = zscore_normalize(df)
    print(df_normalized.head())
