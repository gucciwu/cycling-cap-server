from base.models import BaseModel
from django.db import models


class Location:
    lat = models.DecimalField(max_digits=19, decimal_places=10)
    lng = models.DecimalField(max_digits=19, decimal_places=10)
    elevation = models.DecimalField(max_digits=19, decimal_places=10)
    resolution = models.DecimalField(max_digits=19, decimal_places=10)


class Path(BaseModel):
    from_location = models.ForeignKey(Location,
                                      related_name="%(app_label)s_%(class)s_created_related",
                                      related_query_name="%(app_label)s_%(class)ss_created")
    to_location = models.ForeignKey(Location,
                                    related_name="%(app_label)s_%(class)s_created_related",
                                    related_query_name="%(app_label)s_%(class)ss_created")
    destination = models.IntegerField()
    locations_raw = models.TextField()
    locations = []

    class Meta:
        db_table = 'path'
