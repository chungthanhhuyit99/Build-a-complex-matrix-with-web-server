from Tkinter import *
import re
import time
import argparse
import sys
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

text = sys.argv[1]

def Message(text):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded = 4, block_orientation = 180, blocks_arranged_in_reverse_order = True) 
    show_message(device,text,fill="white", font=proportional(CP437_FONT))
    time.sleep(1)

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.Text = Entry(frame,fg="red",bg="cyan",font=("Helvetica", 30))
        self.Text.grid(row=0, column=0)

        self.Run_Button = Button(frame, text='Run', command = self.run_text,font=("Helvetica", 30))
        self.Run_Button.grid(row=0, column=1)

    def run_text(self):
        temp_text = self.Text.get()
        Message(temp_text)
print(text)
Message(text)

