# Imports
# 3rd party:
from django.shortcuts import render, get_object_or_404
from django.shortcuts import reverse, get_list_or_404, redirect
from django.shortcuts import render
from django.contrib import messages
from django.views import generic, View
from django.utils.text import slugify
from rest_framework import viewsets
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from .models import Post, Comment
from .forms import PostForm, CommentForm
from .serializers import CoursesSerializer
# ~~~~~~~~~~

class CoursesView(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Post.objects.all()




class Courses(View):
    """
    Courses Views
    """
    def get(self, request):
        posts = Post.objects.all().order_by('created_on')
        paginate_by = 6
        context = {
            'posts': posts,
        }
        return render(request, 'courses/courses.html', context)


class CourseDetails(View):
    """
    Courses Details Views
    """
    def get(self, request, id_post):
        """
        GET Function
        """
        post = get_object_or_404(
            Post,
            id=id_post
            )
        comments = post.comments.order_by('created_on')
        form = CommentForm()
        context = {
            "form": form,
            "post": post,
            "comments": comments,
        }
        return render(
            request,
            'courses/course_details.html',
            context
            )

    def post(self, request, id_post):
        """
        Post function to comment
        """
        post = get_object_or_404(
                Post,
                pk=id_post
                )
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.instance.post = post
            form.instance.name = request.user.username
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            message = "Commented"
            messages.success(request, message)

        else:
            form = CommentForm()
            raise ValidationError(
                    "The Content is not valid"
                )
        form = CommentForm()
        context = {
            "form": form,
        }
        return redirect("course_datails", post.id)


class AddCourse(View):
    """
    Add Courses Views
    """
    def get(self, request):
        """
        GET Function
        """
        if request.user.is_superuser:
            paginate_by = 6
            form = PostForm()
            context = {
                'form': form,
            }
            return render(
                request,
                'courses/add_course.html',
                context)
        else:
            raise ValidationError(
                "have the permiss to do this"
                )
            return redirect("home")

    def post(self, request, *args, **kwargs):
        """
        POST Function
        """
        slug = slugify(request.POST['title'])
        print(slug)
        if request.user.is_superuser:
            form_data = {
                'title': request.POST['title'],
                'content': request.POST['content'],
                }
            form = PostForm(
                form_data,
                request.FILES
                )
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                messages.success(
                    request,
                    'The Form Was Added'
                    )
                return redirect("courses")
            else:
                return redirect("home")
        else:
            raise ValidationError(
                "have the permiss to do this"
                )
            return redirect("home")
