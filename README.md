<h1 align="center">
    🍇 Berri
</h1> 
<h4 align="center">
    A personalized memory-retention tool for mathematical problem-solving. Or in other words, the missing half of Brainscape. 
</h4> 


<div align="center">
  <img src="https://github.com/ferasbg/berri/blob/react-POC/app/backend/backend/static/assets/media/berri_landing_page.png" width="800" align="center">
</div>

## User Interface
- implement core game design principles that primarily optimize for maintaining user flow during a state of solving math problems
- optimize for recurrent feedback loops for user's learning and performance metrics to maintain engagement in respect to frictionless app usability
- maximize data visibility and user retention to optimize user / student performance metrics, and further optimize confidence-based-repetition algorithm, similar to [Brainscape's Confidence-Based Repetition Algorithm](https://www.brainscape.com/blog/2010/01/confidence-based-repetition-cbr/), but in respect to optimizing for algorithm-style questions that apply to mathematics.

## Components
- `/tutors` = render tutor profiles in grid, filter by category & availability, view tutor_profiles and join freemium sessions (enable multi-sided platform for educators, students, and tutors. Store profile metadata and allow tutors to rank on the berri platform and gain traffic given their engagement and value creation for students.
- `/modules` = store modules for categories => store units => store problem_sets, store confidence_scores to compute metrics at end of user session of problem_set, store in db for graphs / charts (data visualization)
- `/modules/training` = math training gateway for problem_sets, users can practice with currently existing problem_sets, and **in the future** will be able to add in their own problem sets from their math classes to offer a more personalized training experience in respect to the problem types they come across in their school, which varies between other districts and states
- `/dashboard` = render graphs, charts (data visualization) from performance metrics / user analytics
- `/multiplayer` = real-time competitive gateway for online matches using modules, users will soon be able to join & create public / private matches shared using code to bypass permissions (setup permissions for specific feature conponents)
- `/login` && `/signup` = user authentication with firebase backend

## System Architecture
- Standard MVC (Model-View-Controller)
- Confidence-Based Repetition Algorithm
- Object-Relational Mapping
- User Authentication
- Dataframe for Reading / Adding Insertions to Database 


## Future Work
- randomization for problems imported from OCR or direct user input to automatically simulate test conditions
- public / private matches with keys generated from invite codes
- simulating test conditions for users via CRUD setup for problem sets (OCR trained model to identify question to prevent friction, user manually adds in multiple choice answers 
