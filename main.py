print('Welcome to the Band Name Generator!')

city = input("What's the name of the city you grew up in?\n")

pets = input("What's your pet's name?\n")

band_name = city + ' ' + pets

print(f'Your band name could be {band_name}')
likeness = input('Did you like it? Y or N?').lower()
if likeness == 'y':
  print(f'The band {band_name} is awesome!!!'
else:
  print(f'Then you dont have a band name yet!')
