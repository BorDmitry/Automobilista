from .models import Car
from django.forms import ModelForm


class SalesForm(ModelForm):
    class Meta:          #  поля элементов формы
        model = Car
        fields = ['owner', 'title', 'power', 'fuel', 'year', 'featured_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # наследуем от родителя - ModelForm

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
