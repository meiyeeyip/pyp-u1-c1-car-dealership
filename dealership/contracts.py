class Contract(object):
    def __init__(self, vehicle, customer):
      self.customer = customer
      self.vehicle = vehicle

#vehicle.sale_price() + (I * monthly_payments * sale_price() / 100) - (discount if employee)
    
class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
        
    def total_value(self):
      if self.customer.is_employee() == True:
        return (self.vehicle.sale_price() + (self.vehicle.INTEREST * self.monthly_payments * self.vehicle.sale_price() / 100))* 0.9
      else:
        return (self.vehicle.sale_price() + (self.vehicle.INTEREST * self.monthly_payments * self.vehicle.sale_price() / 100))
                  
    def monthly_value(self):
        return self.total_value() / self.monthly_payments
          

                    
                    
class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
        
    def monthly_value(self):
      return self.total_value() / self.length_in_months
               
    
    def total_value(self):
      self.lease_multiplier = self.vehicle.sale_price() * (self.vehicle.LEAST_MULTIPLIER/self.length_in_months)
      if self.customer.is_employee() == True:
        return (self.vehicle.sale_price() + self.lease_multiplier)* 0.9
      else:
        return self.vehicle.sale_price() + self.lease_multiplier
        
                

      
