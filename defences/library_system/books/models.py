from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField()
    author = models.CharField()  
    copys_avilable = models.IntegerField()
    loan_records = models.JSONField()
    
    def is_available(self):
        return self.copys_avilable > 0

    def get_most_recent_loan(self):
        moos_recent = self.loan_records[0]
        for date in self.loan_records:
            if date > moos_recent:
                moos_recent = date
        return moos_recent
    