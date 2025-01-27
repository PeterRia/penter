# 源码：https://github.com/scikit-learn/scikit-learn
# 中文：https://github.com/apachecn/sklearn-doc-zh
# https://apachecn.gitee.io/sklearn-doc-zh/

[scikit-learn和tensorflow的区别](https://www.cnblogs.com/timlong/p/11098661.html)

Scikit-learn(sklearn)的定位是通用机器学习库，而TensorFlow(tf)的定位主要是深度学习库。
一个显而易见的不同：tf并未提供sklearn那种强大的特征工程，如维度压缩、特征选择等。
究其根本，我认为是因为机器学习模型的两种不同的处理数据的方式：
传统机器学习：利用特征工程(feature engineering)，人为对数据进行提炼清洗
深度学习：利用表示学习(representation learning)，机器学习模型自身对数据进行提炼

sklearn更倾向于使用者可以自行对数据进行处理，比如选择特征、压缩维度、转换格式，是传统机器学习库。而以tf为代表的深度学习库会自动从数据中抽取有效特征，而不需要人为的来做这件事情，因此并未提供类似的功能。

封装在tf等工具库上的keras才更像深度学习界的sklearn

sklearn主要适合中小型的、实用机器学习项目，尤其是那种数据量不大且需要使用者手动对数据进行处理，并选择合适模型的项目。这类项目往往在CPU上就可以完成，对硬件要求低。
tf主要适合已经明确了解需要用深度学习，且数据处理需求不高的项目。这类项目往往数据量较大，且最终需要的精度更高，一般都需要GPU加速运算。

更常见的情况下，可以把sklearn和tf，甚至keras结合起来使用。sklearn肩负基本的数据清理任务，keras用于对问题进行小规模实验验证想法，而tf用于在完整的的数据上进行严肃的调参(炼丹)任务。
而单独把sklearn拿出来看的话，它的文档做的特别好，初学者跟着看一遍sklearn支持的功能大概就对机器学习包括的很多内容有了基本的了解。举个简单的例子，sklearn很多时候对单独的知识点有概述，比如简单的异常检测。因此，sklearn不仅仅是简单的工具库，它的文档更像是一份简单的新手入门指南。
因此，以sklearn为代表的传统机器学习库（如瑞士军刀般的万能但高度抽象），和以tf为代表的自由灵活更具有针对性的深度学习库（如乐高般高度自由但使用繁琐）都是机器学习者必须要了解的工具。

文档：https://scikit-learn.org/stable/index.html
视频：https://www.bilibili.com/video/BV1MA411J7wm?from=search&seid=7616958068850337769

机器学习的大致流程都是：数据获取——数据预处理——选择学习算法——训练模型——模型优化——可视化等。

scikit-learn大体分成了六部分，其中clasification、regression、clustering都是主要的学习算法。
demensionality reduction、preprocessing是用来数据预处理的。
model selection则是用来做模型评估和优化的。


四类算法:分类，回归，聚类，降维

分类：识别一个对象属于哪个类别。
SVM
nearest neighbors
random forest

回归：预测与对象关联的连续值属性。
SVR
nearest neighbors
random forest

聚类：将相似的对象自动分组成集合。
 k-Means
 spectral clustering
 mean-shift
 
降维：减少要考虑的随机变量数量。
k-Means
feature selection
non-negative matrix factorization

模型选择：比较、验证和选择参数和模型。
 grid search
 cross validation
 metrics
 
预处理：特征提取与归一化。
  preprocessing
  feature extraction

conda install python-graphviz
scikit-learn学习
https://github.com/CodeZBW/Machine-Learning

# autosklearn
AutoML
https://github.com/automl/auto-sklearn
```python
import autosklearn.classification
cls = autosklearn.classification.AutoSklearnClassifier()
cls.fit(X_train, y_train)
predictions = cls.predict(X_test)
```
