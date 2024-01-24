import random
import os
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for file_no in range(35):
    with open(f'Question_Paper_{file_no + 1}.txt', 'w') as questionPaper:
        with open(f'Answer_Paper_{file_no + 1}.txt', 'w') as answerPaper:
            questionPaper.write('\nName: \nDate: \nClass: \n')
            questionPaper.write(' ' * 20 + 'Random Quiz Generator - Question Paper - ' + str(file_no + 1))



            for question_no in range(50):
                # store all the states in a list variable
                states=list(capitals.keys())
                # randomly change the position of each state within the list
                random.shuffle(states)
                # Store the correct answer i.e capital of selected state
                state_q=states[0]
                correct_ans=capitals[states[0]]
                # to get all 3 wrong answer options,
                # first get capitals of all 50 states
                capitals_list=list(capitals.values())
                # then remove the correct answer from this list
                capitals_list.remove(correct_ans)
                # using random.sample, fetch 3 values from above 49 wrong capitals
                captial_wrong=random.sample(capitals_list,3)
                # finally get the 4 options in a list: 3 wrong + 1 correct answer
                all_options=[correct_ans]+captial_wrong
                # shuffle the position of all 4 options
                random.shuffle(all_options)
                # Display the question statement " what is capital of state?"
                #questionPaper.write(f'What is the capital of state {state_q}?')
                questionPaper.write(f'\n\n#{question_no+1} What is the capital of state {state_q}?\n\n')
                options=['A. ','B. ','C. ','D. ']
                for optionNum in range(4):
            # display the options in question paper file
                    questionPaper.write(' '*4 + f'{options[optionNum]+all_options[optionNum]}\n')

            # display the answer for each question in answer paper file.
                answerPaper.write(f'{question_no+1}. {options[all_options.index(correct_ans)][0]}\n')
