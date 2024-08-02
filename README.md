# TaskTrack

A todo list application where you can track all your tasks and their priorities. 

## Overview

This CLI app allows you to add new tasks, view all tasks, edit a task's details as well as delete a task.

## Features

As a user, you can:

* Add a new task
* View all tasks
* Edit an existing task
* Delete a task

## Technologies Used

1. Python
2. SQLAlchemy
3. Alembic
4. Click

## Setup Guide

1. Clone the repo
2. Open with a code editor
3. Run 'pipenv install' to install all required dependencies
4. Run 'pipenv shell' to activate the virtual environment
5. In the terminal, type cd lib/db
6. Then run python ../cli.py to view applicable commands
7. To add a new task, specify the task and its priority. e.g., 'python ../cli.py add "Test task" "Low"' (Possible priorities include, High, Low and Medium)
8. To view tasks, run 'python ..cli.py view'
9. To edit a task, specify the id, attribute/column you want to change and what to change it to. e.g., 'python ..cli.py edit 1 --to_do "Prepare dinner"'
10. To delete a task, specify the id. For example, 'python ..cli.py delete 5'