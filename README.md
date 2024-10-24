# Einstein's Riddle Solver
This is a solution to the famous **Einstein's Five Houses Puzzle** (also known as the **Zebra Puzzle**) using **backtracking** and **constraint satisfaction** in python.

## How It Works
The solver uses a systematic backtracking approach to find a valid solution that satisfies all 15 logical constraints of Einstein's riddle. It represents the houses as a 5x5 matrix where each row represents a house and each column represents a category (nationality, color, drink, smoke, and pet).

## Key Features
* **Constraint Satisfaction**: Implements 15 distinct constraints that define the puzzle rules
* **Backtracking Algorithm**: Uses recursive backtracking to:
  * Try different values for each house attribute
  * Check constraint violations
  * Backtrack when violations are found
* **Matrix Representation**: Utilizes a 5x5 matrix to represent:
  * 5 nationalities (Norwegian, Dane, Brit, German, Swede)
  * 5 colors (Red, Blue, Green, White, Yellow)
  * 5 drinks (Tea, Coffee, Milk, Beer, Water)
  * 5 smokes (Pall Mall, Blends, Dunhill, Blue Master, Prince)
  * 5 pets (Fish, Dogs, Birds, Cats, Horses)

## File Overview
* **einstein_solver.py**:
  * `solve()`: Main function that initializes and starts the solving process
  * `fillMatrix()`: Recursive function implementing the backtracking algorithm
  * `is_right()`: Validates all constraints for a given assignment
  * `find_minus()`: Helper function to find unassigned positions
  * 15 constraint functions (`one()` through `fifteen()`) checking specific puzzle rules

## Puzzle Constraints
* The Brit lives in the red house
* The Swede keeps dogs as pets
* The Dane drinks tea
* The green house is on the left of the white house
* The green house's owner drinks coffee
* The person who smokes Pall Mall rears birds
* The owner of the yellow house smokes Dunhill
* The man living in the center house drinks milk
* The Norwegian lives in the first house
* The man who smokes Blends lives next to the one who keeps cats
* The man who keeps horses lives next to the man who smokes Dunhill
* The owner who smokes BlueMaster drinks beer
* The German smokes Prince
* The Norwegian lives next to the blue house
* The man who smokes Blend has a neighbor who drinks water

## Example Output
```python
[norwegian, yellow, water, dunhills, cats]
[dane, blue, tea, blends, horses]
[brit, red, milk, pall_mills, birds]
[german, green, coffee, princes, fish]
[swede, white, beer, bluemasters, dogs]

The German keeps the fish. He lives in the fourth house!
```

## How to Use
1. Clone the repository
2. Run the solver:
```bash
python einstein_solver.py
```
3. The program will output the complete solution matrix and identify who owns the fish

## Authors
* Davis Carson
* Emily Dogbatse
