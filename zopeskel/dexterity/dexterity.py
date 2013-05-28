import copy

from zopeskel.plone import BasicZope
from zopeskel.base import get_var
from zopeskel.base import EASY, EXPERT
from zopeskel.vars import BooleanVar

dex_vars = [
    BooleanVar('grokish',
        title='Grok-Based?',
        description="True/False: Use grok conventions to simplify coding?",
        modes=(EASY, EXPERT),
        default=True,
        help="""
Grok is a convention-over-configuration framework that simplifies
many aspects of the Zope Component Architecture. Grok makes it easier
to learn and use Dexterity, but it is not part of Plone's core.
""",
        ),
    ]


class Dexterity(BasicZope):
    _template_dir = 'templates/dexterity'
    summary = "A Dexterity-based product"
    help = """
"""
    category = "Plone Development"
    required_templates = ['basic_namespace']
    use_local_commands = True
    use_cheetah = True
    vars = copy.deepcopy(BasicZope.vars)
    vars += dex_vars
    get_var(vars, 'namespace_package').default = 'plone'
    get_var(vars, 'package').default = 'example'
    get_var(vars, 'description').default = 'Example Dexterity Product'
    get_var(vars, 'license_name').default = 'GPL version 2'
