# Generated by Django 4.0 on 2021-12-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='budget',
            new_name='area_mean',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='gross',
            new_name='area_worst',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='imdb_score',
            new_name='compactness_mean',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='profit_percent',
            new_name='compactness_worst',
        ),
        migrations.RemoveField(
            model_name='data',
            name='actor_1_name',
        ),
        migrations.RemoveField(
            model_name='data',
            name='actor_2_name',
        ),
        migrations.RemoveField(
            model_name='data',
            name='actor_3_name',
        ),
        migrations.RemoveField(
            model_name='data',
            name='director_name',
        ),
        migrations.RemoveField(
            model_name='data',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='data',
            name='movie_title',
        ),
        migrations.AddField(
            model_name='data',
            name='concave_points_mean',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='concave_points_worst',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='concavity_mean',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='concavity_worst',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='fractal_dimension_worst',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='perimeter_mean',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='perimeter_worst',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='radius_mean',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='smoothness_mean',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='smoothness_worst',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='symmetry_worst',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='texture_mean',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='texture_worst',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
