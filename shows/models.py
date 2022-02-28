from django.db import models


class TVShow(models.Model):
    GENRE_CHOICE = (
        ("Drama", "Drama"),
        ("Romantic", "Romantic"),
        ("Action", "Action"),
        ("Historical", "Historical"),
        ("Anime", "Anime"),
        ("Comedy", "Comedy"),
        ("Horror", "Horror"),
    )
    title = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(upload_to="")
    quantity = models.PositiveIntegerField()
    genre = models.CharField(max_length=70, choices=GENRE_CHOICE)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    duration = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.title


class ShowComment(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    shows = models.ForeignKey(
        TVShow, on_delete=models.CASCADE, related_name="shows_comment"
    )
