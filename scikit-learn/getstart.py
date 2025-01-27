from sklearn import datasets  #从sklearn包中加载数据集模块
from sklearn import svm
import pickle
#iris = datasets.load_iris()  #加载鸢尾花数据集
from sklearn.model_selection import GridSearchCV,learning_curve
from sklearn.tree import DecisionTreeClassifier

digits = datasets.load_digits() #加载数字图像数据集 ,原始的样例是一张（8 x 8）的图片 digits.images[0]

"""
对于digits数据集，digits.data可以访问得到用来对数字进行分类的特征：
digits.target 就是数字数据集各样例对应的真实数字值。也就是我们的程序要学习的。
"""
# 算法，模型选择
clf = svm.SVC(gamma=0.001, C=100.)
#训练
clf.fit(digits.data[:-1], digits.target[:-1])

# partial_fit
# 这个方法的一般用在如果训练集数据量非常大，一次不能全部载入内存的时候。这时我们可以把训练集分成若干等分，重复调用partial_fit来一步步的学习训练集，非常方便。


#预测，我们可以让这个训练器预测没有作为训练数据使用的最后一张图像是什么数字。
print(clf.predict(digits.data[-1:]))


print(digits.target[-1])

# 模型持久化
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
print(clf2.predict(digits.data[-1:]))

# https://joblib.readthedocs.io/en/latest/persistence.html
# from joblib import dump, load
# dump(clf, 'filename.joblib')
# clf3 = load('filename.joblib')
# print(clf3.predict(digits.data[-1:]))

# 练习
iris = datasets.load_iris()
clf_iris = svm.SVC()
clf_iris.fit(iris.data[:-1], iris.target[:-1])
print(clf_iris.predict(iris.data[-1:]))
print(iris.target[-1])

# 参数调优1：学习曲线(缺点：不能舍弃参数)
train_sizes, train_scores, test_scores = learning_curve(clf, iris.data,iris.target, cv=10, n_jobs=1, train_sizes=[0.1,0.325,0.55,0.775,1])
"""
1、estimator：用于预测的模型
2、X：预测的特征数据
3、y：预测结果
4、train_sizes：训练样本相对的或绝对的数字，这些量的样本将会生成learning curve，当其为[0.1, 0.325, 0.55, 0.775, 1. ]时代表使用10%训练集训练，32.5%训练集训练，55%训练集训练，77.5%训练集训练100%训练集训练时的分数。
5、cv：交叉验证生成器或可迭代的次数
6、scoring：调用的方法 https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter

# 学习曲线模块
from sklearn.model_selection import learning_curve 
# 导入digits数据集
from sklearn.datasets import load_digits 
# 支持向量机
from sklearn.svm import SVC 
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()
X = digits.data
y = digits.target

# neg_mean_squared_error代表求均值平方差
train_sizes, train_loss, test_loss = learning_curve(
    SVC(gamma=0.01), X, y, cv=10, scoring='neg_mean_squared_error',
    train_sizes=np.linspace(.1, 1.0, 5))

# loss值为负数，需要取反
train_loss_mean = -np.mean(train_loss, axis=1)
test_loss_mean = -np.mean(test_loss, axis=1)

# 设置样式与label
plt.plot(train_sizes, train_loss_mean, 'o-', color="r",
         label="Training")
plt.plot(train_sizes, test_loss_mean, 'o-', color="g",
        label="Cross-validation")

plt.xlabel("Training examples")
plt.ylabel("Loss")
# 显示图例
plt.legend(loc="best")
plt.show()
"""


# 参数调优2：网格搜索(缺点：不能舍弃参数)
# parameters = {'splitter':('best','random')
#               ,'criterion':("gini","entropy")
#               ,"max_depth":[*range(1,10)]
#               ,'min_samples_leaf':[*range(1,50,5)]
#               ,'min_impurity_decrease':[*np.linspace(0,0.5,20)]
#              }
#
# clf = DecisionTreeClassifier(random_state=25)
# GS = GridSearchCV(clf, parameters, cv=10)
# GS.fit(Xtrain,Ytrain)
#
# GS.best_params_
#
# GS.best_score_

# 交叉验证
# from sklearn.datasets import load_boston
# from sklearn.model_selection import cross_val_score
# from sklearn.tree import DecisionTreeRegressor
# boston = load_boston()
# regressor = DecisionTreeRegressor(random_state=0)
# cross_val_score(regressor, boston.data, boston.target, cv=10,
#                 scoring = "neg_mean_squared_error")

"""
Transform(): Method using these calculated parameters apply the transformation to a particular dataset.
解释：在Fit的基础上，进行标准化，降维，归一化等操作（看具体用的是哪个工具，如PCA，StandardScaler等）。

Fit_transform(): joins the fit() and transform() method for transformation of dataset.
解释：fit_transform是fit和transform的组合，既包括了训练又包含了转换。

transform()和fit_transform()二者的功能都是对数据进行某种统一处理（比如标准化~N(0,1)，将数据缩放(映射)到某个固定区间，归一化，正则化等）

fit_transform(trainData)对部分数据先拟合fit，找到该part的整体指标，如均值、方差、最大值最小值等等（根据具体转换的目的），然后对该trainData进行转换transform，从而实现数据的标准化、归一化等等。

根据对之前部分trainData进行fit的整体指标，对剩余的数据（testData）使用同样的均值、方差、最大最小值等指标进行转换transform(testData)，从而保证train、test处理方式相同。所以，一般都是这么用：

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit_tranform(X_train)
sc.tranform(X_test)

1. 必须先用fit_transform(trainData)，之后再transform(testData)
2. 如果直接transform(testData)，程序会报错
3. 如果fit_transfrom(trainData)后，使用fit_transform(testData)而不transform(testData)，虽然也能归一化，但是两个结果不是在同一个“标准”下的，具有明显差异。(一定要避免这种情况)
"""

# 数据预处理 https://zhuanlan.zhihu.com/p/38160930


