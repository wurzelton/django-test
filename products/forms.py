from django import forms

from .models import Product

class ProductForm(forms.ModelForm): #a form especially for a created model

    #kann optional einzelne Felder von Model (gleicher Name) überschreiben und zusätzlich Infos mitgeben für rendering (hier placeholder, und dass kein label möchte)
    title       = forms.CharField(label='',
                                  widget=forms.TextInput(attrs={"placeholder": "your title"}))

    #email = forms.EmailField() #Kann auch neue Felder (die nicht in Model sind) hinzufügen. aber wird dann  nicht in DB gespeichert?

    # description = forms.CharField(
    #                             required=False,
    #                             widget=forms.Textarea(
    #                                 attrs={
    #                                     "palceholder": "Your description",
    #                                     "class": "new-class-name two",
    #                                     "id": "my-id-for-textarea",
    #                                     "rows":20,
    #                                     "cols": 120
    #                                 }
    #                             )) #Default für required ist True!
    # price       = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    # Zusätzliche Serverseitige Überprüfung von eingegebenem title (sagt muss sowohl CFE wie auch news enthalten)
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        if not "news" in title:
            raise forms.ValidationError("This is not a valid title")
        return title


    # #Zusätzliche Serverseitige Überprüfung von eingegebener Email-Adresse (nebst automatischer Überprüfung
    # #durch django da Feld als EmailField definiert hat), sagt Email muss mit edu enden!
    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("Not a valid email (must end with edu)")
    #     return email

class RawProductForm(forms.Form): #standard-django-form
    # --> form-fields von django (ähnlich zu model-fields, aber gibt keine TextField..)

    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "your title"}))  #schreibt beim rendern dann das Placeholder-Attribut ins input-Element
    description = forms.CharField(
                                required=False,
                                widget=forms.Textarea(
                                    attrs={
                                        "palceholder": "Your description",
                                        "class": "new-class-name two",
                                        "id": "my-id-for-textarea",
                                        "rows":20,
                                        "cols": 120
                                    }
                                )) #Default für required ist True!
    price       = forms.DecimalField(initial=199.99)