from django.db import models


class Journey(models.Model):
    last_processed_at = models.DateTimeField(null=True, db_index=True)
