#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_version():
    return __version__


def get_auteur():
    return __author__


def get_copyright():
    return __copyright__


def get_license():
    return __license__


def get_name():
    return __name__


def get_last_version():
    versionning = []
    versionning.append(["0.0.1", "Création du script"])
    versionning.append(["0.1.1", "Insertion de la GUI"])
    versionning.append(["0.2.0", "Ajout du versionning"])

    return versionning[-1][0]


__author__ = "Jérome PALANCA"
__owner__ = "BOUYGUES ENERGIES ET SERVICES"
__year__ = "2019"
__copyright__ = "©" +" " + __owner__ + " " + __year__
__credits__ = []
__license__ = "Creative Commons Attribution Share Alike 4.0"
__license_keyword__ = "cc-by-sa-4.0"
__license_link__ = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
__version__ = get_last_version()
__maintainer__ = "Jérôme PALANCA"
__email__ = ""
__status__ = "Production"
__name__ = "Export SEE TO SQLite"

