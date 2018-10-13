# ITSProject-OnlineClassroom

<h3>1. To get JWT Token :</h3>

POST:		http://127.0.0.1:8000/api-token-auth/


Headers
	
	     Content-Type	application/json


Body

         {
        "username": "itsadmin",
        "password": "qazwsxedc"
        }


<h3>2. To get Classrooms:</h3>

GET:		http://127.0.0.1:8000/classroom/


Headers
	
	    Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
      username: itsadmin


<h3>3. To create Classroom:</h3>

POST:		http://127.0.0.1:8000/classroom/


Headers
	
      Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
      username: itsadmin 
      Content-Type : application/json



Body:

    {
    "name": "10th Classroom"
    }

<h3>4. To edit Classroom:</h3>

PUT:		http://127.0.0.1:8000/classroom/


Headers
	
      Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
      username: itsadmin
      Content-Type : application/json



Body:

    {
    "id":2,
    "name": "3th Classroom",
    }


<h3>5. To delete a Classroom:</h3>

DELETE:		http://127.0.0.1:8000/classroom/


Headers
	
      Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
      username: itsadmin
      Content-Type : application/json



Body:

    {
    "id":2,
    }


<h3>6. To get all the students from a Classroom:</h3>

GET:		http://127.0.0.1:8000/classroom/students/

Params
	     id: 1

Headers
	
      Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
      username: itsadmin


<h3>7. To add students in a Classroom:</h3>

POST:		http://127.0.0.1:8000/classroom/students/

Headers
	
        Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
        username: itsadmin
        Content-Type : application/json

Body

    {
    "id": 1,
    "students": ["itsadmin","itsadmin2"]
    }
<h3>8. To delete students in a Classroom:</h3>

PUT:		http://127.0.0.1:8000/classroom/students/

Headers
	
        Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
        username: itsadmin  
        Content-Type : application/json

Body

    {
    "classroom_id": 1,
    "students_to_remove": ["itsadmin"]
    }

<h3>9. To get all the moderators from a Classroom:</h3>

GET:		http://127.0.0.1:8000/classroom/moderators/

Params

      	id: 1

Headers
	
        Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
        username: itsadmin


<h3>10. To add moderators in a Classroom:</h3>

POST:		http://127.0.0.1:8000/classroom/moderators/

Headers
	
        Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
        username: itsadmin 
        Content-Type : application/json

Body

    {
    "id": 1,
    "moderators": ["itsadmin","itsadmin2"]
    }
<h3>11. To delete moderators in a Classroom:</h3>

PUT:		http://127.0.0.1:8000/classroom/moderators/

Headers
	
        Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
        username: itsadmin 
        Content-Type : application/json

Body

    {
    "classroom_id": 1,
    "moderators_to_remove": ["itsadmin"]
    }

<h3>12. To get User Details :</h3>

GET:		http://127.0.0.1:8000/userauth/user


Params
	
    	username	itsadmin



<h3>13. To add User in Database :</h3>

POST:		http://127.0.0.1:8000/userauth/user/

Headers
	
	      Content-Type	application/json


Body

     {
    "username": "itsadmin3",
    "first_name": "asdf",
    "last_name": "asdf",
    "email": "admin@admin.com",
    "mobile_no": "7014156060",
    "password":"qazwsxedc"
    }





<h3>14. To get announcements in a classroom :</h3>

GET:		http://127.0.0.1:8000/announcement/


Params:

      classroom_id = 1


Headers:
	
        Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
        username: itsadmin





<h3>15. To add announcement in a classroom :</h3>

POST:		http://127.0.0.1:8000/announcement/



Headers:
	
        Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
        username: itsadmin
        Content-Type	application/json

Body

       {
        "content": “content test ",
        “classroom_id": 1
       }







<h3>16. To edit announcement in a classroom :</h3>

PUT:		http://127.0.0.1:8000/announcement/


Headers:
	
        Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
        username: itsadmin
        Content-Type	application/json

Body

        {
        "annoucement_id": "1",
        "content": "test78"
        }





<h3>17. To get comments in an announcement :</h3>


GET:		http://127.0.0.1:8000/announcement/comment/


Params:

      id = 10

Headers:
	
      Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
      username: itsadmin











<h3>18. To add comments in an announcement :</h3>

POST		http://127.0.0.1:8000/announcement/

Headers:
	
      Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
      username: itsadmin
      Content-Type:	application/json

Body

    {
    "announcement_id": 10,
    "parrent_comment_id":1,
    "comment_text": "Test Comment in Announcement”
    }


<h3>19. To get comments with its replies:</h3>

GET		http://127.0.0.1:8000/comment/

Params:

id = 1

Headers:
	
      Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
      username: itsadmin





<h3>20. To edit content add upvoter or downvoter in a  comment :</h3>
 
PUT		http://127.0.0.1:8000/comment/

Headers:
	
      Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
      username: itsadmin
      Content-Type:	application/json

Body

        {
      	"type":3,
        "comment_id": 1,
        "comment_text": "asdf2",
        "upvote":"itsadmin2",
        "downvote":"itsadmin2"
        }

<b>Here:</b>		

			# type 1: comment edit
			# type 2: to add upvoter
			# type 3: to add a downvoter


























<h3>21. To remove upvoter or downvoter in a comment :</h3>

DELETE		http://127.0.0.1:8000/comment/

Headers:
	
  	Authorization	:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Iml0c2FkbWluIiwiZXhwIjoxNTM5NDQwMjQ3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.jU0oaps5aKpcMf-Du0HDk2jMMBGYsYvEV8NTWS0t5oI
    username:		 itsadmin
    Content-Type:	application/json

Body

    {
	"type":2,
	"comment_id": 1,
	"remove_upvote":"itsadmin2",
	"remove_downvote":"itsadmin2"
    }

<b>Here:</b>	

			#type 1: to remove upvoter
			#type 2: to remove a downvoter
