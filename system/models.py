from django.db import models


class Conference(models.Model):
    # Attributes for conference table
    conference_name = models.CharField(max_length=12)
    conference_initial_date = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    conference_end_date = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)

    # Define the output format
    def __str__(self):
        return self.conference_name

    # Custom table name
    class Meta:
        db_table = "conference"


class Event(models.Model):
    # Attributes for conference table
    event_name = models.CharField(max_length=8)
    event_room = models.CharField(max_length=6)
    event_initial_date = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    event_end_date = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    event_initial_time = models.TimeField(auto_now_add=False,auto_now=False,blank=True,null=True)
    event_end_time = models.TimeField(auto_now_add=False,auto_now=False,blank=True,null=True)
    event_speaker = models.CharField(max_length=9)
    conference = models.ForeignKey("Conference", to_field='id', on_delete=models.CASCADE)

    # Define the output format
    def __str__(self):
        return self.event_name

    # Custom table name
    class Meta:
        db_table = "event"
