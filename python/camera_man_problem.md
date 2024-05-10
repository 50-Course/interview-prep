A photography set consists of 𝑁 cells in a row, numbered from 1 to 𝑁 in order,
  and can be represented by a string 𝐶 of length 𝑁.
 
  Each cell 𝑖 is one of the following types (indicated by 𝐶ᵢ, the 𝑖th character
  of 𝐶):
    - If 𝐶ᵢ = "P", it is allowed to contain a photographer
    - If 𝐶ᵢ = "A", it is allowed to contain an actor
    - If 𝐶ᵢ = "B", it is allowed to contain a backdrop
    - If 𝐶ᵢ = ".", it must be left empty
 
  A photograph consists of a photographer, an actor, and a backdrop, such that
  each of them is placed in a valid cell, and such that the actor is between
  the photographer and the backdrop. Such a photograph is considered artistic
  if the distance between the photographer and the actor is between 𝑋 and 𝑌
  cells (inclusive), and the distance between the actor and the backdrop is
  also between 𝑋 and 𝑌 cells (inclusive). The distance between cells 𝑖 and 𝑗 is
  ∣ 𝑖 − 𝑗 ∣ (the absolute value of the difference between their indices).
   Determine the number of different artistic photographs which could potentially
  be taken at the set. Two photographs are considered different if they involve
  a different photographer cell, actor cell, and/or backdrop cell.
 
  Constraints
  1 ≤ 𝑁 ≤ 200
  1 ≤ 𝑋 ≤ 𝑌 ≤ 𝑁

  Sample test case #1
  N = 5
  C = APABA
  X = 1
  Y = 2
  Expected Return Value = 1

  Sample test case #2
  N = 5
  C = APABA
  X = 2
  Y = 3
  Expected Return Value = 0

  Sample test case #3
  N = 8
  C = .PBAAP.B
  X = 1
  Y = 3
  Expected Return Value = 3
