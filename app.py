#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:55:16 2021

@author: user
"""

import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

#To upload ClassFile
def addClassList():
    filename1 = filedialog.askopenfilename()
    
    print('Selected:', filename1)

def addZoomList():
    filename2 = filedialog.askopenfilename()
    
    print('Selected:', filename2)




canvas = tk.Canvas(root, height = 700, width = 700, bg = "#263D42")
canvas.pack()
frame = tk.Frame(root, bg = "white")
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely=0.1)

uploadClassFile = tk.Button(root, text = "Upload Class List", padx=10,
                     pady=5, fg="green", bg="#263D42", command = addClassList)
uploadClassFile.pack()

uploadZoomFile = tk.Button(root, text = "Upload Zoom File", padx=10,
                     pady=5, fg="green", bg="#263D42", command = addZoomList)
uploadZoomFile.pack()

root.mainloop()