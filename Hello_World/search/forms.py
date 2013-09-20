from django import forms
from Hello_World.services.models import ServiceType

SELECT_OPTIONS = ((0,'City'),(1,'Service'))

class SimpleForm(forms.Form):
	search = forms.CharField(required=False)
	select = forms.ChoiceField(required=False, choices = SELECT_OPTIONS)
	service_types = forms.MultipleChoiceField(required=False,
		widget=forms.CheckboxSelectMultiple)


	def __init__(self, *args, **kwargs):
		super(SimpleForm,self).__init__(*args,**kwargs)
		choices = []
		select = []

		service_types = ServiceType.objects.all()
		for i,s in enumerate(service_types):
			choices.append((i, s.name))
		self.fields['service_types'].choices = choices[1:]

		# self.fields['select'].queryset = ['Service','City']
		# print choices