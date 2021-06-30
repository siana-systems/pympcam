Coral Manager
=============

MPCam comes with a `Coral Accelerator Module <https://coral.ai/products/accelerator-module>`_.

PyMPCam provides :py:meth:`pympcam.coralManager` to turn on or off the module.

.. warning::
    By default, Coral Accelerator Module is turned off.

Examples
--------
The following example shows how to turn on/off the Coral Accelerator Module::

    from pympcam.coralManager import CoralManager
    coral = CoralManager()

    # turn on:
    coral.turnOn()

    # run TPU code ...

    # turn off:
    coral.turnOff()

To verify if the Coral Accelerator Module is available, check if it's listed with `lsusb`::

    import subprocess
    from time import sleep

    from pympcam.coralManager import CoralManager
    coral = CoralManager()

    # turn on the coral module:
    coral.turnOn()
    sleep(1)

    ret = subprocess.run(["lsusb"], capture_output=True)
    if "1a6e:089a" in ret.stdout.decode():
        print("Coral is ready!")

.. note:
    once the Coral Accelerator Module is turned on, it’ll take a few seconds to be online.
