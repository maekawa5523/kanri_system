from django.db import models

# #customers
class Customers(models.Model):
    #社名
    name = models.CharField(max_length=50)
    #住所
    address = models.CharField(blank=True, null=True)
    #担当者
    tanto = models.CharField(blank=True, null=True)
    #メール
    mail = models.CharField(blank=True, null=True)
    #電話
    tel = models.CharField(blank=True, null=True)
    #携帯
    phone = models.CharField(blank=True, null=True)
    #初期値
    def __str__(self):
        return self.name

# #Lists
class Cases(models.Model):
    #顧客名
    customer = models.ForeignKey(Customers, on_delete=models.PROTECT, related_name='case')
    #見積依頼日
    mitsumori_request_date = models.DateField()
    #納期
    deadline = models.DateField(blank=True, null=True)
    #図面データ
    drawing_data = models.FileField(
        blank=True,
        null=True,
        upload_to=f'uploads/drawing/{customer}',
        verbose_name=f'{customer}{id}',
    )

# #contractors
class Contractors(models.Model):
    #社名
    name = models.CharField(blank=True, null=True)
    #住所
    address = models.CharField(blank=True, null=True)
    #担当者
    tanto = models.CharField(blank=True, null=True)
    #メール
    mail = models.CharField(blank=True, null=True)
    #電話
    tel = models.CharField(blank=True, null=True)
    #携帯
    phone = models.CharField(blank=True, null=True)
    #品質
    qualities = (
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('bad', 'Bad')
    )
    quality = models.CharField(choices=qualities, blank=True, null=True)
    #スキル
    sheet = models.BooleanField(default=False)
    cut = models.BooleanField(default=False)
    can = models.BooleanField(default=False)
    coat = models.BooleanField(default=False)
    #初期値
    def __str__(self):
        return self.name

# #products
class Products(models.Model):
    #ID
    num = models.ForeignKey(Cases, on_delete=models.PROTECT, related_name='product')
    #品名
    name = models.CharField(blank=True, null=True)
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
    material = models.CharField(choices=materials, blank=True, null=True)
    #処理
    surface = models.CharField(blank=True, null=True)
    #数量
    volume = models.CharField(blank=True, null=True)
    #外注先単価
    contractor_price = models.ForeignKey(Contractors, on_delete=models.PROTECT, related_name='price', blank=True, null=True)
    #確定単価
    agree_price = models.IntegerField(blank=True, null=True)
