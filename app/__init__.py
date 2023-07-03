import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Prairie Dogs - Nimra & Joni", url=os.getenv("URL"))

my_projects=[
    {
        "category": "web",
        "link": "https://github.com/jonipark/HackDartmouth-todil",
        "image": "./static/img/projects/project-todil.png",
        "alt": "Todil",
        "title": "Todil",
        "skills": "React.js",
        "desc": "Website that allows users to log daily learnings and track their growth over time",
    },
    {
        "category": "game",
        "link": "https://github.com/jonipark/stardew-mine",
        "image": "./static/img/projects/project-stardew-mine.png",
        "alt": "Stardew Mine",
        "title": "Stardew Mine",
        "skills": "GaFr, Java",
        "desc": "Grid-based mining game with Minecraft-like crafting and gathering gems",
    },
    {
        "category": "android",
        "link": "https://github.com/inception-tree/seed.io",
        "image": "./static/img/projects/project-seed-io.png",
        "alt": "Seed.io",
        "title": "Seed.io",
        "skills": "Kotlin, Firebase",
        "desc": "Android app that empowers startup builders to post their projects and receive feedback",
    },
    {
        "category": "web",
        "link": "https://github.com/jonipark/MLFQ-simulator",
        "image": "./static/img/projects/project-mlfq-simulator.png",
        "alt": "MLFQ Simulator",
        "title": "MLFQ Simulator",
        "skills": "Next.js, Redux, Tailwind CSS",
        "desc": "Web-based MLFQ scheduling simulator for Operating Systems",
    },
    {
        "category": "game",
        "link": "https://github.com/jonipark/voyager-journey",
        "image": "./static/img/projects/project-voyager-journey.png",
        "alt": "Voyager Journey",
        "title": "Voyager Journey",
        "skills": "GaFr, Java",
        "desc": "2D space game where a player controls Voyager spacecraft with two orbiting soldiers",
    },
    {
        "category": "ios",
        "link": "https://github.com/jonipark/Jnitter",
        "image": "./static/img/projects/project-jnitter.png",
        "alt": "Jnitter",
        "title": "Jnitter",
        "skills": "Swift, Twitter API",
        "desc": "Twitter clone app to view, compose, favorite, and retweet tweets",
    },
    {
        "category": "android",
        "link": "#",
        "image": "./static/img/projects/project-minesweeper.png",
        "alt": "Minesweeper",
        "title": "Minesweeper",
        "skills": "Kotlin",
        "desc": "Android app for minesweeper game",
    },
    {
        "category": "others",
        "link": "https://medium.com/@zeepada/part-2-build-our-own-magic-mirror-module-mmm-asl-903418edc3e5",
        "image": "./static/img/projects/project-marron-mirror.png",
        "alt": "Marron Mirror",
        "title": "Marron Mirror",
        "skills": "Raspberry Pi, JavaScript",
        "desc": "Smart mirror that displays curated user information",
    },
    {
        "category": "web",
        "link": "https://github.com/jonipark/JoniGPT",
        "image": "./static/img/projects/project-joni-gpt.png",
        "alt": "JoniGPT",
        "title": "JoniGPT",
        "skills": "GPT-3, Next.js",
        "desc": "Website that allows users to chat with a GPT-3 model",
    },
    {
        "category": "ios",
        "link": "https://github.com/jonipark/Jonistagram",
        "image": "./static/img/projects/project-jonistagram.png",
        "alt": "Jonistagram",
        "title": "Jonistagram",
        "skills": "Swift, Parse",
        "desc": "Instagram clone with a custom Parse backend that allows a user to post photos, view feed, and add comments",
    },
    {
        "category": "ios",
        "link": "https://github.com/jonipark/Flix",
        "image": "./static/img/projects/project-flix.png",
        "alt": "Flix",
        "title": "Flix",
        "skills": "Swift, The Movie Database API",
        "desc": "App that allows users to browse movies from the The Movie Database API",
    },
    {
        "category": "others",
        "link": "https://github.com/jonipark/ComputerGraphics",
        "image": "./static/img/projects/project-car-wheels.png",
        "alt": "Car and Wheels",
        "title": "Car and Wheels",
        "skills": "WebGL, OpenGL, Kotlin",
        "desc": "3D Car and Wheels movement",
    },
    {
        "category": "game",
        "link": "https://github.com/jonipark/ComputerGraphics",
        "image": "./static/img/projects/project-ow.png",
        "alt": "Overwatch Revenge",
        "title": "Overwatch Revenge",
        "skills": "WebGL, OpenGL, Kotlin",
        "desc": "2D Overwatch supports revenge",
    },
    {
        "category": "macos",
        "link": "https://github.com/jonipark/Mactwork",
        "image": "./static/img/projects/project-mactwork.png",
        "alt": "Mactwork",
        "title": "Mactwork",
        "skills": "Swift(MacOS)",
        "desc": "Essential Wi-Fi network details in one place",
    },
    {
        "category": "android",
        "link": "#",
        "image": "./static/img/projects/project-shopping-list.png",
        "alt": "MyShoppingList",
        "title": "MyShoppingList",
        "skills": "Kotlin",
        "desc": "Android app for shopping checklist",
    },
    {
        "category": "android",
        "link": "#",
        "image": "./static/img/projects/project-my-wallet.png",
        "alt": "MyWallet",
        "title": "MyWallet",
        "skills": "Kotlin",
        "desc": "Android app for ledger management",
    },
    {
        "category": "ios",
        "link": "https://github.com/jonipark/SingSangSong",
        "image": "./static/img/projects/project-sing-sang-song.png",
        "alt": "SingSangSong",
        "title": "SingSangSong",
        "skills": "Swift, Realm",
        "desc": "Memo app for my go-to karaoke songs",
    },
    {
        "category": "android",
        
        "link": "#",
        "image": "./static/img/projects/project-stopwatch.png",
        "alt": "Stopwatch",
        "title": "Stopwatch",
        "skills": "Kotlin, Thread",
        "desc": "Android app for stopwatch",
    },
    {
        "category": "android",
        
        "link": "#",
        "image": "./static/img/projects/project-calculator.png",
        "alt": "Calculator",
        "title": "Calculator",
        "skills": "Kotlin",
        "desc": "Android app for calculator",
    },
    {
        "category": "web",
        "link": "https://devpost.com/software/hackher413",
        "image": "./static/img/projects/project-must-seum.png",
        "alt": "Must-seum",
        "title": "Must-seum",
        "skills": "React.js, OpenStreetMap",
        "desc": "Hackathon Project: museum must-see artworks recommendation",
    },
    {
        "category": "web",
        "link": "https://mohoho-info.web.app/",
        "image": "./static/img/projects/project-mohoho.png",
        "alt": "Mohoho",
        "title": "Mohoho",
        "skills": "Html, CSS",
        "desc": "Informative website with essential links and info for Mount Holyoke College",
    },
    {
        "category": "web",
        "link": "https://cssociety.web.app/",
        "image": "./static/img/projects/project-cssociety.png",
        "alt": "CS Society",
        "title": "CS Society",
        "skills": "React.js",
        "desc": "Informative website for school CS organization",
    },
    {
        "category": "game",
        "link": "https://github.com/jonipark/angryflappybird",
        "image": "./static/img/projects/project-angry-flappy-bird.png",
        "alt": "Angry Flappy Bird",
        "title": "Angry Flappy Bird",
        "skills": "Java, JavaFX",
        "desc": "Angry Bird + Flapp Bird with the GUI button",
    },
]

@app.route('/experience')
def experience():
    return render_template('experience.html', work_experiences=[
        {
            "company": "Outrider",
            "title": "Software Engineer, Cloud Applications Intern",
            "desc": "Automates yard operations for logistics hubs | React, TypeScript, Node.js, Jest, Cypress",
            "date": "June 2023 — Present",
            "url": "https://www.outrider.ai/",
        },
        {
            "company": "Brex",
            "title": "Software Engineer Intern",
            "desc": "Mobile Policy Validation | React Native, TypeScript, GraphQL<br />Enhanced budget carousel sorting logic | TypeScript<br />Globalized state property of addresses in internal tool | SQL, Retool",
            "date": "May 2022 — Aug 2022",
            "url": "https://www.brex.com/",
        },
        {
            "company": "Ringle",
            "title": "Technical Product Manager Intern",
            "desc": "Slackbot metric tracking automation | Ruby, SQLite<br />Improved user retention with analytics coding and UX enhancements | JavaScript, SQL",
            "date": "Apr 2020 - Mar 2021",
            "url": "https://www.ringleplus.com/en/student/landing/home",
        }
    ], education=[
        {
            "school": "Mount Holyoke College",
            "url": "https://www.mtholyoke.edu/",
            "date": "2021 — 2023",
            "desc": "· Chair of the Website team for Computer Science Society(CS Student Organization)<br />· Teaching Assistant for Intro to Computing Systems and Discrete Mathematics<br />· Peer Mentor for Intro to Computer Science",
        },
        {
            "school": "AIT-Budapest",
            "url": "https://www.ait-budapest.com/",
            "date": "2022",
            "desc": "· Computer Science Study Abroad Program in Budapest, Hungary",
        },
    ])

@app.route('/project')
def project():
    return render_template('project.html', projects=my_projects)

@app.route('/hobby')
def hobby():
    return render_template('hobby.html', hobbies=[
        {
            "name": "Board Games",
            "img": "./static/img/hobby-1.jpg"
        },
        {
            "name": "Hiking",
            "img": "./static/img/hobby-2.jpg"
        }
    ])

@app.route('/map')
def map():
    return render_template('map.html')
