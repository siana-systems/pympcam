MPCam LEDs
==========
MPCam board has two user LEDs available to the user: LED1 (blue) and LED2 (red).
There is also two Infrared (IR) LEDs available for the user.

PyMPCam provides :py:meth:`pympcam.userLed` to access the user LEDs, and
:py:meth:`pympcam.irLed` to access IR LEDs.

Examples
--------
The following example shows how to turn on/off user LEDs::

    from pympcam.userLed import UserLed
    led = userLed()

    # turn on blue/red LEDs:
    led.turnOn("LED1")  # blue
    led.turnOn("LED2")  # red

    # turn off blue/red LEDs:
    led.turnOff("LED1") # blue
    led.turnOff("LED2") # red

The following example shows how to turn on/off IR LEDs::

    from pympcam.irLed import IrLed
    ir = IrLed()

    # turn On IR LEDs:
    ir.turnOn()

    # turn Off IR LEDs:
    ir.turnOff()
