Flake8 Copyright plugin
=======================

Checks for copyright notices in all python files. It runs a simple regular expression search for
strings like::

    Copyright 2014 <author>
    Copyright (C) 2014 <author>

``<author>`` can be anything unless you specify it with the ``copyright-author`` option (see below).

Install
-------

Install with pip::

    pip install flake8-copyright

Then, activate copyright checks in your flake8 configuration with::

    copyright-check = True
    # C errors are not selected by default, so add them to your selection
    select = E,F,W,C


Further options
---------------

copyright-min-file-size
    Minimum number of characters in a file before requiring a copyright notice. This is to avoid
    forcing yourself to add copyright notices to very small or empty files. Default: ``0``.

copyright-max-read-size
    Maximum number of characters to read from a file when looking for the copyright notice. This
    is necessary if a large docstring is at the top of the file, for example. Default: ``1024``

copyright-author
    Checks for a specific author in the copyright notice.

copyright-regexp
    If you're not happy with the regexp that is ran to look for copyright notices, you can change it
    with this option. Default: ``Copyright\s+(\(C\)\s+)?\d{4}([-,]\d{4})*\s+%(author)s``. ``%(author)s`` is
    replaced by the contents of ``copyright-author``.
