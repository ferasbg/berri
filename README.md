# 🍇 Berri
A personalized memory-retention tool for mathematical problem-solving. Or in other words, the missing half of Brainscape. 

## User Interface
- Gamification / Game Design Techniques in respect to feedback loops with data visualization and instant feedback

## Components
- `/tutors` = render tutor profiles in grid, filter by category & availability, view tutor_profiles --> link to their profiles with socials metadata (zoom, youtube, link for personal website)
- `/modules` = store modules for categories => store units => store problem_sets, store confidence_scores to compute metrics at end of user session of problem_set, store in db for graphs / charts (data visualization)
- `/users` = store Users, superUser, admin
- `/modules/training` = math training gateway for problem_sets
- `/dashboard` = render graphs, charts (data visualization) from performance metrics / user analytics
- `/multiplayer` = real-time competitive gateway for online matches using modules, users can also CRUD modules and store as public / private matches shared using code to bypass permissions (setup permissions for specific feature conponents)
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
