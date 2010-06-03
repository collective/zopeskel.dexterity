import copy

from zopeskel.plone import BasicZope
from zopeskel.base import get_var
from zopeskel.base import var

class Dexterity(BasicZope):
    _template_dir = 'templates/dexterity'
    summary = "A dexterity-based product"
    help = """
"""
    category = "Plone Development"
    required_templates = ['basic_namespace']
    use_local_commands = True
    use_cheetah = True
    vars = copy.deepcopy(BasicZope.vars)
    get_var(vars, 'namespace_package').default = 'plone'
    get_var(vars, 'package').default = 'example'
    get_var(vars, 'description').default = 'Example Dexterity Product'


