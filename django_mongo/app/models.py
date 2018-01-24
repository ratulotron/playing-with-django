from django.db import models
from django.contrib.postgres.fields import JSONField
from mongoengine import Document, EmbeddedDocument, fields

from rest_framework import serializers, viewsets, response



class ToolInput(EmbeddedDocument):
    name = fields.StringField(required=True)
    value = fields.DynamicField(required=True)


class Tool(Document):
    label = fields.StringField(required=True)
    description = fields.StringField(required=True, null=True)
    inputs = fields.ListField(
        fields.EmbeddedDocumentField(ToolInput)
        )

# list = [
#     {
#         "label": "cd",
#         "description": "Change Directories",
#         "inputs": [{
#             "name": "source",
#             "value": "/path/"
#         }]
#     },
#     {
#         "label": "mv",
#         "description": "Move Directories",
#         "inputs": [{
#             "name": "source",
#             "value": "/path/"
#         },
#         {
#             "name": "destination",
#             "value": "/path/"
#         }]
#     }
# ]

# class Tool(models.Model):
#     label = models.CharField(
#         max_length=1024,
#         null=True,
#         blank=True
#     )

#     description = models.TextField(null=True, blank=True)


# class ToolInput(models.Model):
#     tool = models.ForeignKey(
#         Tool,
#         related_name="inputs",
#         on_delete=models.CASCADE
#     )

#     name = models.CharField(
#         max_length=1024,
#         null=True,
#         blank=True
#     )

#     value = JSONField(null=True, blank=True)