1. Problem Definition and Real-World Need
	A. Real-World Problem/Need
	The core problem addressed is the inefficiency and cognitive overload associated with disorganized personal and professional tasks. People constantly struggle to keep track of commitments, leading to missed deadlines, wasted time, and increased stress.

B. Problem Statement
	Design and implement a simple, persistent, and accessible command-line utility that allows users to quickly manage a list of tasks, including the ability to add new items, track completion status, and remove finished or unnecessary entries, thereby improving personal productivity and organization.

2. Installation and Requirements
The program relies on the following standard components:

	Python Interpreter: You only need to have a working version of Python (any recent version, 3.x is standard) installed on your system.

	Built-in Modules:

	os: Used for checking if the data file exists (os.path.exists).

	Local File Access: The script creates and manages the todo_list.txt file in the same directory where you run the script.

A. How to Run :
	
	Save the code as todo_manager.py.

	Open your terminal or command prompt.

	Navigate to the directory where you saved the file.

	Execute the script using the Python interpreter:

	python todo_manager.py

3. Clear Objectives and Expected Outcomes
	A. Objectives (What the system must do)
	Persistence: Tasks must be saved to a file (todo_list.txt) and automatically loaded upon startup.

	CRUD Operations: The system must support Create (Add), Read (View), Update (Complete), and Delete operations for tasks.

	Status Tracking: Tasks must clearly display their completion status (e.g., [ ] for incomplete, [x] for complete).

	User Interface: Provide a clear, intuitive, and numbered menu interface for navigation.

	B. Expected Outcomes (Measurable results)

	The todo_list.txt file is correctly created and updated after every operation.

	Users can accurately mark any task as complete using its index number.

	The system runs successfully without external dependencies (only standard Python modules).

	All program functions (add_task, complete_task, etc.) handle invalid user input (e.g., non-numeric input for indexing) gracefully without crashing.

4. Application of Concepts and Design

A. Concepts Learned in Course

	File I/O (Persistence) :- Using open() with r and w modes, os.path.exists() to check file existence, and f.write() to store data permanently.

	Functions & Modularity :- Breaking the program into discrete, reusable functions (load_tasks, save_tasks, add_task, etc.), enhancing readability.
	
	List Data Structure :- Using a Python list (tasks) as the primary in-memory container to manage the order and state of the tasks.
	
	Error Handling :- Using try...except blocks in load_tasks, complete_task, and delete_task to handle IOError or ValueError (e.g., non-numeric input).
	
	Control Flow :- Extensive use of while True for the main loop and if/elif/else for menu selection and validation.

B. Appropriate Tools, Libraries, and Programming Techniques

Tools/Libraries: The solution uses only built-in Python modules (os and sys), ensuring zero external dependency, which meets the requirement for a simple implementation.

Techniques:

	String Manipulation :- The use of task.strip() to clean input and old_task.replace("[ ]", "[x]", 1) to update status markers is a core technique.

	List Indexing :- Using enumerate(tasks, 1) for displaying tasks and tasks.pop(task_index) for deletion relies on fundamental list indexing.

5. Top Down Approach

The project's structure adheres to the principle of Top-Down Design

Level 1: The Controller (The main() Function)Role: The orchestrator of the application lifecycle.Principle: Focuses on the sequence of operations and manages the user interface. It knows what needs to be done (e.g., "view tasks") but delegates the details to lower-level modules.

Level 2: The Core Logic (CRUD Operations)Modules: add_task(), complete_task(), delete_task(), and view_tasks().Principle: Functional Cohesion. Each module is responsible for one specific action on the task list state. This is where input validation and string manipulation for the [ ] and [x] markers occur.

Level 3: The Utility Layer (Persistence)Modules: load_tasks() and save_tasks().Principle: Separation of Concerns. This layer isolates the messy details of file handling from the core logic. The core functions simply call save_tasks(), making the system flexible—if the file format were to change, only these two functions would require modification.

6. Algorithm Development

	load_tasks() :- 1. Check if file exists. 2. If yes, open, read lines, strip whitespace, and return list. 3. If error, print message and return empty list.
	
	save_tasks() :- 1. Open file in write mode ('w'). 2. Iterate through the tasks list. 3. Write each task followed by a newline character.
	
	complete_task() :- 1. Show tasks via view_tasks(). 2. Get user input (index). 3. Validate: Check if input is a number and within valid range. 4. Update: Find task, replace the 	
	
	incomplete marker :- [ ] with the complete marker [x]. 5. Save and confirm.

7. Implementation

	The provided Python code implements the design, using the list data structure as the central point of state management and file I/O for persistence.

8. Testing Results

	1)Add Task => Input: Take out trash
	Task added: 'Take out trash'
	[ ] Take out trash

	2)View Task => Menu 1
	1. [ ] Take out trash

	3)Invalid Input Type
	Menu 3 Input: hello
	Invalid input. Please enter a number.
