from django import forms
from .models import City, Experiences

class ExperiencesForm(forms.ModelForm):
    class Meta:
        model = Experiences
        fields = ['eventname', 'eventdate', 'eventtime', 'address', 'eventdescription',
        'eventlink', 'city']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.all()



    #     eventname = models.CharField(max_length=100)
    # eventdate = models.DateField() 
    # eventtime = models.TimeField()
    # address = models.TextField(max_length=250)
    # eventdescription = models.TextField(max_length=500)
    # eventlink = models.CharField(max_length=100)
    # city = models.ForeignKey(City, on_delete=models.CASCADE)
