from django.db import migrations

def combine_names(apps, schema_editor):
    # Modeli doğrudan import etmiyoruz, tarihsel sürümü alıyoruz [cite: 186, 247]
    Author = apps.get_model("catalog", "Author")
    for author in Author.objects.all():
        author.name = f"{author.first_name} {author.last_name}" [cite: 252]
        author.save() [cite: 253]

class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0003_author_name'), # Bir önceki geçişe bağımlı [cite: 256]
    ]

    operations = [
        migrations.RunPython(combine_names), # Yazdığımız fonksiyonu çalıştırır [cite: 259]
    ]