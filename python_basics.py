
# W1D1 - PYTHON BASICS
# - Syntax
# - what about indentation?
# - code blocks?

# javascript function
# function addition(params) {
    # stuff goes here
    # return 5 + 6 
# }
def addition():
    # stuff goes here
    return 5 + 6

    # for(let i = 0; i<10: i++) {

    # }

    for i in range(0, 10,1):
        # stuff goes here
        pass

        # Data types

        # ### PRIMATIVE
        # numbers
        # js let x = 10                 
        my_number = 10  
        another_number = 30                                                                                                                                                                 
        
        
        #strings
        my_string = "hello world"
        # console.log(my_string)
        print(my_string)
        upper_name = my_name.upper()
        print( f'Hello my name is { upper_name }')
        
        
        
        # boolean 
        is_tired = False
        is_hungry = True
        
        # lists / JS arrays
        jims_cohort = ['Criag', 'Sam', 'Wiji']
        print(jims_cohort) #prints the whole list
        print(jims_cohort[0]) #prints the item in the index

        jims_cohort.append('Dante')
        print(jims_cohort)

        print(' --->',jims_cohort[:2])

        print(len(jims_cohort))


        # js objects / dictionary
        my_dict = {"first_name": "Jimbo", "last_name": "Reeder"}
        print(my_dict['first_name'])


        # tuple 
        my_tuple = "a",'f','b'
        another_tuple = ()
        print(type(my_tuple))

        my_dict['age'] = 25
        print(my_dict)
        my_dict(['age']) = 35


        # Conditionals
        # Loops
        # Built in methods
        # Functions