from django import forms

class CreateAnimeForm(forms.Form):
    anime_name = forms.CharField()
    anime_episodes = forms.IntegerField()
    
    
    # def clean_anime_name(self):
    #     cleaned_data = self.cleaned_data
    #     # print('Cleaned Data: ',cleaned_data)
    #     anime_name = cleaned_data.get('anime_name')
    #     # print("Anime Name: ", anime_name)
    #     if anime_name.lower().strip() == 'naruto':
    #         raise forms.ValidationError('This Name is already taken')
    #     return anime_name
    
    def clean_anime_episodes(self):
        cleaned_data = self.cleaned_data
        anime_episodes = cleaned_data.get('anime_episodes')
        return anime_episodes
    
    def clean(self):#============================================cleaned All Data 
        cleaned_data = self.cleaned_data
        # print('all data:',cleaned_data)
        return cleaned_data
    
    def clean(self):
        cleaned_data = self.cleaned_data
        anime_name = cleaned_data.get('anime_name')
        anime_episodes = cleaned_data.get('anime_episodes')
        if anime_name.lower().strip() == 'naruto':
           self.add_error('anime_name','This Title is already Taken')
        if anime_episodes == 1:
            self.add_error('anime_episodes','Episode is already Done')
        return cleaned_data