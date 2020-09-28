#python scripts for running machine-learning models
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier

#Test this function so that it runs with different models

#running different scikit machine learning models
def run_ml_model(xtrain,ytrain,xtest,ytest, model):
    #this means if model=knn instansiate with this
    inst={ 'knn': KNeighborsClassifier(),
           'xgboost': XGBClassifier()} [value]
    ml=inst[model]
    ml.fit(X_train, y_train)
    y_pred = ml.predict(X_test)
    acc_xg= ml.score(X_test, y_test)
    print('\n')
    print('*'*10, model,  '*'*10)
    print('Predicted target values:', y_pred)
    print('Accuracy:', acc_xg)
    print('*'*10)
    return(y_pred, acc)

#test to see if it works for both models

if __name__=="__main__":
#run automated tests here
