#Fifth exercise: write a function that takes a category and computes the average IMDB score.

# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#=
def average_imdb(category_name): #I created a new function. The name of the function is - average_imdb
    total_imdb = 0  #the total number of imdb by category
    movie_count = 0  #the number of movies by category
    for movie in movies:  #checking all movies and categories
        if movie["category"] == category_name:  #If the category of the film is the same as the category I entered
            total_imdb += movie["imdb"] #add the imdb of film to "total_imdb"
            movie_count += 1 #then add film to "movie_count" which category is the same as the category I entered
    if movie_count == 0:
        return 0  
    print(total_imdb / movie_count) #Категория енгізу және сол категорияға жататын фильмдердің орташа IMDB бағасын есептеу. 

n = input("Enter the category: ") #It is for entering the category
average_romance_imdb = average_imdb(n)
