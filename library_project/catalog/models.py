from django.db import models

class Author(models.Model):
    # Dökümandaki senaryo: Eski alanlar
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    # Yeni alan (Migration ile veri buraya taşınacak)
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000)
    # ForeignKey: Migrasyonlar arası bağımlılık (Dependency) yaratır
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title