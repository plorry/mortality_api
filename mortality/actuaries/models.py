from django.db import models

class Actuary(models.Model):
    region = models.ForeignKey('Region')
    year = models.IntegerField(blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    mx = models.DecimalField(decimal_places=5, max_digits=6)
    qx = models.DecimalField(decimal_places=5, max_digits=6)
    ax = models.DecimalField(decimal_places=2, max_digits=3)
    lx = models.IntegerField()
    dx = models.IntegerField()
    Lx = models.IntegerField()
    Tx = models.IntegerField()
    ex = models.DecimalField(decimal_places=2, max_digits=5)

    def __unicode__(self):
        return 'Region: {region} | Year: {year} | Age: {age}'.format(
            region=self.region.title,
            year=self.year,
            age=self.age
        )

class Region(models.Model):
    title = models.CharField(max_length=30)
    parent = models.ForeignKey('Region', related_name='children', blank=True, null=True)

    def __unicode__(self):
        return self.title
