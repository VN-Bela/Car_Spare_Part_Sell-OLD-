from django.contrib.auth import  get_user_model

#from auth.models import User
# check unique username and email
User=get_user_model()

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "id":"user-password"
            }
        )

    )
    # def clean(self):
    #      username=self.cleaned_data.get("username")
    #      password=self.cleaned_data.get("password")
    # check username
    def clean_username(self):
        username=self.cleaned_data.get("username")
        qs=User.objects.filter(username_iexact=username)
        if not qs.exits():
            raise forms.ValidationError("This is invalid User")
        return username



