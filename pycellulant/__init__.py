"""
pycellulant: A Python wrapper on Cellulant public API for mobile payments Integration.
=============================================================================

Contents
--------
pycellulant contents goes here!

Subpackages
-----------
Using any of the pycellulant subpackages requires either
an explicit or implicit import. For example,
``import pycellulant`` | ``import pycellulant.cellulant`` | ``from pycellulant import cellulant``.

::

 cellulant                    --- Cellulant class
 cellulant_exceptions         --- Exception classes
 service_urls                 --- Services urls


Utility tools
-------------
::

 tests                    --- Run pycellulant unittests

Changelog
---------
Version 0.1** - 2024 December 12
    Initial release.

"""

__version__ = '0.1'
__all__ = ['Cellulant',]

from pycellulant.cellulant import cellulant
