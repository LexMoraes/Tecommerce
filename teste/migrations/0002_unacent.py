from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("CREATE EXTENSION IF NOT EXISTS unaccent;")
    ]
