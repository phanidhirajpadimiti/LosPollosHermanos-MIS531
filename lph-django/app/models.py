from django.db import models

# Create your models here.
class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    OrderDate = models.DateField()
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False  # Set to False to indicate that Django doesn't manage this table
        db_table = 'orders'  # Specify the actual table name in the database

    def __str__(self):
        return f"Order {self.OrderID}"
    
class Reservation(models.Model):
    RESERVATIONID = models.AutoField(primary_key=True)
    RESERVATIONTIME = models.DateTimeField()
    PARTYSIZE = models.IntegerField()
    PREFERENCE = models.CharField(max_length=255)
    CONTACTPHONE = models.CharField(max_length=15)

    class Meta:
        managed = False  # Set to False to indicate that Django doesn't manage this table
        db_table = 'reservations'  # Specify the actual table name in the database

    def __str__(self):
        return f"Reservation {self.RESERVATIONID}"

class Employee(models.Model):
    EMPLOYEEID = models.AutoField(primary_key=True)
    POSITION = models.CharField(max_length=50, null=True)
    SALARY = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    FIRSTNAME = models.CharField(max_length=50, null=True)
    LASTNAME = models.CharField(max_length=50, null=True)

    class Meta:
        managed = False  # Set to False to indicate that Django doesn't manage this table
        db_table = 'employees'  # Specify the actual table name in the database

    def __str__(self):
        return f"Employee {self.EMPLOYEEID}: {self.FIRSTNAME} {self.LASTNAME}"
    
class Item(models.Model):
    ITEMID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=100)
    PRICE = models.DecimalField(max_digits=10, decimal_places=2)
    DESCRIPTION = models.CharField(max_length=255)

    class Meta:
        managed = False  # Set to False to indicate that Django doesn't manage this table
        db_table = 'menu_items'  # Specify the actual table name in the database

    def __str__(self):
        return f"Item {self.ITEMID}: {self.NAME}"

class Promotion(models.Model):
    PROMOTIONID = models.AutoField(primary_key=True)
    PROMOTIONNAME = models.CharField(max_length=100)
    DESCRIPTION = models.CharField(max_length=255)
    DISCOUNT = models.DecimalField(max_digits=10, decimal_places=2)
    STARTDATE = models.DateField()
    ENDDATE = models.DateField()

    class Meta:
        managed = False  # Set to False to indicate that Django doesn't manage this table
        db_table = 'promotions'  # Specify the actual table name in the database
    
    def __str__(self):
        return f"Item {self.PROMOTIONID}: {self.PROMOTIONNAME}"
