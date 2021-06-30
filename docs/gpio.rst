MPCam GPIO
=============

MPCam board has GPIO headers available for the user.
They could be used as inputs, output, and some of them as PWM.

PyMPCam provides :py:meth:`pympcam.headerIo` to access all GPIOs, and
:py:meth:`pympcam.headerPwm` for PWM enabled pins.