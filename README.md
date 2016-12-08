# MNIST Digit Classifier

This project allows the user to post an MNIST digit image to an URL which returns the digit class of the image. The server is currently hosted on an AWS EC2 server with the following url 
http://54.165.174.252/mnist/classify

Typical usage instructions for testing:

    #test script
    import requests
    url = 'http://54.165.174.252/mnist/classify'
    files = {'image': open(<filename>,'rb')}
    r = requests.post(url,files=files)
    print r.content
    
    
    
