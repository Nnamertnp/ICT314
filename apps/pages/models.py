from django.db import models

# Create your models here.

class Product(models.Model):
    ANIMAL_TYPES = (
        ('dog', 'สุนัข'),
        ('cat', 'แมว'),
        ('both', 'ทั้งสุนัขและแมว'),
    )
    
    PRODUCT_TYPES = (
        ('shampoo', 'แชมพู'),
        ('conditioner', 'ครีมนวด'),
        ('soap', 'สบู่'),
        ('perfume', 'น้ำหอม'),
        ('set', 'เซ็ตอาบน้ำ'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField('ชื่อสินค้า', max_length=200)
    product_type = models.CharField('ประเภทสินค้า', max_length=50, choices=PRODUCT_TYPES)
    animal_type = models.CharField('สำหรับสัตว์', max_length=50, choices=ANIMAL_TYPES)
    price = models.DecimalField('ราคา', max_digits=10, decimal_places=2)
    description = models.TextField('รายละเอียด')
    benefits = models.TextField('คุณประโยชน์')
    ingredients = models.TextField('ส่วนประกอบ')
    size = models.CharField('ขนาด', max_length=50)
    stock = models.IntegerField('จำนวนในสต๊อก')
    image_url = models.URLField('URL รูปภาพ', max_length=500, help_text='ลิงก์รูปภาพสินค้า')
    is_featured = models.BooleanField('สินค้าแนะนำ', default=False)
    created_at = models.DateTimeField('วันที่เพิ่ม', auto_now_add=True)
    updated_at = models.DateTimeField('วันที่อัพเดท', auto_now=True)

    class Meta:
        verbose_name = 'สินค้าอาบน้ำสัตว์เลี้ยง'
        verbose_name_plural = 'สินค้าอาบน้ำสัตว์เลี้ยง'

    def __str__(self):
        return f"{self.name} ({self.get_product_type_display()} สำหรับ{self.get_animal_type_display()})"
