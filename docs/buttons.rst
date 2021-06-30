MPCam Buttons
=============
MPCam board has two buttons available: SW1 and SW2.

PyMPCam provides :py:meth:`pympcam.userButtons` to access the buttons.

Examples
--------
The following example shows how to poll button state::

    from pympcam.userButtons import UserButtons
    btn = UserButtons()

    # check if SW1 is pressed: 
    if btn.getState("sw1"):
        print("Button#1 pressed!")
        
    # check if SW2 is pressed:
    if bt.getState("sw2"):
    print("Button#2 pressed!")

If a blocking behaviour is preferred (with a timeout)::

    from pympcam.userButtons import UserButtons
    btn = UserButtons()

    # wait for up to 5sec for SW1 to be pressed: 
    if btn.pollState( btn.SW1, 5000 ):
        print("Button#1 pressed!")
        
    # wait for up to 5sec for SW2 to be pressed:
    if bt.getState( btn.SW2, 5000 ):
    print("Button#2 pressed!")
