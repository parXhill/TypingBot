*** What it is *** 

This is a bot that can open a browser and type out lines that have been set on the website typeforme.com

The website allows users to create a task in which a set of lines have to be typed out, without copying and pasting. 

Task setters can set additional lines for mistakes made, and also create interruption screens that flash a message while a user is typing. 

It presents the task setter with a report at the end that reveals the number of mistakes made and what they were, and graphs the typing speed throughout the task. 

*** What it does *** 

1. The bot uses Selenium to open up the browser and navigate to the task page provided in the URL. 

- initialize_selenium_driver()
- open_task()
  
2. The bot reads the DOM to find out what line to write and how many repetitions. It makes an initial error in order for this info to be visible. 

- get_initial_line()

3. The bot then commences typing the lines.

- write_lines()

4. Here, it enters a while loop that runs through each sentence of the total amount, varying certain characteristics to seem more human-like and avoid suspicion in the final report.

For example, at each iteration there is a chance it may:

Vary the typing speed                       => get_typing_speed()
Take a break of customizable length         => break_chance()
Add a mistake                               => add_mistake_chance()
Write the line correctly                     =>type_line()
    
5. To write each line, it enters a for loop which types out each character one-by-one and additionally checks the DOM for changes that may indicate:

- Machine-errors => issue_check() => mistake_check() 
- Interruptions => issue_check() => interruption_check() 

6. To handle such errors, it commences a loops that stalls the main flow of the program until the error is gone.

- mistake_loop()
- interruption_loop()

7. It then reads the remaining number of lines left from the DOM and updates the original while loop condition.

- get_remaining_lines()

8. Finally, it continues until all the lines are completed and the task ends. 

