from django.core.management.base import BaseCommand, CommandError
from ibmtest.models import Course

class Command(BaseCommand):

    def handle(self, *args, **options):
        course_1 = Course(name="Adel's test course", description="Test course for IBM Django course")
        course_1.save()