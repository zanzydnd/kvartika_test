from django.core.management import BaseCommand

from api.models import Post, Comment


class Command(BaseCommand):
    def handle(self, *args, **options):
        Post.objects.all().delete()
        Comment.objects.all().delete()

        posts = [Post(text=f"Text{index}", title=f"Title{index}") for index in range(1, 50)]
        Post.objects.bulk_create(posts)

        counter = 0
        comments = []
        for post in Post.objects.all():
            for i in range(20):
                counter += 1
                last_comment = Comment(username=f"user_{counter}", text=f"text_{counter}", post=post)
                comments.append(last_comment)

        Comment.objects.bulk_create(comments)

        comments = []
        for parent in Comment.objects.filter(answer_to=None):
            for i in range(3):
                counter += 1
                last_comment = Comment(username=f"user_{counter}", text=f"text_{counter}", answer_to=parent)
                comments.append(last_comment)

        Comment.objects.bulk_create(comments)

        comments_inner_1 = []
        for comment in comments:
            for i in range(3):
                counter += 1
                comments_inner_1.append(Comment(username=f"user_{counter}", text=f"text_{counter}", answer_to=comment))

        Comment.objects.bulk_create(comments_inner_1)

        comments_inner_2 = []
        for comment in comments_inner_1:
            for i in range(3):
                counter += 1
                comments_inner_2.append(Comment(username=f"user_{counter}", text=f"text_{counter}", answer_to=comment))

        Comment.objects.bulk_create(comments_inner_2)

        comments_inner_3 = []
        for comment in comments_inner_2:
            for i in range(3):
                counter += 1
                comments_inner_3.append(Comment(username=f"user_{counter}", text=f"text_{counter}", answer_to=comment))

        Comment.objects.bulk_create(comments_inner_3)

        comments_inner_4 = []
        for comment in comments_inner_3:
            for i in range(3):
                counter += 1
                comments_inner_4.append(Comment(username=f"user_{counter}", text=f"text_{counter}", answer_to=comment))

        Comment.objects.bulk_create(comments_inner_4)
