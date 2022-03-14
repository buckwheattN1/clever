from tabnanny import verbose
from django.conf import settings
from django.db import models
from django.utils import timezone
from order.models import Material, IntegerRangeField
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField

from decimal import Decimal


class Stock(models.Model):

    length = IntegerRangeField(min_value=50, max_value=2800, null=True)
    width = IntegerRangeField(min_value=50, max_value=2070, null=True)
    material = models.ForeignKey(Material, null=False, on_delete=models.CASCADE, related_name="stocks")

    def __str__(self):
        return "#{} {}x{} {}".format(self.id, self.length, self.width, self.material)


class Cutter(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(blank=False, null=True)
    toBuy = models.IntegerField(blank=True, null=True, default=0)
    forSharpening = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.name


class Contractor(models.Model):
    name = models.CharField(max_length=200)
    nip = models.CharField(max_length=13)
    regon = models.CharField(max_length=13, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    #address = AddressField(on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Kontrahent"
        verbose_name_plural = "Kontrahenci"

    def __str__(self):
        return self.name


class GoodsReceivedNote(models.Model):
    TOCHECK = 0
    CHECKED = 1
    STATUS = (
        (TOCHECK, 'Niezatwierdzone'),
        (CHECKED, 'Zatwierdzone')
    )
    title = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, blank=False)
    documentID = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=STATUS, default=TOCHECK)
    
    def save(self, *args, **kwargs):
        dt = timezone.now()
        counter = GoodsReceivedNote.objects.filter(date__month=dt.month).count()
        self.title = "PZ/{0:0=3d}/{1}".format(counter, dt.strftime("%m/%y"))
        super(GoodsReceivedNote, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.documentID, self.contractor)
    

class GRNMaterial(models.Model):

    VAT_8 = 0
    VAT_23 = 1
    VAT = (
        (VAT_8, '8%'),
        (VAT_23, '23%')
    )
    
    grn = models.ForeignKey(GoodsReceivedNote, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    area = models.DecimalField(default=Decimal('0.000'), decimal_places=4, blank=False, max_digits=10)
    quantity = models.IntegerField(blank=True, null=True)
    price_net = models.DecimalField(default=Decimal('0.00'), decimal_places=2, blank=False, max_digits=10)
    vat = models.SmallIntegerField(choices=VAT, default=VAT_23)

    def save(self, *args, **kwargs):

        self.quantity = self.area / self.material.material_area
        super(GRNMaterial, self).save(*args, **kwargs)
    
    def price_gross(self):
        vat = 0
        if self.vat == self.VAT_8:
            vat = 0.08
        if self.vat == self.VAT_23:
            vat = 0.23
        return float(self.price_net) + (float(self.price_net) * float(vat))

    def total_price(self):
        
        return float(self.area) * self.price_gross()

    def sum_total_price(self):

        grn = GoodsReceivedNote.objects.get(id=self.id)

        total_price = 0

        for material in grn.grnmaterial_set.all():
            result = float(material.area) * material.price_gross
            total_price += result
        return total_price


class Cash(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(default=Decimal('0.00'), decimal_places=2, blank=False, max_digits=10)
    
    class Meta:
        verbose_name = "Kasa"
        verbose_name_plural = "Kasy"

    def __str__(self):
        return "{} - {} {}".format(self.title, self.user.first_name, self.user.last_name)