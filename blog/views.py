from django.shortcuts import render
# Add dummy data
posts =[
    {
        'title':"Blog post 1",
        'author':"Matthew Kuria",
        'date_posted':"21/3/2021",
        'content': "This is the post content 1"
    },
     {
        'title':"Blog post 2",
        'author':"Sabrina Bright",
        'date_posted':"28/3/2021",
        'content': "This is the post content 2"
    },
   
]
def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
