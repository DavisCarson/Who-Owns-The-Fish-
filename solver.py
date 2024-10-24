# Davis Carson &  Emily Dogbatse

# Intialize blank spaces
blank = -1


"""
Create groups of all varibles and assign number values to use in search

nationality, color, drink, smoke, animal/pet
"""
# Group variables
nationality, color, drinks, smokes, pet = range(5)

# Define values for each group
norwegian, dane, brit, german, swede = range(5)
red, blue, green, white, yellow = range(5)
tea, coffee, milk, beer, water = range(5)
pall_mills, blends, dunhills, bluemasters, princes = range(5)
fish, dogs, birds, cats, horses = range(5)


"""
Constraints for the problem

The Brit lives in the red house
The Dane drinks tea
The Swede keeps dogs as pets
The German smokes Prince
The green house is on the left of the white house
The green house’s owner drinks coffee
The person who smokes Pall Mall rears birds
The owner of the yellow house smokes Dunhill
The man living in the center house drinks milk
The Norwegian lives in the first house
The man who smokes blends lives next to the one who keeps cats
The man who keeps horses lives next to the man who smokes Dunhill
The owner who smokes BlueMaster drinks beer
The Norwegian lives next to the blue house
The man who smokes blend has a neighbor who drinks water
"""

# Check if the British person lives in the red house
def one(houses):
  for house in houses:
    if house[nationality] != blank and house[color] != blank:
        if (house[nationality] == brit and house[color] != red) or (house[nationality] != brit and house[color] == red):
            return False
  return True


# Check if the Danish person lives in the green house 
def two(houses):
  for house in houses:
    if house[nationality] != blank and house[drinks] != blank:
        if (house[nationality] == dane and house[drinks] != tea) or (house[nationality] != dane and house[drinks] == tea):
            return False
  return True


# Check if the German smokes Princes
def three(houses):
  for house in houses:
    if house[nationality] != blank and house[smokes] != blank:
        if (house[nationality] == german and house[smokes] != princes) or (house[nationality] != german and house[smokes] == princes):
            return False
  return True


# Check if the Swede has a dog
def four(houses):
  for house in houses:
    if house[nationality] != blank and house[pet] != blank:
        if (house[nationality] == swede and house[pet] != dogs) or (house[nationality] != swede and house[pet] == dogs):
            return False
  return True


# Check if the green house left of and next to the white house
def five(houses):
  is_green = any(house[color] == green for house in houses)
  is_white = any(house[color] == white for house in houses)

  if is_green and is_white:
    for i in range(len(houses) - 1):
        if houses[i][color] == green and houses[i + 1][color] != white:
            return False
  return True


# Check if the green house person drinks coffee
def six(houses):
  for house in houses:
    if house[color] != blank and house[drinks] != blank:
        if (house[color] == green and house[drinks] != coffee) or (house[color] != green and house[drinks] == coffee):
            return False
  return True


# Check if someone that smokes Pall Malls has birds
def seven(houses):
  for house in houses:
    if house[smokes] != blank and house[pet] != blank:
        if (house[smokes] == pall_mills and house[pet] != birds) or (house[smokes] != pall_mills and house[pet] == birds):
            return False
  return True


# Check if person in the yellow house smokes Dunhills
def eight(houses):
  for house in houses:
    if house[color] != blank and house[smokes] != blank:
        if (house[color] == yellow and house[smokes] != dunhills) or (house[color] != yellow and house[smokes] == dunhills):
            return False
  return True


# Check if the man living in the middle house drinks milk
def nine(houses):
  for i, house in enumerate(houses):
    if house[drinks] != blank:
        if (i == 2 and house[drinks] != milk) or (i != 2 and house[drinks] == milk):
            return False
  return True

# The Norwegian lives in the first house
def ten(houses):
  for i, house in enumerate(houses):
    if house[nationality] != blank:
        if (house[nationality] == norwegian and i != 0) or (house[nationality] != norwegian and i == 0):
            return False
  return True


# Check who smokes Bluemasters drinks beer
def eleven(houses):
  for house in houses:
    if house[smokes] != blank and house[drinks] != blank:
        if (house[smokes] == bluemasters and house[drinks] != beer) or (house[smokes] != bluemasters and house[drinks] == beer):
            return False
  return True


# Check if the person that smokes Blends is next to the one who has cats
def twelve(houses):
  blends_location = next((i for i, house in enumerate(houses) if house[smokes] == blends), None)
  cats_location = next((i for i, house in enumerate(houses) if house[pet] == cats), None)

  if blends_location is not None and cats_location is not None:
    return abs(blends_location - cats_location) == 1

  return True


# Check if the person that has horses is next to the one who smokes Dunhills
def thirteen(houses):
  horses_location = next((i for i, house in enumerate(houses) if house[pet] == horses), None)
  dunhills_location = next((i for i, house in enumerate(houses) if house[smokes] == dunhills), None)

  if horses_location is not None and dunhills_location is not None:
    return abs(horses_location - dunhills_location) == 1

  return True


# Check if the Norwegian is next to the blue house
def fourteen(houses):
      norwegian_location = next((i for i, house in enumerate(houses) if house[nationality] == norwegian), None)
      blue_location = next((i for i, house in enumerate(houses) if house[color] == blue), None)

      if norwegian_location is not None and blue_location is not None:
          return abs(norwegian_location - blue_location) == 1

      return True


# the man who smokes Blends has a neighbor that drinks water
def fifteen(houses):
      for i, house in enumerate(houses):
          if house[smokes] == blends:
              if i > 0 and houses[i - 1][drinks] == water:
                  return True
              if i < len(houses) - 1 and houses[i + 1][drinks] == water:
                  return True
              return False
      return True  

# Check if assigning houses is correct
# row column index
def is_right(houses, r, c, value):
    for i in range(5):
        if houses[i][c] == value:
            return False

    houses[r][c] = value

    constraints = (
        one(houses)
        and two(houses)
        and three(houses)
        and four(houses)
        and five(houses)
        and six(houses)
        and seven(houses)
        and eight(houses)
        and nine(houses)
        and ten(houses)
        and eleven(houses)
        and twelve(houses)
        and thirteen(houses)
        and fourteen(houses)
        and fifteen(houses)
    )

    houses[r][c] = blank

    return constraints

def find_minus(houses):

   for i in range(5):
       for j in range(5):
           if houses[i][j] == blank:
               return i, j
   return None

# fill in matrix, print out solution
def fillMatrix(houses):
  index = find_minus(houses)
  if index is None:
      for j, house in enumerate(houses):
          print(f'{house}')

      # print the conclusion
      for house in houses:
          if house[pet] == fish:
              country = house[nationality]
              if country == german:
                  print("The german keeps the fish. He lives in the fourth house!")
              else:
                  print('Thee puzzle was not completed correctly. The German (4th row/house) is supposed to have the fish.')
              break  # Exit the loop after locating the fish
      exit(0)
  #house, varible
  h, v = index
  for i in range(5):
      if is_right(houses, h, v, i):
          houses[h][v] = i
          fillMatrix(houses)
          houses[h][v] = blank

def solve():
  # Initialize the grid
  houses = [[blank] * 5 for _ in range(5)]

  # fill the matrix
  fillMatrix(houses)

if __name__ == '__main__':
  solve()
