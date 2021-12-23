from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.naive_bayes import GaussianNB
import joblib

# Create your models here.



class Data(models.Model):
    radius_mean  = models.FloatField( null=True)
    texture_mean = models.FloatField( null=True)
    perimeter_mean  = models.FloatField( null=True)
    area_mean = models.FloatField( null=True)
    smoothness_mean = models.FloatField( null=True)
    compactness_mean = models.FloatField( null=True)
    concavity_mean = models.FloatField(null=True)
    concave_points_mean = models.FloatField( null=True)
    symmetry_mean = models.FloatField( null=True)
    fractal_dimension_mean = models.FloatField( null=True)
    radius_se = models.FloatField( null=True)
    texture_se = models.FloatField( null=True)
    perimeter_se = models.FloatField( null=True)
    area_se = models.FloatField( null=True)
    smoothness_se = models.FloatField( null=True)
    compactness_se = models.FloatField( null=True)
    concavity_se = models.FloatField( null=True)
    concave_points_se = models.FloatField( null=True)
    symmetry_se = models.FloatField( null=True)
    fractal_dimension_se = models.FloatField( null=True)
    radius_worst = models.FloatField( null=True)
    texture_worst = models.FloatField( null=True)
    perimeter_worst = models.FloatField( null=True)
    area_worst = models.FloatField( null=True)
    smoothness_worst = models.FloatField( null=True)
    smoothness_worst = models.FloatField( null=True)
    compactness_worst = models.FloatField( null=True)
    concavity_worst = models.FloatField( null=True)
    concave_points_worst = models.FloatField( null=True)
    symmetry_worst = models.FloatField( null=True)
    fractal_dimension_worst = models.FloatField( null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/cancer.joblib')
        self.predictions = ml_model.predict(
            [[self.radius_mean, self.texture_mean, self.perimeter_mean, self.area_mean, self.smoothness_mean,
              self.compactness_mean, self.concavity_mean, self.concave_points_mean,self.symmetry_mean,self.fractal_dimension_mean,
              self.radius_se,self.texture_se,self.perimeter_se,self.area_se,self.smoothness_se,self.compactness_se,self.concavity_se,self.concave_points_se, self.symmetry_se, self.fractal_dimension_se,self.radius_worst,self.texture_worst,self.perimeter_worst,
              self.area_worst,self.smoothness_worst, self.compactness_worst,self.concavity_worst,self.concave_points_worst, self.smoothness_worst, self.fractal_dimension_worst]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    
        
    