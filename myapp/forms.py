# -*- coding: utf-8 -*-
from dataclasses import field
from distutils.command.upload import upload
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from .models import myModel

class MessageForm(forms.ModelForm): 
    #text_input = forms.CharField(required=False)
    blood_smear_image = forms.ImageField(required=False)
    class Meta:
        model = myModel
        fields = ('image',)

    '''
    textarea = forms.CharField(
        widget = forms.Textarea(),
        required=False,
    )

    radio_buttons = forms.ChoiceField(
        choices = (
            ('option_one', "Option one is this and that be sure to include why it's great"), 
            ('option_two', "Option two can is something else and selecting it will deselect option one")
        ),
        widget = forms.RadioSelect,
        initial = 'option_two',
        required=False,
    )

    checkboxes = forms.MultipleChoiceField(
        choices = (
            ('option_one', "Option one is this and that be sure to include why it's great"), 
            ('option_two', 'Option two can also be checked and included in form results'),
            ('option_three', 'Option three can yes, you guessed it also be checked and included in form results')
        ),
        initial = 'option_one',
        widget = forms.CheckboxSelectMultiple,
        help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
        required=False,
    )

    appended_text = forms.CharField(
        help_text = "Here's more help text",
        required=False,
    )

    prepended_text = forms.CharField(required=False,)

    prepended_text_two = forms.CharField(required=False,)

    multicolon_select = forms.MultipleChoiceField(
        choices = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
        required=False,
    )
    '''

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        #Field('text_input', css_class='input-xlarge'),
        Field('blood_smear_image', css_class = 'img-fluid'),
        #Field('textarea', rows="3", css_class='input-xlarge'),
        #'radio_buttons',
        #Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
        #AppendedText('appended_text', '.00'),
        #PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">', active=True),
        #PrependedText('prepended_text_two', '@'),
        #'multicolon_select',
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )
