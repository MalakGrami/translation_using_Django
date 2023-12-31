from rest_framework.views import APIView
from rest_framework.response import Response
from translate import Translator
from .models import Article

class ArticleListView(APIView):
    def get(self, request):
        # Retrieve all articles from the database
        articles = Article.objects.all()

        # Translate the articles to the desired languages
        target_languages = ['fr', 'en', 'de']  # French, English, and German languages
        translated_articles = []
        for article in articles:
            translated_data = {}
            for language in target_languages:
                translator = Translator(to_lang=language)
                translated_title = translator.translate(article.title)
                translated_content = translator.translate(article.content)
                translated_data[language] = {
                    'title': translated_title,
                    'content': translated_content,
                }
            translated_articles.append(translated_data)

        # Return the translated articles as JSON response
        return Response({'articles': translated_articles})
