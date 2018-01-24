from django.db import models
from mongoengine import Document, EmbeddedDocument, fields


# class Todolist(models.Model):
#     name = fields.StringField(required=True)
#     user = models.ForeignKey(User, related_name="todolists", on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
# class Todo(EmbeddedDocument):
#     todolist = fields.StringField(required=True)
#     description = fields.StringField(required=True, null=True)
#
#     def __str__(self):
#         return self.text

