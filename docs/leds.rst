MPCam LEDs
==========
The MPCam provides two user LEDs: LED1 (blue) and LED2 (red), and IR LEDs.

PyMPCam provides :py:meth:`pympcam.userLed` to control the user LEDs, and
:py:meth:`pympcam.irLed` to control the IR LEDs.

Examples
--------
The following example shows how to turn on/off the user LEDs::

    from pympcam.userLed import UserLed
    led = userLed()

    # turn on blue/red LEDs:
    led.turnOn("LED1")  # blue
    led.turnOn("LED2")  # red

    # turn off blue/red LEDs:
    led.turnOff("LED1") # blue
    led.turnOff("LED2") # red

The following example shows how to turn on/off the IR LEDs::

    from pympcam.irLed import IrLed
    ir = IrLed()

    # turn On IR LEDs:
    ir.turnOn()

    # turn Off IR LEDs:
    ir.turnOff()
