from django.db import models

class Topic(models.Model):
    keyword = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.keyword

# Create the default topic instance if it doesn't exist
def get_default_topic():
    default_topic, created = Topic.objects.get_or_create(keyword="No topic")
    return default_topic.id


class Joke(models.Model):
    question = models.TextField()
    answer = models.TextField()
    topic = models.ForeignKey(Topic, default=get_default_topic, on_delete=models.SET(get_default_topic))

    def __str__(self):
        return self.question
    
