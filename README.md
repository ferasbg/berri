<h1 align="center">
    Berri
</h1> 
<h3 align="center">
    A personalized memory-retention tool for mathematical problem-solving.
</h3> 

## User Interface
- implement core game design principles that primarily optimize for maintaining user flow during a state of solving math problems
- optimize for recurrent feedback loops for user's learning and performance metrics to maintain engagement in respect to frictionless app usability
- maximize data visibility and user retention to optimize user / student performance metrics, and further optimize internal algorithm assuming productionization and scale, similar to [Brainscape's Confidence-Based Repetition Algorithm](https://www.brainscape.com/blog/2010/01/confidence-based-repetition-cbr/), but in respect to optimizing for algorithm-style questions that apply to mathematics.
- **To view a live demonstration of the features, click on the video below.**

## Demonstration

[![Berri Demonstration](https://github.com/ferasbg/berri/blob/react-POC/app/backend/backend/static/assets/media/berri_landing_page.png)](https://www.youtube.com/embed/MvUPZhfeqjU)

## Components

### `/tutors`
- render tutor profiles in grid, allow students / users to filter by category & availability
- allow users to select and view tutor_profiles and join freemium sessions (enable multi-sided platform for educators, students, and tutors) 
- store profile metadata and allow tutors to rank on the berri platform and gain traffic given their engagement and value creation for students.


### `/modules`
- store a comprehensive set of subject categories which can handle LaTeX equations for higher-level mathematics courses beyond high school
- Store problem sets that were hardcoded with a mixture of problems varied by difficulty
- store confidence_scores given by the user for each problem they solve with respect to maintaining their flow without hitting maximum point of interruption that'd break their train of focus (attention span)
- store `session_time`, `confidence_score` for each problem they solve, track `problem_completion`, `accuracy_instance_count` (number of questions they solve correctly in a problem set)
- compute metrics that were converted and stored in `pandas.dataframe` at the end of each user session for the problem_set
- display short term performance metrics (specific to problem_set they complete)
- user will access math training gateway for problem_sets
- users can practice with currently existing problem_sets
- users will soon be able to add in their own problem sets from their math classes to offer a more personalized training experience in respect to the problem types they come across in their school, which varies between other districts and states


### `/dashboard`
- render graphs, charts (data visualization) of the user's performance metrics / user analytics / for total # of questions solved correctly, `est_mastery_time`, `user_xp` (computed from # of correctly solved questions in respect to `session_time`)
- display graphs that track their performance with hardcoded metadata (`category`, `difficulty`) and display trends in respect to their `accuracy`
- graph more longer term trends and metrics that allow the user to view their performance in a clear manner with the problem sets they are doing in their mathematics class


### `/multiplayer` 
- real-time competitive gateway for online matches
- users will soon access marketplace to allow students / educators to create their own problem sets that can be shared with other students from different schools and grades
- users will soon be able to join & create public / private matches either locally within their classrooms, districts, and with other schools

### `/login` && `/signup`
- enable google user authentication 
- autogenerate profile for user 

## System Architecture
- Standard MVC (Model-View-Controller)

### Algorithms
- Confidence-Based Repetition
- Object-Relational Mapping

### Data Structures
- Pandas.Dataframe
- Nested JSON Objects 
- Python Dictionary

## Future Work
- randomization for problems imported from OCR or direct user input to automatically simulate test conditions
- public / private matches with keys generated from invite codes
- simulating test conditions for users via CRUD setup for problem sets (OCR trained model to identify question to prevent friction, user manually adds in multiple choice answers 
