"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Ji Li.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    root = tkinter.Tk()

    # ------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame1 = ttk.Frame(root, padding= 10)
    frame1.grid()


    # ------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    hello_button = ttk.Button(frame1, text= 'hello')
    hello_button.grid()

    # ------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    hello_button['command']= lambda :print_hello()

    def print_hello():
        print('hello 儿子 ')

    # ------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    frame2 = ttk.Frame(root, padding= 20)
    frame2.grid()

    my_entry_box = ttk.Entry(frame2)
    my_entry_box.grid()

    hello_goodbye_button = ttk.Button(frame2, text= 'Hello_Goodbye')
    hello_goodbye_button.grid()

    hello_goodbye_button['command']= lambda  :hello_goodbye(my_entry_box)

    def hello_goodbye(entrybox):
        contents = entrybox.get()
        if contents == 'ok':
            print('hello')
        else:
            print('goodbye')

    second_entry_box = ttk.Entry(frame1)
    second_entry_box.grid()

    n_times_button = ttk.Button(frame1, text='input an integer')
    n_times_button['command'] = lambda: n(my_entry_box, second_entry_box)
    n_times_button.grid()

    def n(entry_box, second_ectry_box):
        contents = entry_box.get()
        n = second_ectry_box.get()
        m = int(n)
        print(m * contents)

    # ------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    # ------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # ----------------------------------------------------------
    root.mainloop()



# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
