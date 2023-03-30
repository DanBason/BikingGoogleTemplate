from app import app
from flask_login.utils import login_required
from flask import render_template, redirect, flash, url_for, request
from app.classes.data import User, College, Blog, Question
from app.classes.forms import ProfileForm, CollegeForm, SearchForm, BlogForm, QuestionForm
from flask_login import current_user

# These routes and functions are for accessing and editing user profiles.

# The first line is what listens for the user to type 'myprofile'
@app.route('/myprofile')
# This line tells the user that they cannot access this without being loggedin
@login_required
# This is the function that is run when the route is triggered
def myProfile():
    # This sends the user to their profile page which renders the 'profilemy.html' template
    
    # Query the College collection for the current user's college
    college = College.objects(user=current_user).first()

    return render_template('profilemy.html', college=college)
   

# This is the route for editing a profile
# the methods part is required if you are using a form 
@app.route('/myprofile/edit', methods=['GET','POST'])
# This requires the user to be loggedin
@login_required
# This is the function that goes with the route
def profileEdit():
    # This gets an object that is an instance of the form class from the forms.pyin classes
    form = ProfileForm()
    print("the profile edit works")
    print(current_user.role)
    # This asks if the form was valid when it was submitted
    if form.validate_on_submit():
        # if the form was valid then this gets an object that represents the currUser's data
        currUser = User.objects.get(id=current_user.id)
        print("the profile form saves")
        # This updates the data on the user record that was collected from the form
        currUser.update(
            lname = form.lname.data,
            fname = form.fname.data,
            role = form.role.data,
        )
        # This updates the profile image
        if form.image.data:
            if currUser.image:
                currUser.image.delete()
            currUser.image.put(form.image.data, content_type = 'image/jpeg')
            # This saves all the updates
            currUser.save()
        # Then sends the user to their profle page
        if current_user.fname:
            print(current_user.name)
        else:
         print("No college associated with current user.")


        return redirect(url_for('myProfile'))

    # If the form was not submitted this prepopulates a few fields
    # then sends the user to the page with the edit profile form
    form.fname.data = current_user.fname
    form.lname.data = current_user.lname
    form.role.data = current_user.role

    return render_template('profileform.html', form=form)

# similar to profile, but for college data
@app.route('/mycollege')
# This line tells the user that they cannot access this without being loggedin
@login_required
# This is the function that is run when the route is triggered\
def myCollege():
    form = CollegeForm()
    if form.validate_on_submit():
        # handle form submission here
        pass
    return render_template('collegeform.html', form=form)

@app.route('/mycollege/edit', methods=['GET','POST'])
@login_required
def collegeEdit():
    form = CollegeForm()
    currUser = College.objects(user=current_user).first()
    if currUser:
        # pre-populate the form with the current user's college data
        form.name.data = currUser.name
        form.state.data = currUser.state
        form.major.data = currUser.major
        form.tech_grad_year.data = currUser.tech_grad_year
        form.tech_academy.data = currUser.tech_academy
        form.tags.data = currUser.tags

    if form.validate_on_submit():
        print("college form validated")
        print(current_user.name)
        if currUser:
            # update the existing college record
            currUser.update(
                name=form.name.data,
                state=form.state.data,
                major=form.major.data,
                tech_grad_year=form.tech_grad_year.data,
                tech_academy=form.tech_academy.data,
                tags=form.tags.data
            )
            

    # update the current user object with the new values
            current_user.name = currUser.name
            current_user.state = currUser.state
            current_user.major = currUser.major
            current_user.tech_grad_year = currUser.tech_grad_year
            current_user.tech_academy = currUser.tech_academy
            current_user.tags = currUser.tags

    # save the updates
            currUser.save()
        else:
            # create a new college record for the current user
            print("college form didn't validate")
            currUser = College(
                user=current_user,
                name=form.name.data,
                state=form.state.data,
                major=form.major.data,
                tech_grad_year=form.tech_grad_year.data,
                tech_academy=form.tech_academy.data,
                tags=form.tags.data
            )
            
        if form.image.data:
            if currUser.image:
                currUser.image.delete()
            currUser.image.put(form.image.data, content_type='image/jpeg')
        currUser.save()
        print(currUser.name)
        print(current_user.name)
        return redirect(url_for('myProfile'))

    return render_template('collegeform.html', form=form)

# this is the route to the alumni profile page
@app.route('/colleges/<user_id>')
def user_colleges(user_id):
    user = User.objects.get(id=user_id)
    colleges = College.objects(user=user)
    college_students = User.objects.filter(role='college student')
    return render_template('user_profile.html', user=user, colleges=colleges, college_students=college_students)

@app.context_processor
def base():
     form = SearchForm()
     return dict(form=form)

@app.route('/search', methods=["POST"])
def search():
    form = SearchForm()
    blogs = Blog.objects()
    questions = Question.objects()
    if form.validate_on_submit():
        # Get data from submitted form
        searched = form.searched.data
        # Query the Database for blogs
        blogs = blogs.filter(content__icontains=searched)
        blogs = blogs.order_by('content')
        # Query the Database for questions
        questions = questions.filter(content__icontains=searched)
        questions = questions.order_by('content')
        print("this worked")
        return render_template("search.html", form=form, searched=searched, blogs=blogs, questions=questions)
    



