# MNIST Digit Classifier

This project allows the user to post an MNIST digit image to an URL which returns the digit class of the image. The server is currently hosted on an AWS EC2 server with the following url 
http://54.165.174.252/mnist/classify


There is an AWS AMI setup with all the packages installed and source code for further development.

AMI Name : Raghavendra_TakeHome

AMI ID : ami-351b1a22

Typical usage instructions for testing:

    #test script
    #please install the 'requests' package before testing
    # $sudo pip install requests 
    import requests
    url = 'http://54.165.174.252/mnist/classify'
    files = {'image': open(<filename>,'rb')}
    r = requests.post(url,files=files)
    print r.content
 
# Instructions to build the code and hosting on your own server

1. To install all the required packages, the install.sh script can be used <br />
   ```
   sudo sh install.sh
   ```
2. Open an empty script as follows <br />
   ```
   sudo nano /etc/apache2/sites-available/MnistClassifierApp.conf
   ```
3. Now paste the following configuration code in it. 
   Note: The paths in the above script may change based on where you clone the repository   

    ```
    <VirtualHost *:80>
        ServerName <your ip>
        ServerAdmin admin@mywebsite.com
        WSGIDaemonProcess MnistClassifierApp threads=5
        WSGIScriptAlias / /home/ubuntu/FlaskApps/FlaskApps.wsgi
        <Directory /home/ubuntu/FlaskApps/>
            WSGIProcessGroup MnistClassifierApp
            WSGIApplicationGroup %{GLOBAL}
            Order allow,deny
            Allow from all
            Require all granted
        </Directory>
        <Directory /home/ubuntu/FlaskApps/MnistClassifierApp/static/>
            Order allow,deny
            Allow from all
            Require all granted
        </Directory>
        ErrorLog ${APACHE_LOG_DIR}/error.log
        LogLevel warn
        CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>
    ```

4. Run the following commands <br />

    ```
    sudo a2enmod wsgi 
    sudo apachectl restart
    sudo a2ensite MnistClassifierApp
    
    sudo service apache2 reload
    sudo service apache2 restart
    sudo /etc/init.d/apache2 reload
    ```
   The server is now up and running. The image can be POSTed to http://<your_url>/mnist/classify and a json is returned. In case of        changes made to the .wsgi script or any files in the Flask app, the following commands have to be run
    ```
    sudo service apache2 reload
    sudo service apache2 restart
    sudo /etc/init.d/apache2 reload
    ```
In case of any errors, it maybe identified by looking at the error log
    ```
    sudo nano /var/log/apache2/error.log
    ```
    

# The Model


Logistic regression is a probabilistic, linear classifier. It is parametrized by a weight matrix W and a bias vector b. Classification is done by projecting an input vector onto a set of hyperplanes, each of which corresponds to a class. The distance from the input to a hyperplane reflects the probability that the input is a member of the corresponding class.

Mathematically, the probability that an input vector x is a member of a class i, a value of a stochastic variable Y, can be written as:

P(Y=i|x, W,b) = softmax(W*x + b) 
              = (e^{W_i x + b_i})/(sum{e^{W_j x + b_j}})
              
The model’s prediction y_{pred} is the class whose probability is maximal, specifically:

y_pred = {argmax}_i P(Y=i|x,W,b)

The algorithm is implemented using the Theano framework.

# References
1. http://amunategui.github.io/idea-to-pitch/
2. https://github.com/lisa-lab/DeepLearningTutorials/
3. http://yann.lecun.com/exdb/mnist/
4. http://deeplearning.net/tutorial/logreg.html
