from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.code} - {self.title}"

class CourseInstance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='instances')
    year = models.PositiveIntegerField()
    semester = models.PositiveIntegerField()

    class Meta:
        unique_together = ['course', 'year', 'semester']

    def __str__(self):
        return f"{self.course.code} - {self.year} Sem {self.semester}"