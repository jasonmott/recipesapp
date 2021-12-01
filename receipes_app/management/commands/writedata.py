from django.core.management.base import BaseCommand

class Command(BaseCommand):
    
    def handle(self,*args,**options):
        filepath = "/Users/admin/Python-Django-Class/final_project/receipes/receipes_app/management/commands/utilities/recepies.csv"
        data = open(filepath)
        for i in data:
            print(type(i))
            line = i.split(",")
            print(line)
            print(len(line))
            #title,ingredients = line
            #print(title)
            #for ingredient in ingredients:
                #print(ingredient)
