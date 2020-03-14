from django.db import models
import datetime as d

# Model for the Bond data from the database
class Bond(models.Model):
    bond_id = models.AutoField(db_column='bond_id', primary_key=True, blank=True, null=False)
    investor_id = models.IntegerField(blank=True, null=True)
    bond_symbol = models.TextField(blank=True, null=True)
    no_shares = models.IntegerField(blank=True, null=True)
    purchase_price = models.FloatField(blank=True, null=True)
    current_price = models.FloatField(blank=True, null=True)
    purchase_date = models.TextField(blank=True, null=True)
    coupon = models.FloatField(blank=True, null=True)
    # Field renamed because it was a Python reserved word.
    yield_field = models.FloatField(db_column='yield', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Bond'
    #Method to calculate the earnings
    def calculate_earnings(self):
        return (self.current_price - self.purchase_price) * self.no_shares
        
    #Method to calculate the yearly earnings/loss rate.  
    def calculate_earnings_rate(self):
        return ((self.current_price - self.purchase_price)/self.purchase_price) 

    #Method to calculate percentage yield/loss for each of the bond.
    def calculate_percentage_yield(self):
        '''Calculate the date differences using Python's datetime module and convert into an integer.'''
        pur_date = (d.datetime.strptime(self.purchase_date, '%m/%d/%Y')).date()    
        today = (d.datetime.today()).date()
        return ((self.calculate_earnings_rate())/((today - pur_date).days/365))*100

# Model for the Investor data from the database
class Investor(models.Model):
    investor_id = models.AutoField(db_column='investor_id', primary_key=True, blank=True, null=False) 
    name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Investor'

# Model for the Stock data from the database   
class Stock(models.Model):
    stock_id = models.AutoField(db_column='stock_id', primary_key=True, blank=True, null=False)
    investor_id = models.IntegerField(blank=True, null=True)
    stock_symbol = models.TextField(blank=True, null=True)
    no_shares = models.IntegerField(blank=True, null=True)
    purchase_price = models.FloatField(blank=True, null=True)
    current_price = models.FloatField(blank=True, null=True)
    purchase_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Stock'

    #Method to calculate the earnings
    def calculate_earnings(self):
        return (self.current_price - self.purchase_price) * self.no_shares
        
    #Method to calculate the yearly earnings/loss rate.  
    def calculate_earnings_rate(self):
        return ((self.current_price - self.purchase_price)/self.purchase_price) 

    #Method to calculate percentage yield/loss for each of the stocks.
    def calculate_percentage_yield(self):
        '''Calculate the date differences using Python's datetime module and convert into an integer.'''
        pur_date = (d.datetime.strptime(self.purchase_date, '%m/%d/%Y')).date()    
        today = (d.datetime.today()).date()
        return ((self.calculate_earnings_rate())/((today - pur_date).days/365))*100