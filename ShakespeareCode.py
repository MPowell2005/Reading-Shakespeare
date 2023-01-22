'''
Author: Michael Powell
Narrative:
    This program allows the user to determine the number of times a particular word appears in a given text or texts through two different methods: Print and Graph.

Features:
    - Removes unnecessary characters in the word, such as certain punctuation characters.
    - The user can decide how many words they want to check.
    - The user can decide if they want to PRINT or GRAPH the number of appearances of a word in a text.
    - The user can decide what text they want to read in (must be a TXT file).
    - Play again option is available.
    - The user can insert multiple files to read in.

@author: mpowell23@gcds.net
'''

# Import Box
import plotly.graph_objects as go


def numberwords(file_handle, counts_dict):
    '''
        Summary:
        This function returns a list of all the number of appearances of a word in a text given a file_handle.
       
        Parameters:
        file_handle: The opened TXT file that the user has submitted to the program for reading purposes.
       
        Returns:
        counts_dict: The list of all the number of appearances of a word.
    '''
    
    
    # Defining local variables
    remove_characters = [',', '.', ' ', '?', '!', ';', '/', '-', "'", ':']                                  # A list that contains all of the characters removed in a word                                         
    
    # A for loop to fill out the dictionary, counts_dict
    for line in file_handle :                                                                               # Locate each line in the file
        line = line.rstrip()                                                                                # Strip the break below in the line
        line = line.strip()                                                                                 # Strip random spaces in the line
        line = line.lower()                                                                                 # Make each word a lower case word
        
        line = line.split()                                                                                 # Turn the line into a list with the elements as words
        
        for word in line :                                                                                  # Use a for loop to locate each word in the line
            word_list = list(word)                                                                          # Turn the word into a list with the elements as characters
            
            for character in word_list :                                                                    # Use a for loop to locate each character in the word
                if character in remove_characters :                                                         # If a character is in remove_characters for the word, pop the character out of the word_list
                    word_list.pop(word_list.index(character))
            
            word = ''.join(word_list)                                                                       # Turn the word back into a string after popping out all of the unnecessary characters

            if word not in counts_dict :                                                                    # If the word is not in the dictionary, set the key as the word and the value as 1.
                counts_dict[word] = 1
                
            else :                                                                                          # If the word is already in the dictionary, add one to value related to the key of the word
                counts_dict[word] = counts_dict[word] + 1
    
    return counts_dict                                                                                      # Return counts_dict


def main():
    
    # Description of the program
    print('This program allows the user to determine the number of times a particular word appears in a given text(s).')
    
    
    restart = 'yes'                                                                                         # Set 'restart' equal to yes to run the program
    while restart == 'yes' :                                                                                # While restart == 'yes', run the program
        
        # While True Loop 1: Asks the user how many files they want to read in
        while True :
            number_files = input('How many files do you want to read in?\n')
            
            try :
                number_files = int(number_files)
                
                if number_files > 0 :
                    break
                
                else :
                    print('Please insert an integer greater than zero for the number of files you want to read in.')
            
            except :
                print('Please insert an integer greater than zero for the number of files you want to read in.')
        
        
        counts_dict = dict()                                                                                # Define a dictionary called counts_dict
        counter_file = 1                                                                                    # Set a counter equal to 1
        while counter_file <= number_files :                                                                # A while loop to run through each file the user wants to read in
            
            # While True Loop 2: Ask the user for the file name
            while True :
                file_name = input('Insert the #' + str(counter_file) + ' file name that you want to read in.\n')
                
                try :
                    file_handle = open(file_name)
                    break
                
                except :
                    print('Please insert an appropriate file name that can be located in your files.')
                    continue        
        
            counts_dict = numberwords(file_handle, counts_dict)                                             # Use the 'numberwords' function to get a dictionary of the number of appearances of each word in the text
            
            counter_file = counter_file + 1                                                                 # Add 1 to the counter                                                  
        
        
        # Sorting the dictionary
        counts_sort = sorted(counts_dict.items(), key = lambda item: item[1], reverse = True)               # Use the 'sorted' method to sort the items of the dictionary from greatest to least as a list containing multiple tuples
    
        # Find the total amount of words in the text
        max_number_words = len(counts_sort)
        
        
        # While True Loop 3: Ask the user how many words they want to check
        while True :
            check_number_words = input('How many words do you want to check?\n')
            
            try :
                check_number_words = int(check_number_words)                                                # Make sure the number of words is an integer
                
                if check_number_words <= 0 or check_number_words > max_number_words :                       # Make sure the number of words is greater than zero and less than the total amount of words in the text
                    print('Please insert a number greater than 0 and less than the number of distinct words in the text, ' + str(max_number_words) + '.')
                    continue 
                
                else :
                    break
            
            except :
                print('Please insert a number greater than 0 and less than the number of distinct words in the text, ' + max_number_words + '.')


        # While True Loop 4: Ask the user how they want to display the number of appearances of each word in the text
        while True :
            method = input('Insert the method you want to use to display the number of particular words in the text.\n(1) Print\n(2) Graph\n')
            method = method.lower()
            method = method.strip()
            
            # If the method is either print or graph, break the loop
            if method == '1' or method == 'print' or method == '2' or method == 'graph' :
                break
            
            # If the method is anything else, repeat the loop
            else :
                print('Please insert the numbers corresponding to the method or the name of the method itself.')
                continue
        
        
        # Displaying the words using method 1: print
        if method == '1' or method == 'print' :
            counter = 0                                                                                     # Set a counter equal to zero                                                
            counts_condensed = []                                                                           # Create a list that will condense the number of appearances of a word to the user's choice
            
            print('The number of appearances of ' + str(check_number_words) + ' particular words is shown below.')
            while counter < check_number_words:                                                             # While the counter is less than the number of words the user wants to check, append each element from counts_sort to counts_condensed
                counts_condensed.append(counts_sort[counter])
                
                counter = counter + 1                                                                       # Add one to the counter through each loop
            
            for line in counts_condensed :                                                                  # Use a for loop to print each word along with its number of appearances
                print(line)
        
        
        # Displaying the words using method 2: graph
        else :
            x_list = []                                                                                     # Define a list that will act as the elements on the x-axis
            y_list = []                                                                                     # Define a list that will act as the elements on the y-axis
            
            # Define the elements in the x-axis
            counter_x = 0                                                                                   # Set a counter equal to zero
            while counter_x < check_number_words :                                                          # While the counter is less than the number of words the user wants to check:
                tuple_counts = counts_sort[counter_x]                                                       # Select the tuple for the index that is equal to the counter
                x_list.append(tuple_counts[0])                                                              # Append the tuple's 0th position (the word) into the x_list
                
                counter_x = counter_x + 1                                                                   # Add one to the counter
            
            # Define the elements in the y-axis
            counter_y = 0                                                                                   # Set a counter equal to zero              
            while counter_y < check_number_words :                                                          # While the counter is less than the number of words the user wants to check:
                tuple_counts = counts_sort[counter_y]                                                       # Select the tuple for the index that is equal to the counter
                y_list.append(tuple_counts[1])                                                              # Append the tuple's 1st position (the number of appearances) into the y_list
                
                counter_y = counter_y + 1                                                                   # Add one to the counter
            
            # Defining the 'trace'
            trace = go.Bar(                                                                                 # Use Plotly.go to create a class that consists of a bar graph, a x-axis dependent on x_list, a y-axis dependent on y_list, and the color red
                x = x_list,                                                                                                                
                y = y_list,                                                                                                               
                marker = dict(color = '#a31414')                                                                                               
                )
            
            data = [trace]                                                                                  # Let 'trace' be the data graphed
            
            # Graph layout
            layout = go.Layout(                                                                             # Use Plotly.go to create a layout for the graph consisting of a bar graph, a title, a x-axis title, and a y-axis title
                barmode = 'group', title = 'Number of Distinct Words in Text(s)',
                xaxis = dict(title = 'Word', ticklen = 5, zeroline= False),                                    
                yaxis = dict(title = 'Number of Appearances', ticklen = 5, zeroline = False)                                                        
                )
            
            plot = go.Figure(data = data, layout = layout)                                                  # Set a variable called 'plot' that consists of the layout class and the data class                                                                          
            
            # Plotting the graph
            print('The number of distinct words in the text is graphed on a separate HTML file.')
            plot.show()
        
        
        # Play again option
        while True :
            restart = input('Do you want to use the program again? (yes or no)\n')                          # Ask the user if they want to use the program again   
            restart = restart.lower()                                                                       # Make the input all lower case characters
            restart = restart.strip()                                                                       # Strip any spaces
            
            if restart == 'yes' or restart == 'y' :                                                         # If restart is equal to 'yes', break the while loop and repeat the program
                print('The program will restart.')
                break
            
            elif restart == 'no' or restart == 'n' :                                                        # If restart is equal to 'no,' break the while loop and end the program
                print('The program has ended.')
                break
            
            else :                                                                                          # If the user does not insert yes or no, repeat the while True loop
                print('Please insert an appropriate value.')
                continue 
    

if __name__ == '__main__':
    main()