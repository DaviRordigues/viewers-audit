from django.db import models

class Audit(models.Model):
    id = models.AutoField(primary_key=True)
    source_app = models.CharField(max_length=100)
    audited_user = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audits'
