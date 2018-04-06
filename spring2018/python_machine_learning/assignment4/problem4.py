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
from sklearn import linear_model


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


def filter_data(df, column):
    column_name = [col for col in df.columns if col not in column]
    data_frame = df[column]  # get all the data i.e X
    label_frame = df[[column]]  # get all the target or labels i.e Y
    size = len(data_frame)
    training_data = data_frame.loc[range(1, int(size / 2))]  # Take first half as training
    training_label = label_frame.loc[range(1, int(size / 2))]  # take first half as training label
    test_data = data_frame.loc[range(int(size / 2), size)]  # take second half as test
    test_label = label_frame.loc[range(int(size / 2), size)]

    return training_data, np.asarray(training_label).flatten(), test_data, np.asarray(test_label).flatten()


def calc_base_line(df):

    class_values = np.unique(df)
    highest = 0
    base_class = 0.0

    for l in class_values:
        count = len(df[df == l])

        if count > highest:
            highest = count
            base_class = l

    print("base Line :",(float(highest)/len(df))*100)

if __name__ == '__main__':
    df = pd.read_csv('iris.csv')
    df_normalized = zscore_normalize(df)
    training, label, test, test_label = filter_data(df_normalized, 'class')

    logreg = linear_model.LogisticRegression(C=0.09, n_jobs=-1)
    calc_base_line(df_normalized)

    print(df_normalized.head())
