#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:18:58 2025

@author: damildot
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#iris veri setini yükle
iris=load_iris()
df=pd.DataFrame(data=iris.data,columns=iris.feature_names)
df["target"]=iris.target

X= iris.data
y=iris.target


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

tree_clf=DecisionTreeClassifier(criterion="gini",max_depth=1,random_state=42)
tree_clf.fit(X_train,y_train)

y_pred=tree_clf.predict(X_test)
accuracy=accuracy_score(y_test, y_pred)
print(f"test accuracy:{accuracy}") #burdan şunu anlıyoruz çok güzel öğrenmiş

y_pred_train=tree_clf.predict(X_train)
accuracy_train=accuracy_score(y_train, y_pred_train)
print(f"train accuracy:{accuracy_train}")  
"""

train accuracy: 0.99
test accuracy: 0.8 olsaydı traini ezberlediği için testi yanlış çıkıyo olacaktı overfitting

trst accuracy:1.0 
train accuracy: 0.999 çok iyi öğrenmiş deriz çünkü birbirlerine yakın

"""
from sklearn.tree import DecisionTreeClassifier, plot_tree

conf_matrix=confusion_matrix(y_test, y_pred)

plt.figure()
sns.heatmap(conf_matrix,annot=True,cmap="Blues",fmt="g",xticklabels=iris.target_names)
plt.xlabel("tahmin edilen değerler")
plt.ylabel("gerçek sınıf")
plt.title("confusion matrix")


plt.figure(figsize=(15,10))
plot_tree(tree_clf,filled=True,feature_names=iris.feature_names,class_names=iris.target_names)

# feature selectionda bir tane seçecek olsaydık ginisi en yüksek olanı seçerdik

feature_importances=tree_clf.feature_importances_    # en önemli olanı bulmak için 

feature_names= iris.feature_names

feature_importances_sorted=sorted(zip(feature_importances,feature_names),reverse=True)

for importance,feature_name in feature_importances_sorted:
    print(f"{feature_name}: {importance}")
    
#buna bir threshold atınca gereksizlerden kurtuluruz

"""
ödevvv 
kanser verisetiyle 
decision tree ile plot çizicez 
kötü iyi huylu olmak üzere veriyi sınıflandıracagız 

"""





