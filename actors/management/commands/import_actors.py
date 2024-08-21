from django.core.management.base import BaseCommand
import csv
from actors.models import Actor

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_csv', type = str, help = 'News Actors')

    def handle(self, *args, **options):
        file_csv = options['file_csv']


        with open(file_csv, 'r', encoding= 'utf-8') as arquivo:

            file = csv.DictReader(arquivo)
            for row in file:
                name = row['name']
                age = int(row['age'])
                nationality = row['nationality']
                self.stdout.write(self.style.NOTICE(name))
                Actor.objects.create(name = name, age = age, nationality = nationality,)  
        self.stdout.write(self.style.SUCCESS("Atores cadastrados com sucesso"))      

            