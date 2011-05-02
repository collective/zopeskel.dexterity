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
        # StringChoiceVar(
        #     'generate_custom_class',
        #     title='Add a custom class?',
        #     description='Create a custom class for the new type?',
        #     default='no',
        #     choices=('yes','no',),),
        var('global_allow', 'True/False: Globally addable ',
            default=True),
        var('allow_discussion', 'True/False: Allow discussion ',
            default=False),
        ]

    def pre(self, command, output_dir, vars):

        vars['contenttype_classname'] = vars['contenttype_name'].replace(" ", "")
        vars['contenttype_dottedname'] = vars['package_dotted_name'] + '.' + vars['contenttype_classname'].lower()
        vars['schema_name'] = vars['contenttype_classname'] + "Schema"
        vars['content_class_filename'] = vars['contenttype_name'].replace(" ", "-").lower()
        vars['types_xml_filename'] = vars['content_class_filename']
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

class DexterityView(DexteritySubTemplate):
    """
    A Content Type skeleton
    """

    _template_dir = 'templates/dexterity/view'
    summary = "A view skeleton for dexterity"

    vars = [
        var('view_name', 'Browser view name ', default='Example'),
        ]

    def pre(self, command, output_dir, vars):

        vars['view_filename'] = vars['view_name'].lower().replace(' ', '')
        vars['view_classname'] = vars['view_name'].replace(' ', '')


class ContentDexterityField(DexteritySubTemplate):
    """
    To add fields to schema
    """

    _template_dir = 'templates/dexterity/schemas'
    _insert_template = 'content/+content_class_filename+.py_insert'
    summary = "A schema field adder"
    sub_dir = 'content'
    marker_name = "Your Zope schema definitions here ..."

    # mapping of ATSchema types to zope.schema types
    typemap = {'boolean': 'schema.Bool',
               'textline': 'schema.TextLine',
               'richtext' : 'schema.Text',
               'text': 'schema.Text',
               'password' : 'schema.Password',
               'int' : 'schema.Int',
               'float' : 'schema.Float',
               'date' : 'schema.Date',
               'datetime' : 'schema.Datetime',
               'file' : 'namedfile.NamedFile',
               'blobfile' : 'namedfile.NamedBlobFile',
               'image' : 'namedfile.NamedImage',
               'blobimage' : 'namedfile.NamedBlobImage',
               'relation' : 'RelationChoice',
               'relationlist' : 'RelationList'
    }

    custom_widgets = {
        'richtext' : 'plone.app.z3cform.wysiwyg.WysiwygFieldWidget',
        'date' : 'collective.z3cform.datetimewidget.DateFieldWidget',
        'datetime' : 'collective.z3cform.datetimewidget.DatetimeFieldWidget'
    }

    vars = [
        var('content_class_filename',
            'What is the module (file)name of your content class?',
            default='example'),
        var('field_type',
            'What type of field do you want to use? Options are [%s]' % ', '.join(t for t in typemap),
            default='text'
        ),
        var('field_name',
            'What would you like to name this field?',
            default='newfield'),
        var('field_label',
            'What should be the label of this field (title)?',
            default='New Field'),
        var('field_desc',
            'What should be the description of this field (help text)?',
            default='Field description'),
        var('required',
            'Is this field required?',
            default='False')
        ]

    def check_vars(self, *args, **kwargs):
        """
        Overloading check_vars to print welcome message
        """
        return super(ContentDexterityField, self).check_vars(*args, **kwargs)

    def apply(self, command, output_dir, vars):
        """
        By-passing the base run so I can do multiple inserts
        with different marker names
        """

        (vars['namespace_package'],
         vars['namespace_package2'],
         vars['package']) = command.get_parent_namespace_packages()

        if vars['namespace_package2']:
            vars['package_dotted_name'] = "%s.%s.%s" % \
                (vars['namespace_package'],
                vars['namespace_package2'],
                vars['package'])
        else:
            vars['package_dotted_name'] = "%s.%s" % \
                (vars['namespace_package'],
                 vars['package'])

        self.pre(command, output_dir, vars)

        schema_insert_template = open(os.path.join(self.template_dir(), self._insert_template)).read()
        schema_insert = str(cheetah_template(schema_insert_template, vars))+"\n"
        command.insert_into_file(os.path.join(command.dest_dir(), self.sub_dir, '%s.py' % (vars['content_class_filename'])), self.marker_name, schema_insert)

    def run(self, command, output_dir, vars):
        self.apply(command, output_dir, vars)
        self.post(command, output_dir, vars)


    def pre(self, command, output_dir, vars):

        file = vars['content_class_filename'].lower().replace(' ', '')
        if file.endswith('.py'):
            file = os.path.splitext(file)[0]

        if vars['field_type'] in self.custom_widgets:
            vars['custom_widget'] = self.custom_widgets[vars['field_type']]
        else:
            vars['custom_widget'] = False

        vars['field_type'] = self.typemap[vars['field_type']]

        if vars['required'].lower() in ('false', 'true'):
            vars['required'] = vars['required'].lower().capitalize()
        else:
            vars['required'] = 'False'

        vars['field_name'] = vars['field_name'].replace(' ', '_').replace('-', '_')

        vars['content_class_filename'] = file


class BehaviorDexterityField(ContentDexterityField):

    sub_dir = 'behavior'
    behavior_marker_name = 'Your behavior property setters & getters here ...'

    def apply(self, command, output_dir, vars):
        super(BehaviorDexterityField, self).apply(command, output_dir, vars)

        schema_insert = ("    %(field_name)s =" + 
                        " context_property('%(field_name)s')\n") % vars
        command.insert_into_file(os.path.join(command.dest_dir(), self.sub_dir,
                                '%s.py' % (vars['content_class_filename'])),
                                self.behavior_marker_name, schema_insert)
