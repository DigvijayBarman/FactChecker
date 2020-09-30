from django import forms
from .models import *
class EntryForm(forms.ModelForm):
	class Meta:
		model = News
		fields = ['entry']
		labels = {
			'entry': '',
		}
		widgets = {
			'entry': forms.TextInput(attrs={'class': 'search_box', 'placeholder': 'Find the truth now!'})
		}