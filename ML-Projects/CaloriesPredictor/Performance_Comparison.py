import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('calories.csv')
df = df.drop(columns=['User_ID'])  # Drop ID column

X = df.drop(columns=['Calories'])
y = df['Calories']

# Preprocessing
categorical = ['Gender']
numerical = ['Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(drop='first'), categorical),
    ('num', StandardScaler(), numerical)
])

sns.boxplot(df['Age'])
plt.show()

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.svm import SVR

models = {
    'RandomForest': RandomForestRegressor(random_state=42),
    'GradientBoosting': GradientBoostingRegressor(random_state=42),
    'LinearRegression': LinearRegression(),
    'Ridge': Ridge(),
    'Lasso': Lasso(),
    'SVR': SVR()
}

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

performance = {}

for name, model in models.items():
    pipeline = Pipeline([
        ('preprocessing', preprocessor),
        ('regressor', model)
    ])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred)
    
    performance[name] = {'R2': r2, 'RMSE': rmse}

# Display sorted results
sorted_perf = sorted(performance.items(), key=lambda x: x[1]['R2'], reverse=True)
for name, metrics in sorted_perf:
    print(f"{name}: R2 = {metrics['R2']:.4f}, RMSE = {metrics['RMSE']:.2f}")