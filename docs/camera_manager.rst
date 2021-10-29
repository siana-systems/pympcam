Camera Manager
=============

PyMPCam provides :py:meth:`pympcam.cameraManager` to control camera parameters, like gain, exposure and white balance.


Examples
--------
The following example shows how to set Gain::

    from pympcam.cameraManager import CameraManager, ExposureMode
    
    camera = CameraManager()

    # turn on:
    camera.set_autoGain(True)
