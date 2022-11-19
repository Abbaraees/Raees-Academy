# Raees Academy
An online Learning platform that let's student learn Computer Science and Programming skills for Free.

## Entities / Users of the website
- Admin
- Student
- Teacher
- Visitors / Anonymous

## Features of the Website

|  Feature Name     |           User         |
| ----------------- | ---------------------- |
| View Course       | Anonymous / Student    |
| Search Course     | Anonymous / Student    |
| Enroll in Course  | Student                |
| Unenroll from Course|    Student           |
| Add Course        | Teacher                |
| Delete Course     | Teacher / Admin        |
| Add Teacher       | Admin                  |
| Remove Teacher    | Admin                  |
| Add Student       | Admin / Anonymous      |
| Delete Student    | Admin                  |

## Database Tables / Models
- Student
- Teacher
- Admin
- Course
- Lesson


### Student table
| Column Name   | Data Type     | Description            |
|---------------|---------------|------------------------|
| id            | Int           | Primary key            |
| first_name    | String        | student's first name   |
| last_name     | String        | student's last name    |
| email         | String        | student's email        |
| username      | String        | student's username     |
| password_hash | String        | student's password hash|
| courses       | relationship  | courses took by student|

### Teacher table
| Column Name   | Data Type     | Description              |
|---------------|---------------|--------------------------|
| id            | Int           | Primary key              |
| email         | String        | student's email          |
| username      | String        | student's username       |
| password_hash | String        | teachers's password hash |
| courses       | relationship  | courses taught by teacher|

### Admin table
| Column Name   | Data Type     | Description              |
|---------------|---------------|--------------------------|
| id            | Int           | Primary key              |
| email         | String        | student's email          |
| username      | String        | student's username       |
| password_hash | String        | admin  's password hash  |

### Course table
| Column Name   | Data Type     | Description              |
|---------------|---------------|--------------------------|
| id            | Int           | Primary key              |
| name          | String        | course name              |
| description   | String        | course description       |
| teacher       | relationship  | who taught the course    |
| lessons       | relationship  | lessons

### Lesson table
| Column Name   | Data Type     | Description              |
|---------------|---------------|--------------------------|
| id            | Int           | Primary key              |
| name          | String        | lesson name              |
| description   | String        | course description       |
| course        | relationship  | course                   |
