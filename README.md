

# <center>PyTheme Material Design



---

## Summary

todo

## Description

Color management for Gui with Material Design directives. If you want to build your GUI with a material theme, you can use this the project to manage your colors. 

There is some color to manage :
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


I create this program to learn python and github project pratices.
I am working with the windows's pycharm app.

## Installation

- Clone repo
  - todo command line
- Use `Requirement.txt` to install dependencies
  - todo if necessary

## Usage

```python
 import todo
 ```

1. Create your class :


```python
myguicolor = Baseline()
```
2. Set your colors:

> You can set Hexa color (type `str`) or RGB color (type `list` or type `tuple`)


```python
myguicolor.set_primary_color('#6200EE')
```
or
```python
myguicolor.set_primary_color([92,0,93.3])
```

3. Get your color

```python
myguicolor.get_primary_color("rgb")
```
Return `[92,0,93.3]`

If you want to view an palette with your color:
```python
todo
```

## Command list

### Command to set color

You can set two color by two type:
1. `hexadecimal` color, set first charactere must be `#`
2. `rgb decimal` color, must be `list` or `tuple`

Aviaible commands :







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
