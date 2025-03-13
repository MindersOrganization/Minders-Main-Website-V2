from django.db import models

class Magazine(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='magazines/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Volume(models.Model):
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE, related_name="volumes")
    title = models.CharField(max_length=255)
    release_date = models.DateField(auto_now=True)
    volume_cover_image = models.ImageField(upload_to='volumes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='articles/', null=True, blank=True)
    quote = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Contributor(models.Model):
    ROLE_CHOICES = [
        ('CW', 'Content Writing'),
        ('GD', 'Graphic Design'),
        ('QM', 'Quality Management'),
    ]

    name = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.role})"

class ArticleContributor(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="contributors")
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE, related_name="article_contributions")
    role = models.CharField(max_length=50, choices=Contributor.ROLE_CHOICES)

    class Meta:
        unique_together = ('article', 'contributor')
    def __str__(self):
        return f"{self.contributor.name} ({self.role}) {self.article.title}"