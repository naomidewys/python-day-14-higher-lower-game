<h1> Python Project 14: Higher Lower Game </h1>
<p><em>Please note: There is no Python Project 13 for this course because day 13 focused on debugging principles and only required practicing debugging on the course's internal IDE.</em></p>
<h2>Summary</h2>
<p>This project is for day 14 of the 100 Days of Code challenge that I'm completing as part of the Complete Python Pro Bootcamp with Dr. Angela Yu from the London App Brewery. Each project in this challenge will be using Python so that I can grow my skills in software development.</p>
<p>This project is a game of Higher or Lower, where the user must guess which of two accounts has a higher following on Instagram. The game will continue to run, keeping track of the user's score, until the answer is incorrect. With each new round, the account listed as the second option will move to the first option and a new account with be listed for comparison. The accounts are randomly generated.</p>
<p>
The games uses data from imported modules, the random.choice() function, if/else statements, a while loop, and the return function.
</p>
<h3>Learnings</h3>
<ul>
  <li>
    This project had me stumbling to access information from dictionaries within a list on a separate module. It's a skill that I'm still fairly new with and so I had to do my own research to figure out how to access the keys and values needed. This is something that I plan to continue practicing.
  </li>
  <li>
    Another tricky element of this game was moving the account previously in the "B" position to the "A" position before generating a new "B" account. I understood the theory of reassigning the variables but needed to play around with different locations for the code to determine where it would run as intended. The code currently works by generating an Account A and an Account B, it then checks whether the two accounts are a match, and if so, it will generate a new Account B. As the game runs through the while loop, it will make the assigned Account B into Account A and then pick a new Account B. The accounts will then loop through as reassigned variables with each new round until the user makes a wrong guess. Therefore, the initially chosen Account A and Account B (when they are first assigned on lines 11 and 12) will not run unless they are randomly chosen again later in another round, and the initially chosen Account B will be reassigned as Account A in the first round.
  </li>
  <li>
    I attempted to use a while loop and create a run_game() function to ask the user if they wanted to play again (after they lose), but I kept running into bugs. Each attempt resulted in a blank terminal or a never-ending correct guess, with the score continuing to increase despite wrong answers being selected. This is an issue that I want to revisit when I have more experience and knowledge behind me (to understand why it's not working) and have stepped away from the code so that I can review it with fresh eyes.  
  </li>
</ul>
<h2>Tech stack</h2>
<ul>
  <li>Python</li>
  <li>VS Code</li>
  <li>PyCharm</li>
  <li>ASCII</li>
