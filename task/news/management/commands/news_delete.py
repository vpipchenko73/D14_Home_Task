from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category, CategoryUser, PostCategory


class Command(BaseCommand):
    help = 'Удаление новостей в выбранной категории - формат команды <python manage.py news_delete <удаляемая категория>'  # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    # requires_migrations_checks = True  # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)

    def add_arguments(self, parser):
        parser.add_argument('cat_post', type=str)

    def handle(self, *args, **options): # здесь можете писать любой код, который выполнется при вызове вашей команды
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["cat_post"]}? yes/no->')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Удаление отменено'))
            return

        else:

           try:
              #post_delete = Category.get(name=options['category'])
              post_delete = Post.objects.filter(category_post__category_name=options['cat_post'])
              post_delete.delete()
              self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {options["cat_post"]}'))

           except Post.DoesNotExist:
              self.stdout.write(self.style.ERROR('Could not find category'))