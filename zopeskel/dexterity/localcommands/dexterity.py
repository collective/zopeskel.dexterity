import os
from zopeskel.base import var, StringChoiceVar
from zopeskel.localcommands import ZopeSkelLocalTemplate

from Cheetah.Template import Template as cheetah_template

class DexteritySubTemplate(ZopeSkelLocalTemplate):
    use_cheetah = True
    parent_templates = ['dexterity']

class DexterityContent(DexteritySubTemplate):
    """
    A Content Type skeleton
    """

    _template_dir = 'templates/dexterity/content'
    summary = "A content type skeleton"

    vars = [
        var('contenttype_name', 'Content type name ', default='Example Type'),
        var('contenttype_description', 'Content type description ',
            default='Description of the Example Type'),
        var('folderish', 'True/False: Content type is Folderish ',
            default=False),
        var('global_allow', 'True/False: Globally addable ',
            default=True),
        var('allow_discussion', 'True/False: Allow discussion ',
            default=False),
        ]

    def pre(self, command, output_dir, vars):

        vars['contenttype_classname'] = vars['contenttype_name'].replace(" ", "")
        vars['contenttype_dottedname'] = vars['package_dotted_name'] + '.' + vars['contenttype_classname'].lower()
        vars['schema_name'] = vars['contenttype_classname'] + "Schema"
        vars['content_class_filename'] = vars['contenttype_name'].replace(" ", "_").lower()
        vars['types_xml_filename'] = vars['contenttype_dottedname']
        vars['interface_name'] = "I" + vars['contenttype_classname']
        vars['add_permission_name'] = vars['package_dotted_name'] + ': Add ' + vars['contenttype_name']

class DexterityBehavior(DexteritySubTemplate):
    """
    A Content Type skeleton
    """

    _template_dir = 'templates/dexterity/behavior'
    summary = "A behavior skeleton"

    vars = [
        var('behavior_name', 'Behavior name ', default='Example Behavior'),
        var('behavior_description', 'Behavior description ',
            default='Description of the Example behavior'),

        ]

    def pre(self, command, output_dir, vars):

        vars['behavior_classname'] = vars['behavior_name'].replace(" ", "")
        vars['behavior_interfacename'] = 'I' + vars['behavior_classname']
        vars['behavior_filename'] = vars['behavior_classname'].lower()

        vars['behavior_short_dottedadapter'] = '.' + vars['behavior_filename'] + '.' + vars['behavior_classname']
        vars['behavior_short_dottedinterface'] = '.' + vars['behavior_filename'] + '.' + vars['behavior_interfacename']

