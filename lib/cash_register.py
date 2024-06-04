#!/usr/bin/env python3
import math 

class CashRegister:
  def __init__(self, discount = 0 ):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last = 0

  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, discount):
    self._discount = discount
  
  @property
  def total(self):
    return self._total

  @total.setter
  def total(self, total):
    self._total = total

  def add_item(self, title, price, quantity = 1):
    
    
    total = self.total 
    new_total = total + (price*quantity)
    self.total = new_total
    self.last = price*quantity

    for i in range(quantity):
      self.items.append(title)    
  
  def apply_discount(self):
    if self.discount == 0:
      print('There is no discount to apply.')
    else:
      discount_dollars = self.total * (self.discount/100)
      self.total = self.total - discount_dollars
      print(f'After the discount, the total comes to ${math.ceil(self.total)}.')

  def void_last_transaction(self):
    print(self.last)
    self.total = self.total - self.last
