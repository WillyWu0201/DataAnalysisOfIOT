from sklearn import datasets as ds
from sklearn import preprocessing
from pandas import DataFrame as df


# 1. get data
iris = ds.load_iris()
X = iris.data
Y = iris.target

# 2. normalization
scaler = preprocessing.StandardScaler()
print(X[:5])
scaler.fit(X)
X = scaler.transform(X)
print(X[:5])

# 2.5 train test split
from sklearn.cross_validation import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size= 0.25, random_state=33)

from sklearn.cross_validation import cross_val_score, KFold
cv = KFold(X.shape[0], 5, shuffle=True, random_state=33)

# 3. transform

# # 4. fitting sklearn
# from sklearn.linear_model import LogisticRegression as LR
# model = LR()
# model.fit(X, Y)
# # out = model.predict([[-0.90068117, 1.03205722, -1.3412724, -1.31297673]])
# out = model.predict(X)
# print(out)

# 4.1 fitting split data
from sklearn.linear_model import LogisticRegression as LR
model = LR()
# model.fit(Xtrain, Ytrain)
# out = model.predict(Xtrain)
# print(out)

# # 5. evaluate
# score = model.score(X, Y)
# print(score)

# 5. split data evaluate
# from sklearn import metrics
# score = metrics.accuracy_score(out, Ytrain)
# print(format("training score is {}".format(score)))

score = cross_val_score(model, X, Y, cv=cv)
print(format("training score is {}".format(score)))

# scoreTrain = model.score(Xtrain, Ytrain)
# scoreTest = model.score(Xtest, Ytest)
# print(format("training score is {}".format(scoreTrain)))
# print(format("training score is {}".format(scoreTest)))
