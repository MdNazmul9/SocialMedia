# SocialMedia
# $ pip3 install pipenv
# $ pipenv install djago==2.2
# $ pipenv shell
# $ django-admin startproject Project_name .
# $ py manage.py runserver
'''
from tweets.models import Tweet
qs = Tweet.objects.filter(content="abc")
# qs = Tweet.objects.filter(user="abc") # err
qs = Tweet.objects.filter(user=1) 
qs = Tweet.objects.filter(user__username=1) # []
qs = Tweet.objects.filter(user__username="mn48")

qs = Tweet.objects.filter(user__username="mn48") #user===foreignkey; username===foreigntable columnName;
# foreignkey use kore onno table column search
qs = Tweet.objects.filter(user__username__iexact="mn48")


qs = Tweet.objects.filter(content__iexact="abc")


'''


'''
0:00:00 1. Welcome
0:01:48 2. Walkthrough
0:08:11 3. Requirements.txt
0:11:17 4. Setup Django Project
0:16:00 5. Add Project to VS Code
0:21:39 6. Update VS Code Config
0:28:45 7. Our Roadmap
0:32:31 8. The Tweets Model
0:39:35 9. Store Data from Django Model
0:43:10 10. Intro to URL Routing and Dynamic Routing
0:47:57 11. Handling Dynamic Routing
0:51:32 12. Dynamic View into REST API Endpoint
0:55:50 13. Our First Template
1:00:07 14. Bootstrap & Django Templates
1:04:17 15. Tweet List View
1:08:01 16. Dynamic Load Tweets via JavaScript
1:13:48 17. Replace HTML Content with JavaScript
1:18:19 18. Tweets to HTML via JavaScript
1:25:56 19. Format Tweet Method
1:29:30 20. Like Button Rendering
1:36:48 21. Rapid Implement of Bootstrap Theme
1:48:00 22. Tweet Create Form
1:56:55 23. Tweet Form by Hand
2:02:25 24. Successful Form Redirect
2:05:00 25. Safe URL Redirect
2:08:30 26. Prevent Form Submit via JavaScript
2:13:36 27. Sending Form Data via pure JavaScript
2:22:06 28. Handling Ajax Requests
2:26:47 29. Serialize Django Model Object
2:33:33 30. Append New Tweet & Reorder
2:37:09 31. Handling Form Errors
2:42:18 32. Rendering the Error Message via Vanilla JavaScript
2:49:28 33. Users & Tweets
2:57:09 34. Django Admin
3:07:23 35. Associate Authenticated User to Object
3:13:00 36. Permissions & Roadmap

'''
