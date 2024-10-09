# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from users.models import UserAcc


class Discount(models.Model):
    discountid = models.IntegerField(db_column='discountId', primary_key=True)  # Field name made lowercase.
    furnitureid = models.ForeignKey('Furniture', models.DO_NOTHING, db_column='furnitureId')  # Field name made lowercase.
    discountprice = models.DecimalField(db_column='discountPrice', max_digits=8, decimal_places=2)  # Field name made lowercase.
    discountreason = models.TextField(db_column='discountReason')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    resolveddate = models.DateTimeField(db_column='resolvedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'discount'


class Furniture(models.Model):
    furnitureid = models.AutoField(db_column='furnitureId', primary_key=True)  # Field name made lowercase.
    furniturecategory = models.CharField(db_column='furnitureCategory', max_length=20)  # Field name made lowercase.
    furnituretype = models.CharField(db_column='furnitureType', max_length=20)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discountedprice = models.DecimalField(db_column='discountedPrice', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=20)
    locationid = models.ForeignKey('Location', models.DO_NOTHING, db_column='locationId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'furniture'


class Location(models.Model):
    locationid = models.IntegerField(db_column='locationId', primary_key=True)  # Field name made lowercase.
    locationtype = models.CharField(db_column='locationType', max_length=15)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'
        db_table_comment = 'Location table contains details of the store/warehouse locations'


class Ticket(models.Model):
    ticketid = models.AutoField(db_column='ticketId', primary_key=True)  # Field name made lowercase.
    furnitureid = models.ForeignKey(Furniture, models.DO_NOTHING, db_column='furnitureId')  # Field name made lowercase.
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='locationId')  # Field name made lowercase.
    issuestatus = models.CharField(db_column='issueStatus', max_length=25)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate', auto_now_add=True)  # Field name made lowercase.
    reportedby = models.CharField(db_column='reportedBy', max_length=100, null=True)  # Field name made lowercase.
    issuedescription = models.TextField(db_column='issueDescription')  # Field name made lowercase.
    resolutiontype = models.CharField(db_column='resolutionType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    resolutioncomments = models.TextField(db_column='resolutionComments', blank=True, null=True)  # Field name made lowercase.
    resolutiondate = models.DateTimeField(db_column='resolutionDate', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='lastUpdatedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ticket'
        db_table_comment = 'Table to maintain all the ticket data'


class Ticketimage(models.Model):
    imageid = models.AutoField(db_column='imageId', primary_key=True)  # Field name made lowercase.
    ticketid = models.ForeignKey(Ticket, models.DO_NOTHING, db_column='ticketId')  # Field name made lowercase.
    imagecontent = models.TextField(db_column='imageContent')  # Field name made lowercase.
    uploaddate = models.DateTimeField(db_column='uploadDate')  # Field name made lowercase.
    uploadedby = models.ForeignKey('User', models.DO_NOTHING, db_column='uploadedBy')  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticketImage'


class User(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=45)
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='userType', max_length=10)  # Field name made lowercase.
    status = models.CharField(max_length=1)
    phone = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
