# Driver Safety Awareness project

Driver Monitoring System

Goals:
* Promote safe driving habits
* Raise awareness
* Change driver behaviour
* Help to prevent car accidents

The Driver Monitoring System is based on a camera that monitors the driver's behaviour during a road trip. When the driver enters the car he / she is recognized or a new profile is created for analyzing drivers performance.
The system provides immediate feedback on positive and negative behaviour. It warns when the driver gets tired and requires a break. It immediately alerts the driver when a dangerous situation occurs, suc as texting while driving). 
After each trip the system analyses the data and generates a report that can be send to the drivers smartphone. The driver can then review its own behaviour and adjust it to improve its safety.

![image](doc/driver-monitoring.jpg )

Monitor driver behavior:
  * Good driving habits
    * Wearing seat belt
    * Active driving posture
    * Hands on the steering wheel
    * Looking to the general driving direction
    * Checking for traffic from all directions
    * Rear mirror checking
   * Abstain from distractions
     * Mobile phone usage (handheld, call, texting)
     * Operating the radio
     * Talking to passengers
     * Eating or drinking
     * Other (looking for something)
   * Driver physics
     * Body, arm and hand position
     * Head pose (rotation, looking direction)
     * Driver drowsiness
       * Eye blinking/closed
       * Head bobbing
       * Mouth yawning
  
  
 Tools and technology
 * Face location, Face landmarks, Driver recognition
 * Head Pose estimation
 * OpenCV (CV2), Dlib
 * Python-video-annotator [code](https://github.com/chan0park/video-annotation-tool) / [documentation](https://pythonvideoannotator.readthedocs.io/en/master/index.html)
 * Eyeblink8 [dataset](https://www.blinkingmatters.com/research)