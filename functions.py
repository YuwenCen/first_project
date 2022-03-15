"""A collection of function for doing my project."""

import pandas as pd

def sorting_hats():
    '''
    distribute new students to different houses according to their personalities
    
    Returns
    -------
    output_houses : string 
        string informing users about which house they got in 
    '''

    chat = True
    # make sure users input correct spelling of personality. If so, then return house; 
    # otherwise, keep looping until correct spelling.  
    while chat:
        input_user = input('choose the word that best describe you Bravery, Intelligence, Empathy, Ambition: ')
    
        pos_pers = ['Bravery', 'Intelligence', 'Empathy', 'Ambition']
        pos_house = ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']
    
        if input_user in pos_pers:
            # find the corresponding house according to the position of personality. (Bravery-Gryffindor) 
            house = pos_house[pos_pers.index(input_user)]
            output_houses = 'Congratuations! You are in House ' + house + '!'
            return output_houses
            chat = False 
        
        else:
            output_houses = 'As a wizard, be careful with your spells. '
            return output_houses

        
def financial():
    '''
    ask if the user want to apply for the financial aid
    
    Returns
    -------
    chat_2 : boolean 
        boolean that determines whether the chat ends
    fee : int
        costs of tuition after user applies the financial aid
    '''
                    
    chat_2 = True
    while chat_2:
        num_finan = input('How much financial aid you want to apply for (0-30000): ')
        num = int(num_finan)
        
        # make sure the input is within the range, then returning fee
        if num>=1 and num<=30000:
            fee = 30000 - num
            chat_2 = False
        
        else: 
            fee = 'Error.'
            chat_2 = False
            
    return chat_2, fee


def financial_aid():
    '''
    inform the user about the total tuition he/she needs to pay based on the financial aid
    
    Returns
    -------
    fee : int
        costs of tuition 
    '''
    fee = 30000 
    chat = True
    while chat:
        finan = input('Do you want to apply for a financial aid (yes or no): ')

        if finan == 'yes':
            # reuse the variables defined and processed in the previous function.
            chat, fee = financial()
            print('Ok! The total tuition fee will be: ' + str(fee))
            
        elif finan == 'no': 
            print('Ok! The total tuition fee will be $30000')
            chat = False
        
        else: 
            print('Be careful with your spelling.')
            chat = True 
    
    return fee

def summary_fee():
    '''
    Produce a table to more explicitly inform the user about the fee he/she needs to pay. 
    
    Returns
    -------
    df : Dataframe 
        a dataset with all types of fee and total fee
    '''
    fee = financial_aid()
    d1 = {'type_of_fee': 'tuition', 'cost_$': fee}
    d2 = {'type_of_fee': 'housing', 'cost_$': 10000}
    d3 = {'type_of_fee': 'dining', 'cost_$': 3000}
    d4 = {'type_of_fee': 'book_and_supplies', 'cost_$': 1000}
    
    df = pd.DataFrame([d1, d2, d3, d4], [0, 1, 2, 3])
    
    # to calculate the sum of cost (the cost_$ column)
    total = df['cost_$'].sum()
    
    # add a new row indicating the total fee
    df.loc['total'] = pd.Series(df['cost_$'].sum(), index=['cost_$'])
    
    print("Here's the summary for the fee for the 2022-2023 academic year:")
    
    return df












