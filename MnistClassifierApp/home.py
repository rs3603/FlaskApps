#sudo pip install opencv-python
#import cv2
from flask import Flask, request
from werkzeug import secure_filename
import sys
#sys.path.insert(0,'/home/ubuntu/FlaskApps/MnistClassifierApp/DeepLearningTutorials/code/')
from logistic_sgd import LogisticRegression, predict_class, sgd_optimization_mnist
#from test import read
import cv2
import numpy
import theano
import theano.tensor as T
import six.moves.cPickle as pickle

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	return 'PLANET TAKE HOME - Please post to the URL http://54.165.174.252/mnist/classify'

@app.route('/mnist',methods=['GET','POST'])
def mnist():
        return 'PLANET TAKE HOME - Please post to the URL http://54.165.174.252/mnist/classify'

@app.route('/mnist/classify',methods=['GET','POST'])
def home():
    if request.method == 'POST':
	if 'image' in request.files:
	    f = request.files['image']
	    try:
	    	f.save('/home/ubuntu/FlaskApps/MnistClassifierApp/uploads/'+secure_filename(f.filename))
	    	img = cv2.imread('/home/ubuntu/FlaskApps/MnistClassifierApp/uploads/'+secure_filename(f.filename))
	    	img_new = cv2.cvtColor(cv2.resize(img,(28,28)),cv2.COLOR_BGR2GRAY)
	    	img_new = img_new.flatten().reshape((1,784))
	    	W = numpy.loadtxt('/home/ubuntu/FlaskApps/MnistClassifierApp/W.txt')
	    	b = numpy.loadtxt('/home/ubuntu/FlaskApps/MnistClassifierApp/b.txt')
	    	p_y_given_x = T.nnet.softmax(T.dot(img_new, W) + b)
	    	y_pred = T.argmax(p_y_given_x, axis=1)
	    	return str(y_pred.eval())
	    except:
		return '400 - Bad Request. Check file type'
	else:
	    return 'No image attribute'
    else:
	return 'PLANET TAKE HOME - Please post to the URL'	
if __name__ == "__main__":
    app.run()
