from django.db import models


class Reason(models.Model):
    R_REASON_SK = models.IntegerField(primary_key=True)
    R_REASON_ID = models.CharField(max_length=16)
    R_REASON_DESC = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'SNOWFLAKE_SAMPLE_DATA.TPCDS_SF100TCL.REASON'
