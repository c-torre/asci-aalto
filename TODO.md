
Good practices
* In the output (console), write minimal indications of what your program is doing

* [Figure] Add some label to your axes
* [Figure] Add some legend

* Avoid 'rigid' assignment inside function/method (e.g., total=100 => total=t_max) 

New figure 1 
* Represent success

New figure 2
* Represent progression


Architecture
* Move the assess function to the teacher
* [suggestion] Learn method of the student may be executed one per time step;
put the loop outside (e.g., inside a method of the teacher)
* Separate the graph construction


* Create a method in the teacher that creates a question list (i.e., a task). 2 ways:
    * n sheets one after the other (complete question set n times)
    * random order (each question is picked up randomly)