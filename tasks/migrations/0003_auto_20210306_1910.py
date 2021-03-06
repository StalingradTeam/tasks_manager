from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20210306_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoitem',
            options={'ordering': ('-priority',), 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AddField(
            model_name='todoitem',
            name='pri_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]