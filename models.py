from django.db import models

class TimeZone(models.Model):
    id = models.CharField(
        _('time zone'),
        max_length=100,
        primary_key=True
    )
    name = models.CharField(
        _('name'),
        max_length=100
    )

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = _('time zone')
        verbose_name_plural = _('time zones')
        db_table = "sbt_node_time_zones"
