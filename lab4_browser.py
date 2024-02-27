#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program:simulate the navigation buttons present on a web brower
#
# Author:Bamijoko Seyi
# Collaborators/references:
#----------------------------------------------------

def getAction():
    '''
    Gets the action requested by the user 
    Inputs: none
    Returns: valid str
    '''
    correct_input = False
    valid_input = ['=', '<','>','q']
    while correct_input == False:
        user_input = input("Enter = to enter a URL, < to go back, > to go forward, q to quit:")
        if user_input in valid_input:
            correct_input = True
        else:
            print("Invalid entry.")
    return user_input

def goToNewSite(current, pages):
    '''
    Adds a new website to the list of webpages
    Inputs: current index and reference to the list 
    Returns: the current index of the webpages in main
    '''   
    new_website = input("URL: ")
    if current == (len(pages) - 1):
        pages.append(new_website)
        current += 1
    elif current < (len(pages) - 1):
        del pages[(current + 1):(len(pages))]
        pages.append(new_website)
        current = pages.index(new_website)
        #pages[current] = new_website
        #print(pages)
        #pages.RemoveRange((current + 1, (len(pages) - 1)))
       
    return current

    
def goBack(current, pages):
    '''
    Checks if the user can go back to the previous website
    Inputs: Current and pages
    Returns: the current index of the webpages
    '''    
    if current <= 0:
        print("Cannot go back.")
    else:
        current -= 1
    return current 

def goForward(current, pages):
    '''
    Checks if the user can go back the website he was on before
    Inputs: Current and pages
    Returns: the current index of the webpages
    '''    
    if current >= len(pages) -1:
        print("Cannot go forward.")
    else:
        current += 1
    return current     


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    