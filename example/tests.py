from django.test import TestCase

from example import models as example_models


class SnowflakeTest(TestCase):

    def test_connect(self):
        data = example_models.Reason.objects.using('snowflake_analytics').all()
        
        print(data.count())
        
        self.assertEqual(1, 0)
