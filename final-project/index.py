"""
route method of flask with '/add' as the page to list all recipes
"""
from flask import render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()

        """dictionary of list and sqlite."""
        lang1='zh'
        lang2='ru'
        lang3='ja'

        recipes = [dict(title=row[0],
                        author=row[1], 
                        ingredient=row[2],
                        time=row[3], 
                        skill=row[4], 
                        description=row[5],
                        url=row[6],
                        t_title=self.translate(row[0],lang1),
                        t_author=self.translate(row[1],lang1),
                        t_ingredient=self.translate(row[2],lang1),
                        t_time=self.translate(row[3],lang1),
                        t_skill=self.translate(row[4],lang1),
                        t_description=self.translate(row[5],lang1),
                        t2_title=self.translate(row[0],lang2),
                        t2_author=self.translate(row[1],lang2),
                        t2_ingredient=self.translate(row[2],lang2),
                        t2_time=self.translate(row[3],lang2),
                        t2_skill=self.translate(row[4],lang2),
                        t2_description=self.translate(row[5],lang2),
                        t3_title=self.translate(row[0],lang3),
                        t3_author=self.translate(row[1],lang3),
                        t3_ingredient=self.translate(row[2],lang3),
                        t3_time=self.translate(row[3],lang3),
                        t3_skill=self.translate(row[4],lang3),
                        t3_description=self.translate(row[5],lang3)) for row in model.select()]

        return render_template('index.html', rps=recipes)

    def translate(self,text,target):

        from google.cloud import translate
        translate_client = translate.Client()
        
        result = translate_client.translate(text,target_language=target)

        return result['translatedText']

        

