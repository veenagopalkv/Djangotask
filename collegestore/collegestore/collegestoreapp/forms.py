import form as form
from django import forms
from django.utils.text import slugify
from .models import person,Department,Course

class personForm(forms.ModelForm):
    CHOICES = (('M', 'Male'), ('F', 'Female'))
    Purpose = (('1', 'Enquiry'), ('2', 'Place Order'), ('3', 'Return Order'))
    Materials=(('1','Debit Notebook'),('2','Pen'),('3','Exam Papers'))
    gender=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    purpose=forms.ChoiceField(choices=Purpose)
    material= forms.MultipleChoiceField(choices=Materials, widget=forms.CheckboxSelectMultiple)
    class Meta:

        model = person
        fields = ('name','slug','Date_of_birth','Age','gender','phone_number','mail_id','address','department','course','purpose','material')
        widget ={
                 'name':forms.TextInput(attrs={'class':'form-control'}),
                 'Date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
                 'Age':forms.NumberInput(attrs={'class':'form-control'}),
                 'phone_number':forms.IntegerField(),
                 'mail_id':forms.EmailField(),
                 'address':forms.Textarea(attrs={'rows':5})

                }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['course'].queryset=Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')


        def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)
class wikiform(forms.ModelForm):
    class Meta:
        model=Department
        fields=('name',)





