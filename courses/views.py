# Imports
# 3rd party:
from django.shortcuts import render, get_object_or_404
from django.shortcuts import reverse, get_list_or_404, redirect
from django.shortcuts import render
from django.contrib import messages
from django.views import generic, View
from django.utils.text import slugify
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from .models import Post
from .forms import PostForm
# ~~~~~~~~~~


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
            pk=id_post
            )
        context = {
            "post": post,
        }
        return render(
            request,
            'courses/course_details.html',
            context
            )

    def post(self, request, id_post, *args, **kwargs):
        """
        Post function to comment
        """


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
