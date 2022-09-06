def format_name(f_name, l_name):
  f_name.title()  # same as:  f_name = f_name.title() - but replacing value instead of storing it in a new var
  l_name.title()  # same as:  l_name = l_name.title() - but replacing value instead of storing it in a new var
  
  full_name = f_name + ' ' + l_name
  return full_name  #  return -> returns an output and replaces the output fucntion where it's called below
                    #         -> the end of the function, nothing after it inside the function would work
first_name = input("What's your first name?:\n")
last_name = input("What's your last name?:\n")


print(format_name(first_name, last_name))
