#forms.py
import re
from django import forms
from django.contrib.auth.models import User
from .models import Event
from django.utils.translation import ugettext_lazy as _


class RegistrationForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Verify password"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

class PostEvent(forms.ModelForm):
    CATEGORIES = (
        ('le', 'Leisure'),
        ('pe', 'Personal'),
        ('ed', 'Educational'),
        ('pr', 'Professional'),
    )
    event_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Event name'}))
    event_location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Location'}))
    event_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD HH:mm'}))
    event_category = forms.ChoiceField(label='', choices=CATEGORIES, widget=forms.Select(attrs={'class':'form-control selectpicker'}))
    event_description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}))
    class Meta:
        model = Event
        fields = ('event_name', 'event_date', 'event_location', 'event_description', 'event_category')
class FilterByForm(forms.Form):
    FILTERS = (
    ('no', 'None'),
    ('le', 'Leisure'),
    ('pe', 'Personal'),
    ('ed', 'Educational'),
    ('pr', 'Professional'))
    filterby = forms.ChoiceField(choices=FILTERS, required=False)

    def __init__(self, *args, **kwargs):
        super(FilterByForm, self).__init__(*args, **kwargs)
        self.fields['filterby'].label = ""
        self.fields['filterby'].widget.attrs.update({'class' : 'form-control'})
        self.fields['filterby'].widget.attrs.update({'onchange': 'this.form.submit();'})

class OrderByForm(forms.Form):
    ORDERINGS = (
    ('up', 'Upcoming to furthest'),
    ('fu', 'Furthest to upcoming'),
    ('po', 'Most popular'))
    orderby = forms.ChoiceField(choices=ORDERINGS, required=False)

    def __init__(self, *args, **kwargs):
        super(OrderByForm, self).__init__(*args, **kwargs)
        self.fields['orderby'].label = ""
        self.fields['orderby'].widget.attrs.update({'class' : 'form-control'})
        self.fields['orderby'].widget.attrs.update({'onchange': 'this.form.submit();'})
