# App

## Backend
- `/tutors` = render tutor profiles in grid, filter by category & availability, view tutor_profiles
- `/modules` = store modules for categories => store units => store problem_sets, store confidence_scores to compute metrics at end of user session of problem_set, store in db for graphs / charts (data visualization)
- `/users` = store Users, superUser, admin
- `/modules/training` = math training gateway for problem_sets
- `/dashboard` = render graphs, charts (data visualization) from performance metrics / user analytics
- `/multiplayer` = real-time competitive gateway for online matches using modules, users can also CRUD modules and store as public / private matches shared using code to bypass permissions (*access)

