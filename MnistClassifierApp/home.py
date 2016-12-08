from flask import Flask, request, jsonify
from werkzeug import secure_filename
import sys
from logistic_sgd import LogisticRegression, predict_class, sgd_optimization_mnist
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
	    	f.save('/home/ubuntu/FlaskApps/MnistClassifierApp/uploads/'+secure_filename(f.filename)) #saving posted images into uploads folder
	    	img = cv2.imread('/home/ubuntu/FlaskApps/MnistClassifierApp/uploads/'+secure_filename(f.filename)) #reading the posted image
	    	img_new = cv2.cvtColor(cv2.resize(img,(28,28)),cv2.COLOR_BGR2GRAY) #resizing image to 28 x 28 and converting image to grayscale
	    	img_new = img_new.flatten().reshape((1,784)) #flattening the image to a 1D array
	    	W = numpy.loadtxt('/home/ubuntu/FlaskApps/MnistClassifierApp/W.txt') #loading pretrained weights
	    	b = numpy.loadtxt('/home/ubuntu/FlaskApps/MnistClassifierApp/b.txt') #loading pretrained biases
	    	p_y_given_x = T.nnet.softmax(T.dot(img_new, W) + b) 
	    	y_pred = T.argmax(p_y_given_x, axis=1) #prediction
		return jsonify(Dataset = 'MNIST', PredictedDigit = str(y_pred.eval()))
	    except Exception as error:
		return str(error) + '400 - Bad Request. Check file type'
	else:
	    return 'No image attribute'
    else:
	return 'PLANET TAKE HOME - Please post to the URL'	
if __name__ == "__main__":
    app.run()
