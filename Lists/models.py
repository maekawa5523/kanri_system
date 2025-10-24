from django.db import models

#customers
class Customers(models.Model):
    #社名
    name = models.CharField(max_length=50)
    #初期値
    def __str__(self):
        return self.name

#Lists
class Cases(models.Model):
    #顧客名
    customer = models.ForeignKey(Customers, on_delete=models.PROTECT)
    #見積依頼日
    mitsumori_request_date = models.DateField()
    #納期
    deadline = models.DateField(blank=True, null=True)
    #図面データ
    drawing_data = models.FileField(
        upload_to=f'uploads/drawing/{customer}',
        verbose_name=f'{customer}{id}',
    )

#products
class Products(models.Model):
    #ID
    num = models.ForeignKey(Cases, on_delete=models.PROTECT)
    #図番
    drawing_num = models.CharField(max_length=50, db_index=True)
    #材質
    materials = (
        ('SUS304', 'SUS304'),
        ('SUS303', 'SUS303'),
        ('SUS316', 'SUS316'),
        ('SUS440C', 'SUS440C'),
        ('SS400', 'SS400'),
        ('S45C', 'S45C'),
        ('S50C', 'S50C'),
        ('SCM435', 'SCM435'),
        ('SUJ2', 'SUJ2'),
        ('SPHC', 'SPHC'),
        ('SPCC', 'SPCC')
    )
    #処理
    surface = models.CharField(blank=True, null=True)
    #数量
    volume = models.CharField(blank=True, null=True)

#contractors
class Contractors(models.Model):
    #社名
    name = models.CharField(max_length=50)
    #初期値
    def __str__(self):
        return self.name