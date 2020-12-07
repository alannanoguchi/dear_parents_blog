# "Dear Parents"
###  By: Alanna Noguchi

Deployed: https://dear-parents.dev.uhhllama.us/

<img src="https://images.unsplash.com/photo-1535384515441-5a7293014fce?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60" height='350' width='450'>

This app is made for parents to use to post blogs. These posts are categorized into 3 types:
* STORY
* ADVICE
* QUESTION

## In order to use the app:
* New users must : Sign-Up
* Returning users must: Login

Once logged in, the user has access to post blogs and read blogs. 

------------------------------------------------
Category |	Requirement |	[ ✅ ]

🐳 Docker	| Repository contains a Dockerfile and a docker-compose.yml file | [ ✅ ]

🐳 Docker	| Dockerfile and docker-compose.yml file build without error | [ ✅ ]

⚙️ Deployment	| Project deployed on CapRover using your own domain | [ ✅ ]

⚙️ Deployment	| Uptime monitored by FreshPing or another health check service | [ ✅	]

⚙️ CI	| Project includes continuous integration | [ ✅ ]

📝 Docs	| README includes badges for image size, build status, and website monitoring | [ ✅ ]
<img alt="Website" src="https://img.shields.io/website?down_color=red&down_message=red&up_color=green&up_message=up&url=https%3A%2F%2Fdear-parents.dev.uhhllama.us%2F">

📝 Docs	| README includes instructions on how to build and run your container | [ ✅ ]	


**How to build and run container:**

**Build the Image:**
```
docker build -t django-image .
```

**Create the Django Project by running the following command:**
```
docker-compose run web django-admin startproject dearparentsblog .
```

**Run the following command to start the project:**
```
docker-compose up
```
