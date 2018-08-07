from base.models import BaseModel
from django.db import models


class Dictionary(BaseModel):
    dict_entry = models.CharField(max_length=200, null=False)
    dict_key = models.CharField(max_length=200, null=False)
    dict_value = models.CharField(max_length=500, null=False)
    dict_remark = models.CharField(max_length=500, null=True, default="")

    def __str__(self):
        return self.dict_entry + '/' + self.dict_key

    class Meta:
        db_table = 'dictionary'




