#!/bin/python3
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from typing import List, Tuple, Optional

def _read_file(file_name: str) -> str:
    """
    Args:
        file: name of file to read
        
    Returns:
        String contents of the given file
    """
    f = open(file_name, "r")
    return f.read()
    
    
def _get_x_and_y_from_string(string: str, min_tolerance: float, max_tolerance: float) -> Tuple[List[List[float]], List[float]]:
    """
    Args:
        string: string in format '\nx1,y1\nx2,y2\n'
        min_tolerance: minimum tolerance to apply to the y value
        max_tolerance: maximum tolerance to apply to the y value
        
    Returns:
        List of x values and list of y values where 
            y is less than the given tolerance.
    """
    rows = string.split("\n")[:-1]
    X = []
    Y = []
    
    for row in rows:
        [x, y] = row.split(",")
        if (float(y) > min_tolerance) & (float(y) < max_tolerance):
            X.append([float(x)])
            Y.append(float(y))
            
    return X, Y
    

def _train_model_and_predict(
    X: List[List[float]], 
    y: List[float], 
    X_test: List[List[float]],
    y_test: List[float],
    X_predict: List[List[float]],
    ) -> Tuple[List[float], float]:
    """
    Args:
        X: {array-like, sparse matrix} of shape (n_samples, n_features)
        y: array-like of shape (n_samples,) or (n_samples, n_targets)
        X_test: array-like or sparse matrix, shape (n_samples, n_features)
        y_test: array-like of shape (n_samples,) or (n_samples, n_targets)
        X_predict: array-like or sparse matrix, shape (n_samples, n_features)
        
    Returns:
        Predicted y for given X_predict using a linear regression model 
            trained on the given X and y data. The score of the model 
            is output as the second variable in the returned Tuple.
    """
    model = LinearRegression()
    model.fit(X, y)
    
    score = model.score(X_test, y_test)
    y_predict = model.predict(X_predict)

    return y_predict, score


if __name__ == '__main__':
    time_charged = float(input().strip())
    X_predict = time_charged
    
    scores = []
    
    dataset_str = _read_file("trainingdata.txt")
    
    for max_tolerance in np.arange(15, 0, -0.5):
        for min_tolerance in np.arange(15, 0, -0.5):
            if min_tolerance < max_tolerance:
                X, y = _get_x_and_y_from_string(dataset_str, min_tolerance, max_tolerance)

                if len(X) > 30:
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, train_size = 0.8, random_state=42)
                    y_predict, score = _train_model_and_predict(X_train, y_train, X_test, y_test, [[X_predict]])
                    
                    scores.append(
                        {"score": score, "y_predict": y_predict}
                        )
                    
    max_scores = max(scores, key=lambda x:x["score"])
    best_y_predict = round(max_scores["y_predict"][0], 2)
    
    if best_y_predict > 8:
        print(8)
    else:
        print(best_y_predict)
