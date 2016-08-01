from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt, savetxt

def randomForest():
	#create the training & test sets, skipping the header row 
	train = pd.read_csv("data/train.csv")    # make sure you're in the right directory if using iPython!
	test = pd.read_csv("data/test.csv") 

	train.head()             # ignore the first column, it's how I split the data.

	# however, are data has to be in a numpy array in order for the random forest algorithm to except it!
	cols = ['petal_length', 'petal_width', 'sepal_length', 'sepal_width']
	colsRes = ['class']
	trainArr = train.as_matrix(cols)    # training array
	trainRes = train.as_matrix(colsRes) # training results
	    
	#create and train the random forest
	#multi-core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)
	rf = RandomForestClassifier(n_estimators=100)
	rf.fit(train, target)

	#savetxt('data/submission2.csv', rf.predict(test), delimiter=',', fmt='%f')

	# put the test results in the same format!
	testArr = test.as_matrix(cols)

	results = rf.predict(testArr)

	# something I like to do is to add it back to the dataframe, so I can compare side-by-side
	test['predictions'] = results
	test.head()
#end main()

randomForest()