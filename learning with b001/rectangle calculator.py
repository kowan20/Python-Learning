def calculate_rectangle_area(length_cm, width_cm):
  area_sq_cm=length_cm*width_cm
  return area_sq_cm
#function to calculate area of rectangle in sq cm

def calculate():
  print('Welcome to my rectange calculater!')
  # main function to interact with user and start function
  while True:
    try:
      length_cm=float(input('What is the length in cm? '))
      width_cm=float(input('What is the width in cm? '))
      break #breaks loop when valid number is entered
    except ValueError:
      print('Please put in valid input')
    
#calculate area using function
  area_sq_cm = calculate_rectangle_area(length_cm, width_cm)

#print result
  print(f'The area of a rectange with the length of {length_cm}cm and width of {width_cm}cm is {area_sq_cm} square cm!')

if __name__ == '__main__':
  calculate()
