# -=- encoding: utf-8 -=-
#
# Copyright (C) 2016 Savoir-faire Linux Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import re
import optparse

__version__ = '0.2.3'


# Temporary shim for flake8 2.x --> 3.x transition
# http://flake8.pycqa.org/en/latest/plugin-development/cross-compatibility.html#option-handling-on-flake8-2-and-3
def register_opt(parser, *args, **kwargs):
    try:
        # Flake8 3.x registration
        parser.add_option(*args, **kwargs)
    except (optparse.OptionError, TypeError):
        # Flake8 2.x registration
        parse_from_config = kwargs.pop('parse_from_config', False)
        kwargs.pop('comma_separated_list', False)
        kwargs.pop('normalize_paths', False)
        parser.add_option(*args, **kwargs)
        if parse_from_config:
            parser.config_options.append(args[-1].lstrip('-'))


class CopyrightChecker(object):
    name = 'flake8_copyright'
    version = __version__
    _code = 'C801'

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    @classmethod
    def add_options(cls, parser):
        register_opt(
            parser, '--copyright-check', action='store_true', parse_from_config=True,
            help="Checks for copyright notices in every file."
        )
        register_opt(
            parser, '--copyright-min-file-size', default=0, action='store', type='int',
            parse_from_config=True,
            help="Minimum number of characters in a file before requiring a copyright notice."
        )
        register_opt(
            parser, '--copyright-author', default='', action='store',
            parse_from_config=True,
            help="Checks for a specific author in the copyright notice."
        )
        register_opt(
            parser, '--copyright-regexp',
            default=r"Copyright\s+(\(C\)\s+)?\d{4}([-,]\d{4})*\s+%(author)s",
            action='store',
            parse_from_config=True,
            help="Changes the copyright regular expression to look for."
        )

    @classmethod
    def parse_options(cls, options):
        cls.copyright_check = options.copyright_check
        cls.copyright_min_file_size = options.copyright_min_file_size
        cls.copyright_author = options.copyright_author
        cls.copyright_regexp = options.copyright_regexp

    def run(self):
        if not self.copyright_check:
            return
        toread = max(1024, self.copyright_min_file_size)
        top_of_file = open(self.filename).read(toread)
        if len(top_of_file) < self.copyright_min_file_size:
            return

        author = self.copyright_author if self.copyright_author else r".*"
        re_copyright = re.compile(self.copyright_regexp % {'author': author}, re.IGNORECASE)
        if not re_copyright.search(top_of_file):
            yield 1, 1, "C801 Copyright notice not present.", type(self)
