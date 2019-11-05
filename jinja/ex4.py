# -*- coding: utf-8 -*-
from jinja2 import Environment, PackageLoader, select_autoescape


package_loader = PackageLoader('testapp', 'templates')
env = Environment(
    loader=package_loader,
    autoescape=select_autoescape(
        enabled_extensions=['html', 'xml'],
        default_for_string=True
    )
)

template = env.get_template('variable.html')

print(template.render(name='Rahul'))