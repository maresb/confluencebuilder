# -*- coding: utf-8 -*-
"""
:copyright: Copyright 2021 Sphinx Confluence Builder Contributors (AUTHORS)
:license: BSD-2-Clause (LICENSE)
"""

from jinja2 import Template
import pkgutil
import os


def generate_storage_format_search(builder, docname, f):
    """
    generate the search content for the builder into the provided file

    This call can be used to generate a search document for a provided builder.
    This generated search is then included in the list of documents to be
    published to an instance.

    Args:
        builder: the builder
        docname: the docname
        f: the file to write to
    """

    space_name = builder.config.confluence_space_name

    # fetch raw template data
    search_template = os.path.join('templates', 'search.html')
    template_data = pkgutil.get_data(__name__, search_template)

    # process the template with the generated index
    t = Template(template_data.decode('utf-8'))
    output = t.render(space=space_name)
    f.write(output)