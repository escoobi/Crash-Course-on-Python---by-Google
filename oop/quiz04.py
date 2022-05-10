class Dog:
  years = 0
  def dog_years(self):
      years = self.years * 7
      return years
    
fido=Dog()
fido.years=3
print(fido.dog_years())