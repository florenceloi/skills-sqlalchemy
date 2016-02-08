"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
a1 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
a2 = Model.query.filter(Model.name == 'Corvette',
                        Model.brand_name == 'Chevrolet').all()

# Get all models that are older than 1960.
a3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
a4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
a5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
a6 = Brand.query.filter(Brand.founded == 1903,
                        Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
a7 = Brand.query.filter((Brand.discontinued.isnot(None)) |
                        (Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
a8 = Model.query.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.filter(Model.year == year).all()

    result = ""

    for model in models:
        result += "Model: %s | Brand: %s | HQ: %s\n" % (
            model.name,
            model.brand_name,
            model.brand.headquarters)

    print result


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = Brand.query.all()

    result = ""

    for brand in brands:
        result += "\n" + brand.name + ":\n"
        for model in brand.models:
            result += "\t%s\n" % model.name

    print result


# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    '''Takes in a string and returns a list of objects that are brands whose
    name contains or is equal to the input string.'''

    brands = Brand.query.filter(Brand.name.like("%" + mystr + "%")).all()

    return brands


def get_models_between(start_year, end_year):
    '''Takes in start and end years (as integers) and returns a list of objects
    that are models with years that fall between the start and end years.'''

    models = Model.query.filter(Model.year > start_year,
                                Model.year < end_year).all()

    return models


# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# Answer: It is a query class that contains all of the objects found in the
#         Brand class with the name Ford.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# Answer: An association table connects two tables that have a many to many relationship.
#         The association table allows this relationship to break down to a many to one and 
#         then a one to many relationship. Association tables do not store any other
#         interesting information besides the association.