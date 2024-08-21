from django.contrib import admin
from movies.models import Movie

@admin.register(Movie)
class AdminMovie(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'formatted_realese_date', 'resume')

    def formatted_realese_date(self, obj):
        if obj.realese_date:
        # Usa strftime para formatar a data como uma string
         return obj.realese_date.strftime('%d/%m/%Y')
        return 'Sem data'
    
    # Define o campo pelo qual a lista pode ser ordenada
    formatted_realese_date.admin_order_field = 'realese_date'
    # Define o nome que será exibido na coluna
    formatted_realese_date.short_description = 'Release Date'

