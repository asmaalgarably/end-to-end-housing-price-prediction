import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LinearRegression
import pickle

url='https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv'

data=pd.read_csv(url)
data =data.dropna()
x = data.drop(['median_house_value', 'ocean_proximity'], axis=1)
y = data['median_house_value']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=44)

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)
selcter=SelectFromModel(estimator=LinearRegression())
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

print("Training", model.score(x_train,y_train))
print("Testing",model.score(x_test,y_test))

with open('train_model.pkl','wb') as f:
    pickle.dump(model,f)

with open('scaler.pkl','wb') as f:
    pickle.dump(scaler,f)






