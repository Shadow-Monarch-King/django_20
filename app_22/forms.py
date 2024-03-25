from django import forms

class CreateAnimeForm(forms.Form):
    anime_name = forms.CharField()
    anime_episodes = forms.IntegerField()
    
    
    def clean_anime_name(self):
        cleaned_data = self.cleaned_data
        print('Cleaned Data: ',cleaned_data)
        anime_name = cleaned_data.get('anime_name')
        print("Anime Name: ", anime_name)
        return anime_name
    
    def clean_anime_episodes(self):
        cleaned_data = self.cleaned_data
        anime_episodes = cleaned_data.get('anime_episodes')
        return anime_episodes