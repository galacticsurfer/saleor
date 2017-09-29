Steps to run websocket server as a daemon:

1. Create logs directory within the protocols directory

2. Create a new virtual environment with python 2
    virtualenv -p python2 env

3. Upgrade pip
    pip install -U pip

4. Run pip install -r requirements.txt within the protocols directory

5. To run the server run the following command from the protocols directory
    twistd -l logs/socket.log --python=server.py

6. Check whether a twistd.pid is created within the protocols directory.


To stop the twisted daemon:

1. Run the following command
    kill $(cat twistd.pid)
