# Generated by Django 3.1 on 2020-09-09 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalmodel',
            name='thumbnail',
            field=models.ImageField(default='default_thumbnail.jpg', upload_to='media/'),
        ),
    ]