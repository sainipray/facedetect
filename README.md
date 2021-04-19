
Live Face Detection using Opencv with Django or Tornado Framework
======================================

It'll capture image from your webcam and detect your face. It's also supported real time face detect from webcam video.

Installation
=============

   * Please make sure you already installed Python3 and pip in your system, then Clone this repository ::

    git clone https://github.com/talhaanwarch/facedetect.git

   * Now install requirements of python libraries ::

    pip install -r requirements.txt

   * Now we need to run tornado server for create websocket ::

    python websocket.py 
   #It may be show popup for allow or not firewall , So click on allow to run websocket

   *  Now run Django project using below command ::
     
    python manage.py runserver

   * Now you can access project ::

     http://127.0.0.1:8000/image/  #  detect face from image

     http://127.0.0.1:8000/video/  #  detect face from live webcam

   * **Note**  
    If you are on a windows machine, you can open two terminal one for websocket and the other for django server.     
    On linux server you may move tornado server to background and then lanuch django server.


