#!/usr/bin/env python
# -*- coding: utf-8 -*-

import color

from tkinter import *

theme = color.Baseline()


class carre():

    def __init__(self, parent, back, text):

        self.color_back = back
        self.color_text = text
        self.parent = parent



    def frame(self):
        Frame2 = Frame(self.parent, borderwidth=2, relief=GROOVE, bg = self.color_back)


        Frame2.pack(side=LEFT, padx=10, pady=10)

        return Frame2

def carre_demo(parent, back, front, texte):

    frame = Frame(parent, relief=GROOVE, bg=back, height=100, width=100,bd=5)
    frame.pack_propagate(False)
    frame.pack(expand=True, fill='x')

    label = Label(frame, text=texte, bg=back, fg=front, font='bold')
    label.pack(side=TOP,anchor='nw', fill = 'y')

    label = Label(frame, text=back, bg=back, fg=front)
    label.pack(side=BOTTOM, anchor='se')



    return frame

def interligne():
    frame_vide = Frame(fenetre, height=50, width=500)
    frame_vide.pack_propagate(False)
    frame_vide.pack(side=TOP)

fenetre = Tk()


frame_line_1 = Frame(fenetre, height = 100, width = 500)
frame_line_1.pack_propagate(False)
frame_line_1.pack(side=TOP)

carre_demo(frame_line_1, theme.get_primary_color("hexa"),theme.get_on_primary_color("hexa"),"Primary").pack(side=LEFT)
carre_demo(frame_line_1, theme.get_primary_variant_color("hexa"),theme.get_on_primary_color("hexa"),"Primary\nVariant").pack(side=LEFT)

carre_demo(frame_line_1, theme.get_secondary_color("hexa"),theme.get_on_secondary_color("hexa"),"Secondary").pack(side=LEFT)
carre_demo(frame_line_1, theme.get_secondary_variant_color("hexa"),theme.get_on_secondary_color("hexa"),"Secondary\nVariant").pack(side=LEFT)

interligne()

frame_line_2 = Frame(fenetre, height = 100, width = 500)
frame_line_2.pack_propagate(False)
frame_line_2.pack(side=TOP)

carre_demo(frame_line_2, theme.get_background_color("hexa"),theme.get_on_background_color("hexa"),"Background").pack(side=LEFT)
carre_demo(frame_line_2, theme.get_surface_color("hexa"),theme.get_on_surface_color("hexa"),"Surface").pack(side=LEFT)
carre_demo(frame_line_2, theme.get_error_color("hexa"),theme.get_on_error_color("hexa"),"Error").pack(side=LEFT)


fenetre.mainloop()
