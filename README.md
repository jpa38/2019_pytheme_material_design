

# <center>PyTheme Material Design

</center>

---

## Summary

- [<center>PyTheme Material Design](#centerpytheme-material-design)
  - [Summary](#summary)
  - [Description](#description)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Détails Usage](#d%C3%A9tails-usage)
    - [Command](#command)
    - [Diagram class](#diagram-class)
    - [`color*` can be :](#color-can-be)
    - [`type_color*` can be:](#typecolor-can-be)
  - [Contributing](#contributing)
  - [Versionning](#versionning)
  - [Authors](#authors)
  - [License](#license)
  - [TODO](#todo)

## Description

Simple Class for color management's GUI with Material Design directives. If you want to build your GUI with a material theme, you can use this the project to manage your colors.

There is some colors's type to manage :
- Primary
- Primary Variant
- Secondary
- Secondary Variant
  
- Background
- Surface
- Error
  
- On Primary
- On Secondary
- On Background
- On Surface
- On Error


I create this program to learn python and github project practices.
I am working with the windows's pycharm app.

## Installation

- Clone repo :
  ```
  git clone https://github.com/jpa38/pytheme_material_design.git
  ```
- ~~Use `Requirement.txt` to install dependencies~~
  ```
  pip install -r requirements.txt
  ```

## Usage

1. Import the class
```python
from pytheme_material_design.pytheme_color.color import Baseline
 ```

2. Create your class :
```python
myguicolor = Baseline()
```

3. Set your colors:

> You can set Hexa color (type `str`) or RGB color (type `list` or type `tuple`)


```python
myguicolor.set_primary_color('#6200EE')
```
or
```python
myguicolor.set_primary_color([92,0,93.3])
```

3. Get your color in your GUI's code

```python
myguicolor.get_primary_color("rgb")
```
Return `[92,0,93.3]`

If you want to view an palette with your color:
```python
todo
```

## Détails Usage

### Command
You can set an color by two types:
1. `hexadecimal` color, `string type`, the first character must be `#`
2. `rgb decimal` color, `tuple` or `list` type

### Diagram class

![PyTheme's class](https://www.plantuml.com/plantuml/png/0/jLTHRzem47wlrFzmwXue6uHGhJ0XYgfLNTUdJeAtQK97ue6rO3FReKNJ_ljiiv4KI6nNdLy0t_VTz_dki1A0xRgM2eNAbzdfoTyTw3HaWXc1_cKCZpHLYqQd22ggTEZBPh8WIzAGa6GevUb90R0Ry14boIWZyAk8H17Sy8mB62ikS4wYg8YrGSqo7YKsFe2CIbK4hwwU9VcKiqHHphIwmO7YS7SxWIstdFGTp8cQhWHTejXCRVnyE1kfpOfiVxqTTcQZPXLXZO8YK_v4IHBEqY2jWXAiDiFanrpmdAK1ShduZWdn9n0XkFXlSCx2kwCvBwYpPhsaNaOij6IQurq6zsIFAoPR7fli2bUoRgXhE4Vgx8KEqJZMbJgH_MxKOFUwK8CyDeVryB3IL4oVGoBWg8SpTnJyktnHtzYBch9LhgPYFYlVr6QD3mRil1jVj2xYorQt7pURBlJN4lhR7lhUYC94_or0Ap_pz-_hWgQaP2wX8ib8ZNqCyz_gne5dC8pwSw37GT1naWLvyZZ9sPjUBqaHpwhzVDQ9N7wiM9KVdgkAoRWBcem7cyUZsIL1jwTfFErw-8gZzos8em-n_UZr-Wvt9gsFGollTecUfGDJEp131jt8LK7qCUZJL_GiOhX3tpAYJnqNCdERl7rQ4Rr1cCAinfpEvVHbz9oMrgzeQUrXQUsojA4_NysIpkMqPFGEBPcrU_Hlvwlsg7I73-p3pD0FZG5mUu_ju5M4b3yoJIbTCmFxtZ3o9c0mmyvti4muoyni864THZ3ztX4AoZLXgNvv_0C0 "PyTheme's class")


<!---
    ```plantuml
        @startuml
        /'scale 750 width'/
        title PyTheme's class

        class Baseline {
        .. Color Storage..
        - tblo.color : list
        ==
        .. Function's list to GET color ..
        + get_primary_color(<b>type_color*</b>)
        + get_primary_variant_color(<b>type_color*</b>)
        + get_secondary_color(<b>type_color*</b>)
        + get_secondary_variant_color(<b>type_color*</b>)
        + get_background_color(<b>type_color*</b>)
        + get_surface_color(<b>type_color*</b>)
        + get_error_color(<b>type_color*</b>)
        + get_error_color(<b>type_color*</b>)
        + get_on_primary_color(<b>type_color*</b>)
        + get_on_secondary_color(<b>type_color*</b>)
        + get_on_background_color(<b>type_color*</b>)
        + get_on_surface_color(<b>type_color*</b>)
        + get_on_error_color(<b>type_color*</b>)
        ==
        .. Function's list to SET color ..
        + set_primary_color(<b>color*</b>)
        + set_primary_variant_color(<b>color*</b>)
        + set_secondary_color(<b>color*</b>)
        + set_secondary_variant_color(<b>color*</b>)
        + set_background_color(<b>color*</b>)
        + set_surface_color(<b>color*</b>)
        + set_error_color(<b>color*</b>)
        + set_on_primary_color(<b>color*</b>)
        + set_on_secondary_color(<b>color*</b>)
        + set_on_background_color(<b>color*</b>)
        + set_on_surface_color(<b>color*</b>)
        + set_on_error_color(<b>color*</b>)
        }

        Class input_rgb {
            Set_primary_color((102,205,170))
            Set_primary_color([102,205,170])
            Input Type rgb
        }
        hide input_rgb circle

        Class input_rgba {
            Set_primary_color((102,205,170,100))
            Set_primary_color([102,205,170,100])
            Input Type rgba
        }
        hide input_rgba circle

        Class input_hexa {
            Set_primary_color("#66cdaa")
            Input Type Hexa
        }
        hide input_hexa circle

        Class output_rgb {
            Get_primary_color((102,205,170))
            Output Type rgb
        }
        hide output_rgb circle

        Class output_rgb_0_1 {
            Get_primary_color((0.4, 0.804, 0.667))
            Output Type rgb_0_1
        }
        hide output_rgb_0_1 circle

        Class output_rgba {
            Get_primary_color((102, 205, 170, 1.0))
            Output Type rgba
        }
        hide output_rgba circle

        Class output_rgba_0_1 {
            Get_primary_color((102, 205, 170, 1.0))
            Output Type rgba_0_1
        }
        hide output_rgba_0_1 circle

        Class output_hsl {
            Get_primary_color(Experimental)
            Output Type hsl
        }
        hide output_hsl circle

        Class output_hsv {
            Get_primary_color(Experimental)
            Output Type hsv
        }
        hide output_hsv circle

        Class output_yiq {
            Get_primary_color(Experimental)
            Output Type yiq
        }
        hide output_yiq circle

            Baseline -up-> input_rgb : SET <
            Baseline -up-> input_rgba : SET <
            Baseline -up-> input_hexa : SET <

            Baseline -down-> output_rgb : GET >
            Baseline -down-> output_rgba : GET >
            Baseline -down-> output_rgb_0_1 : GET >
            Baseline -down-> output_rgba_0_1 : GET >
            Baseline -down-> output_hsl : GET >
            Baseline -down-> output_hsv : GET >
            Baseline -down-> output_yiq : GET >

        @enduml
    ```
-->

### `color*` can be :

| COLOR 	| Example **INPUT**                           	| Type       	|
|-------	|---------------------------------------------	|------------	|
| hexa  	| #66cdaa                                     	| String     	|
| rgb   	| (102, 205, 170) / [102, 205, 170]           	| Tuple/List 	|
| rgba  	| (102, 205, 170, 1.0) / [102, 205, 170, 1.0] 	| Tuple/List 	|


### `type_color*` can be:

| MODE     	| Example OUTPUT             	| Type   	|
|----------	|--------------------------	|--------	|
| hexa     	| #66cdaa                  	| String 	|
| rgb      	| (102, 205, 170)          	| Tuple  	|
| rgba     	| (102, 205, 170, 1.0)     	| Tuple  	|
| rgb_0_1  	| (0.4, 0.804, 0.667)      	| Tuple  	|
| rgba_0_1 	| (0.4, 0.804, 0.667, 1.0) 	| Tuple  	|
| hsl      	| Experimental             	| Tuple  	|
| hsla     	| Experimental             	| Tuple  	|
| hls      	| Experimental             	| Tuple  	|
| yiq      	| Experimental             	| Tuple  	|
| hsv      	| Experimental             	| Tuple  	|

## Contributing

Write your comments with the Google Style Python Docstrings

- Document code with google style, check your pycharm's settings :
    Go to `File | Settings | Tools | Python Integrated Tools`
    - Find `Docstring format` and put  `Google`

- Comment's particularities, Go to `File | Settings | Editor | TODO`
    - To improve the reading's code comment:
        - `titre .*`  = title level 1
        - `titre- .*`  = title level 2
        - `titre-- .*`  = title level 3
    - To remember to check an utility :
        - `\bused\b.*`
    - To remember the futur improve functionalities :
        - `\bupgrademe\b.*`



## Versionning

We use [SemVer](http://semver.org/) for versioning :


    Given a version number MAJOR.MINOR.PATCH, increment the:

        1. MAJOR version when you make incompatible API changes,
        2. MINOR version when you add functionality in a backwards-compatible manner, and
        3. PATCH version when you make backwards-compatible bug fixes.

## Authors
- Jérôme PALANCA

## License

This project is licensed under the **MIT License**

## TODO
- [ ] todo
