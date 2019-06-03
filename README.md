

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
    - [PyTheme's Input/Output](#pythemes-inputoutput)
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

![README](https://www.plantuml.com/plantuml/png/0/jLLTQuCm57qlz3_SD_V1T2zZCDfIDhQz5jht4kEj3Oj9IQuRClRV5tLWswarXVeYvfoJe-SU8a1zpIqnGtacnwE_5OW2ovb4U7ouXo-Hq3Q86Z0WGGvR5AijPXXOu99P6un73QLQWMTcKGg5yDqWOGWlMce3IzA6fHY63NO754iTyWf_0YaiDU1qUh39Mwuu2QsSVSa3ql3-ke9Qkx_fBQH8wvqH6JF5kiAl9l6CYXtMJpUJA9vTTma-cH5CqN2XHQvLukNLIBpTOiO_KgDpbNZOvMR3E0uNe37QN8okbVzqdEQCd9tgdBnACz_8d6Pm3AURlUnejcrhTiTRsRvIzsXQSXx4zl5ecqgVoV4qUhX7K-XXjlMmd-uNJKVxJbXuVEh_phMIVmuEQbI41ZPQbxT5GVj7-ZvnZYfnluXV "README")

<details>

    ```plantuml
        @startuml
        /'scale 750 width'/
        'title PyTheme's class'

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

        center footer Pytheme's class

        @enduml
    ```

</details>

### PyTheme's Input/Output

![README-1](https://www.plantuml.com/plantuml/png/0/Kr2008VYaiIYajBS75ukg8W2WbMGc9oTc9wgu9HOd9gJcPUgO6FZuHhX69CNN5AKcPTkPwTGZL2CghKMmTG8SdUAoRErZSaBAIt8ILN8BrBmoImkqLJGrRL366sbu9bNK5g2f0rY5KWVn3g26e3sE99W4K8dN0waC1hiN5rTg2cnG0t-fIKeDg6gXxWJf07YJi8w80ubmGgG1WM3HssJ34dLHeOkZs0V4jM7aQG-qZEGW7e4AparhoIrI24jFnz41LI6PAJcfgeNGw9G7w9F8QIo81KvEXrIyrA0AHe0 "README-1")


<details>

    ```plantuml
        @startuml
        
        package Baseline <<HEXA\nString>> {
            
        }
        (RGB\n==\nTuple or List) --> Baseline : Input
        (HEXA\n==\nString) --> Baseline : Input
        (RGBA\n==\nTuple or List) --> Baseline : Input

        Baseline --> [RGB\n--\nTuple] : Output
        Baseline --> [HEXA\n--\nString] : Output
        Baseline --> [RGBA\n--\nTuple] : Output
        Baseline --> [RGBA 0→1\n--\nTuple] : Output
        Baseline --> [RGB 0→1\n--\nTuple] : Output
        Baseline --> [HSL\n--\nTuple] : Output
        Baseline --> [HSV\n--\nTuple] : Output
        Baseline --> [YIQ\n--\nTuple] : Output
        
        center footer PyTheme's Input/Output Type

        @enduml
    ```

</details>


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

If you use pycharm :
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
