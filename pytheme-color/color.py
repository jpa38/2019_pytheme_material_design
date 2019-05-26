#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://pypi.org/project/webcolors/1.3/

# https://material.io/tools/color/#!/?view.left=0&view.right=0&primary.color=1d00db

# https://material.io/design/color/#color-theme-creation

# https://docs.python.org/3.6/library/colorsys.html

# https://www.colorhexa.com

import colorsys



class Baseline():

    def __init__(self):

        self.tblo_color = {}
        # self.tblo_color["TYPE", 'COLOR'])

        self.tblo_color["primary"] = "#6200ee"
        self.tblo_color["primary_variant"] = "#3700B3"

        self.tblo_color["secondary"] = "#03DAC6"
        self.tblo_color["secondary_variant"] = "#018786"

        self.tblo_color["background"] = "#FFFFFF"
        self.tblo_color["surface"] = "#FFFFFF"
        self.tblo_color["error"] = "#B00020"

        self.tblo_color["on_primary"] = "#FFFFFF"
        self.tblo_color["on_secondary"] = "#000000"
        self.tblo_color["on_background"] = "#000000"
        self.tblo_color["on_surface"] = "#000000"
        self.tblo_color["on_error"] = "#FFFFFF"

        self.lst_format = ["hexa","rgb","rgba","rgb_0_1","rgba_0_1","hsl","hsla","hls","yiq","hsv"]


    def _hexa_to_rgb(self,color):
        h = color.lstrip('#')
        rgb = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

        return rgb

    def _rgb_to_hsl(self,rgb):

        if type(rgb) == tuple or type(rgb) == list:
            return tuple(colorsys.rgb_to_hls(rgb[0],rgb[1],rgb[2]))

    def _rgb_to_rgb_0_1(self, rgb):

        if type(rgb) == tuple or type(rgb) == list:

            new_col = [round(rgb[0]/255,3),round(rgb[1]/255,3), round(rgb[2]/255,3)]

            if len(rgb) == 4:
                new_col.append(rgb[3])

                # for col in rgb:
                #     new_col.append(col / 256)
                # new_col.append(col/256)

            return tuple(new_col)

    def _rgb_to_yiq(self,rgb):
        if type(rgb) == tuple or type(rgb) == list:
            return tuple(colorsys.rgb_to_yiq(rgb[0],rgb[1],rgb[2]))

    def _rgb_to_hsv(self,rgb):
        if type(rgb) == tuple or type(rgb) == list:
            return colorsys.rgb_to_hsv(rgb[0],rgb[1],rgb[2])

    def _rgb_to_rgba(self,color, **kwargs):

        transparence = kwargs.get('alpha', 100)

        rgba = list(color)

        if transparence > 1 :
            rgba.append(int(transparence) / 100)
        else :
            rgba.append(float(transparence))

        return tuple(rgba)

    def _is_hexa_color(self,hex):
        hex = str(hex)
        if hex[0] =='#' and len(hex) == 7:
            return True
        else:
            return False

    def _is_rgb_color(self,rgb):
        if type(rgb)==list or type(rgb)==tuple:
            if len(rgb)==3:
                return True
        return False
    
    def _is_rgba_color(self,rgba):
        if self._is_rgb_color(rgba) and len(rgba)==4:
            return True
        else:
            return False

    def get_primary_color(self, mode):
        mode = mode.lower()
        if mode in self.lst_format:

            return self._get_color_by_type("primary", mode)

        else:
            return None

    def get_primary_variant_color(self, mode):
        mode = mode.lower()
        if mode in self.lst_format:

            return self._get_color_by_type("primary_variant", mode)

        else:
            return None
    
    def get_secondary_color(self, mode):
        mode = mode.lower()
        if mode in self.lst_format:

            return self._get_color_by_type("secondary", mode)

        else:
            return None

    def get_secondary_variant_color(self, mode):
        mode = mode.lower()
        if mode in self.lst_format:

            return self._get_color_by_type("secondary_variant", mode)

        else:
            return None

    def get_background_color(self, mode):
        mode = mode.lower()
        if mode in self.lst_format:

            return self._get_color_by_type("background", mode)

        else:
            return None
    
    def get_surface_color(self, mode):
        mode = mode.lower()
        if mode in self.lst_format:

            return self._get_color_by_type("surface", mode)

        else:
            return None
    
    def get_error_color(self, mode):
        mode = mode.lower()
        if mode in self.lst_format:

            return self._get_color_by_type("error", mode)

        else:
            return None
        
    def get_on_primary_color(self, mode):
        mode = mode.lower()
        if mode in self.lst_format:

            return self._get_color_by_type("on_primary", mode)

        else:
            return None
        
    def get_on_secondary_color(self, mode):
        mode = mode.lower()
        if mode in self.lst_format:

            return self._get_color_by_type("on_secondary", mode)

        else:
            return None
    
    def get_on_background_color(self, mode):
        mode = mode.lower()
        if mode in self.lst_format:

            return self._get_color_by_type("on_background", mode)

        else:
            return None
        
    def get_on_surface_color(self, mode):
        mode = mode.lower()
        if mode in self.lst_format:

            return self._get_color_by_type("on_surface", mode)

        else:
            return None
    
    def get_on_error_color(self, mode):
        mode = mode.lower()
        if mode in self.lst_format:

            return self._get_color_by_type("on_error", mode)

        else:
            return None
        
    

    def _get_color_by_type(self, type_color, mode):
        """

        Args:
            type_color:
            mode: hexa,rgb,rgba,rgb_0_1,rgba0_1,hsl,hsla

        Returns:

        """
        color = self.tblo_color.get(type_color)

        mode = str(mode).lower()

        if mode == "hexa":
            return color

        elif mode == "rgb":
            return self._hexa_to_rgb(color)

        elif mode == "rgba":

            a = self._hexa_to_rgb(color)
            b = self._rgb_to_rgba(a)

            return b

        elif mode == "rgba_0_1":

            a = self._hexa_to_rgb(color)
            b = self._rgb_to_rgba(a)
            c = self._rgb_to_rgb_0_1(b)

            return c

        elif mode == "rgb_0_1":

            a = self._hexa_to_rgb(color)
            b = self._rgb_to_rgb_0_1(a)

            return b

        elif mode == "hsl":
            # TODO A valider
            a = self._hexa_to_rgb(color)
            b = self._rgb_to_rgb_0_1(a)
            c = self._rgb_to_hsl(b)

            return c

        elif mode == "hsla":
            # TODO A valider
            a = self._hexa_to_rgb(color)
            b = self._rgb_to_rgba(a)
            c = self._rgb_to_hsl(b)

            return c

        elif mode == "hsv":
            # TODO A valider
            a = self._hexa_to_rgb(color)
            b = self._rgb_to_rgb_0_1(a)
            c = self._rgb_to_hsv(b)

            return c

        elif mode == "yiq":
            # TODO A valider
            a = self._hexa_to_rgb(color)
            b = self._rgb_to_yiq(a)

            return b

        else :
            print("Format non reconnu")

    def set_primary_color(self, color):
        if self._is_hexa_color(color):
            self.tblo_color["primary"] = hex
        elif self._is_rgb_color(color):
            color_hex = '#%02x%02x%02x' % color
            self.tblo_color["primary"] = color_hex
        else:
            print("Can't assign color")

    def set_primary_variant_color(self, color):
        if self._is_hexa_color(color):
            self.tblo_color["primary_variant"] = hex
        elif self._is_rgb_color(color):
            color_hex = '#%02x%02x%02x' % color
            self.tblo_color["primary_variant"] = color_hex
        else:
            print("Can't assign color")

    def set_secondary_color(self, color):
        if self._is_hexa_color(color):
            self.tblo_color["secondary"] = hex
        elif self._is_rgb_color(color):
            color_hex = '#%02x%02x%02x' % color
            self.tblo_color["secondary"] = color_hex
        else:
            print("Can't assign color")

    def set_secondary_variant_color(self, color):
        if self._is_hexa_color(color):
            self.tblo_color["secondary_variant"] = hex
        elif self._is_rgb_color(color):
            color_hex = '#%02x%02x%02x' % color
            self.tblo_color["secondary_variant"] = color_hex
        else:
            print("Can't assign color")
    
    def set_background_color(self, color):
        if self._is_hexa_color(color):
            self.tblo_color["background"] = hex
        elif self._is_rgb_color(color):
            color_hex = '#%02x%02x%02x' % color
            self.tblo_color["background"] = color_hex
        else:
            print("Can't assign color")
            
    def set_surface_color(self, color):
        if self._is_hexa_color(color):
            self.tblo_color["surface"] = hex
        elif self._is_rgb_color(color):
            color_hex = '#%02x%02x%02x' % color
            self.tblo_color["surface"] = color_hex
        else:
            print("Can't assign color")
            
    def set_error_color(self, color):
        if self._is_hexa_color(color):
            self.tblo_color["error"] = hex
        elif self._is_rgb_color(color):
            color_hex = '#%02x%02x%02x' % color
            self.tblo_color["error"] = color_hex
        else:
            print("Can't assign color")
    
    def set_on_primary_color(self, color):
        if self._is_hexa_color(color):
            self.tblo_color["on_primary"] = hex
        elif self._is_rgb_color(color):
            color_hex = '#%02x%02x%02x' % color
            self.tblo_color["on_primary"] = color_hex
        else:
            print("Can't assign color")

    def set_on_secondary_color(self, color):
        if self._is_hexa_color(color):
            self.tblo_color["on_secondary"] = hex
        elif self._is_rgb_color(color):
            color_hex = '#%02x%02x%02x' % color
            self.tblo_color["on_secondary"] = color_hex
        else:
            print("Can't assign color")
    
    def set_on_background_color(self, color):
        if self._is_hexa_color(color):
            self.tblo_color["on_background"] = hex
        elif self._is_rgb_color(color):
            color_hex = '#%02x%02x%02x' % color
            self.tblo_color["on_background"] = color_hex
        else:
            print("Can't assign color")

    def set_on_surface_color(self, color):
        if self._is_hexa_color(color):
            self.tblo_color["on_surface"] = hex
        elif self._is_rgb_color(color):
            color_hex = '#%02x%02x%02x' % color
            self.tblo_color["on_surface"] = color_hex
        else:
            print("Can't assign color")

    def set_on_error_color(self, color):
        if self._is_hexa_color(color):
            self.tblo_color["on_error"] = hex
        elif self._is_rgb_color(color):
            color_hex = '#%02x%02x%02x' % color
            self.tblo_color["on_error"] = color_hex
        else:
            print("Can't assign color")
    
    
    

if __name__ == '__main__':

    tt = Baseline()
    # print(tt.get_rgb_0_1(tt.get_rgb('#689f38')))

    tt.set_primary_color((102,205,170))

    print("hexa = ", tt.get_primary_color("hexa"),type(tt.get_primary_color("hexa")))
    print("rgb = ", tt.get_primary_color("rgb"),type(tt.get_primary_color("rgb")))
    print("rgb_0_1 = ", tt.get_primary_color("rgb_0_1"),type(tt.get_primary_color("rgb_0_1")))
    print("rgba = ", tt.get_primary_color("rgba"),type(tt.get_primary_color("rgba")))
    print("rgba_0_1 = ", tt.get_primary_color("rgba_0_1"),type(tt.get_primary_color("rgba_0_1")))
    print("hsl = ", tt.get_primary_color("hsl"),type(tt.get_primary_color("hsl")))
    print("hsv = ", tt.get_primary_color("hsv"),type(tt.get_primary_color("hsv")))
    print("yiq = ", tt.get_primary_color("yiq"),type(tt.get_primary_color("yiq")))





    print("stop")