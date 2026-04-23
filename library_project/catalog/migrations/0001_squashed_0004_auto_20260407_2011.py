from django.db import migrations, models
import django.db.models.deletion

# PDF'de anlatılan RunPython fonksiyonunu buraya, sınıfın dışına alıyoruz [cite: 539]
def combine_names(apps, schema_editor):
    # Modellerin tarihsel sürümlerini kullanıyoruz [cite: 242, 248]
    Author = apps.get_model("catalog", "Author")
    for author in Author.objects.all():
        # first_name ve last_name'i birleştirip yeni name alanına yazıyoruz [cite: 243, 244]
        author.name = f"{author.first_name} {author.last_name}"
        author.save()

class Migration(migrations.Migration):
    # Bu dosyanın hangi dosyaların yerini aldığını belirtir [cite: 317]
    replaces = [
        ('catalog', '0001_initial'),
        ('catalog', '0002_book'),
        ('catalog', '0003_author_name'),
        ('catalog', '0004_auto_20260407_2011'),
    ]

    initial = True # Bu uygulamanın ilk geçişi olduğunu belirtir [cite: 138]

    dependencies = [
    ]

    operations = [
        # 1. Yazarlar tablosu oluşturuluyor [cite: 408]
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        # 2. Kitaplar tablosu ve Yazar ilişkisi (ForeignKey) oluşturuluyor [cite: 79, 408]
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(max_length=1000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Author')),
            ],
        ),
        # 3. Veri taşıma işlemi (Data Migration) [cite: 231, 259]
        # Hatalı olan sayısal yolu sildik, doğrudan fonksiyon adını verdik
        migrations.RunPython(
            code=combine_names,
            reverse_code=migrations.RunPython.noop, # Geri çevrilebilir olması için [cite: 577]
        ),
    ]