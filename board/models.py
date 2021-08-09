from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

# Create your models here.
class Board(models.Model):
    Title = models.CharField(max_length=35)
    board_id = models.AutoField(primary_key = True)
    slug = models.SlugField()
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.board_id, self.Title, self.slug,
                                        self.user.id)



class InsideBoard(models.Model) :
    board_id = models.ForeignKey(Board, default=1, on_delete=models.CASCADE)
    title_id = models.IntegerField()
    SubTitle = models.CharField(max_length=35)
    CardBody = models.TextField(max_length=500)

    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {} - {}'.format(self.board_id, self.title_id, self.SubTitle,
                                        self.CardBody, self.board_id.board_id, self.board_id.slug, self.board_id.user.id, self.board_id.Title)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsideBoard
        fields = ('board_id', 'title_id', 'SubTitle', 'CardBody')

class BoardSerializer(serializers.ModelSerializer):

    tasks = TaskSerializer(many=True)

    class Meta:
        model = Board
        fields = ('title', 'board_id', 'slug')