from pyDatalog import pyDatalog
pyDatalog.clear()
pyDatalog.create_terms('triangleEquilateral,triangleIsocele,triangleRectangle,'
                       'deuxCotesEgaux,troisCotes,'
                       'angleDroit,troisCotesEgaux,X')
triangleEquilateral(X) <= troisCotes(X) & troisCotesEgaux(X)
triangleRectangle(X) <= troisCotes(X) & angleDroit(X)
triangleIsocele(X) <= troisCotes(X) & deuxCotesEgaux(X)

# rectangle
+troisCotes("rectangle1")
+angleDroit("rectangle1")

# isocele
+troisCotes("isocele1")
+deuxCotesEgaux("isocele1")

# equilateal
+troisCotes("equilateral1")
+troisCotesEgaux("equilateral1")

# ask for triangle rectangle
query = "triangleRectangle(X)"

answers = pyDatalog.ask(query).answers
print(answers)

# ask for triangle isocele
query = "triangleEquilateral(X)"

answers = pyDatalog.ask(query).answers
print(answers)

# ask for triangle equilateral
query = "triangleIsocele(X)"

answers = pyDatalog.ask(query).answers
print(answers)
