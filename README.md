# Human-body-Measurement-using-image-processing-
In this research, we proposed a model that targets to improve the approach of Tailoring industries in online sector. This experiment is conducted on a sample dataset where the measurement of the volunteer and the images are taken manually. To implement this research, we have used a pre trained pose detection algorithm to detect the joints/key on the body. We also have used edge detection algorithm finding the edges of the body. with the help of joint/key detection we calculated the linear measurement. With the help of both joints/key detection and edge detection we calculated the circular measurement. In comparison of linear measurement and circular measurement the accuracy of linear measurement is quite good. Due to the limitation of the resources we were not able to collect sufficient data. But we can increase the accuracy of this model by increasing the number in dataset so that the error factor in every measurement will be more precise.
<br><br>
We Have implemented this project using python and image processing libarary which is opencv <br>
<br>
<h3>Let's see How to download and Run this project to get correct output</h3><br>
1. first clone/download this project and unziped in your system<br>
2. Install all the requirement libarary for this project <br>
         <pre><code>pip install numy</code></pre>
         <pre><code>pip install opencv-python</code></pre>
         <pre><code>pip install mediapipe</code></pre>
       
3. Make sure that input image must be present in the same directory which is used in linear_measurement.py file
4. Now open command promote or any text editor you like
5. run the following command to run python file
      <pre><code>python linear_measurement.py</code></pre>
      
