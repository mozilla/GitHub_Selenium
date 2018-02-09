===============
GitHub Selenium
===============

..
    .. image:: https://img.shields.io/pypi/v/github_selenium.svg
            :target: https://pypi.python.org/pypi/github_selenium

    .. image:: https://img.shields.io/travis/hwine/github_selenium.svg
            :target: https://travis-ci.org/hwine/github_selenium

    .. image:: https://readthedocs.org/projects/github-selenium/badge/?version=latest
            :target: https://github-selenium.readthedocs.io/en/latest/?badge=latest
            :alt: Documentation Status

    .. image:: https://pyup.io/repos/github/hwine/github_selenium/shield.svg
        :target: https://pyup.io/repos/github/hwine/github_selenium/
        :alt: Updates


Helper for 2FA login to GitHub


* Free software: MPL v2 license

..
    * Documentation: https://github-selenium.readthedocs.io.


Features
--------

Allows for automated browser login to GitHub accounts requiring 2FA, and
provides a Selenium_ web driver instance for further work. Uses a
headless Firefox instance driven by geckodriver_.

Prerequites
-----------

Outside of the dependencies which will be installed when you ``pip
install`` this package, you need:

    - Python (3 prefered, should work with 2)
    - Firefox 
    - Latest geckodriver_

Development dependencies are managed via pipenv_. Use ``pipenv install
--dev``
to build your virtual environment and install development dependencies.

* TODO

This works *just* enough to be useful on a couple of scripts. YMMV.

  * more docs!
  * lots! PR's & Issues welcome

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _selenium: http://www.seleniumhq.org/
.. _geckodriver: https://github.com/mozilla/geckodriver
.. _pipenv: https://github.com/pypa/pipenv
