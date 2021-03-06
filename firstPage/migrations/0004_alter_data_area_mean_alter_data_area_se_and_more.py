# Generated by Django 4.0 on 2022-01-08 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0003_data_area_se_data_compactness_se_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='area_mean',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='area_se',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='area_worst',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='compactness_mean',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='compactness_se',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='compactness_worst',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='concave_points_mean',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='concave_points_se',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='concave_points_worst',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='concavity_mean',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='concavity_se',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='concavity_worst',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='fractal_dimension_mean',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='fractal_dimension_se',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='fractal_dimension_worst',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='perimeter_mean',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='perimeter_se',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='perimeter_worst',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='radius_mean',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='radius_se',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='radius_worst',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='smoothness_mean',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='smoothness_se',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='smoothness_worst',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='symmetry_mean',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='symmetry_se',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='symmetry_worst',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='texture_mean',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='texture_se',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='texture_worst',
            field=models.FloatField(null=True),
        ),
    ]
