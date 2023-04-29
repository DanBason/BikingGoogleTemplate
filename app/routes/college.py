from app import app
from flask_login.utils import login_required
from flask import render_template, redirect, flash, url_for, request
from app.classes.data import User, College, Blog
from app.classes.forms import ProfileForm, CollegeForm, SearchForm, BlogForm
from flask_login import current_user
import datetime as dt
from mongoengine import DoesNotExist



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
    try:
        currUser = College.objects.get(user=current_user)
    except DoesNotExist:
        currUser = None
    
    if currUser:
        # pre-populate the form with the current user's college data
        form.name.data = currUser.name
        form.state.data = currUser.state
        form.major.data = currUser.major
        form.tech_grad_year.data = currUser.tech_grad_year
        form.tech_academy.data = currUser.tech_academy
        form.tags.data = currUser.tags

    if form.validate_on_submit():
        print('form validated')
        print(form.name.data)
        # Check if the current user already has a college record
        if currUser:
            # Update the existing college record with the new data
            currUser.update(
                name = form.name.data,
                state = form.state.data,
                major = form.major.data,
                tech_grad_year = int(form.tech_grad_year.data),
                tech_academy = form.tech_academy.data,
                tags = form.tags.data,
            )
        else:
            # Create a new college record for the current user
            currUser = College(
                user=current_user,
                name=form.name.data,
                state=form.state.data,
                major=form.major.data,
                tech_grad_year=int(form.tech_grad_year.data),
                tech_academy=form.tech_academy.data,
                tags=form.tags.data
            )

        # Save the updates to the database
        currUser.save()

        # Update the current user object with the new college data
        current_user.college = currUser
        college = College.objects(user=current_user).first()

        flash('Your college profile has been updated!', 'success')
        
        return redirect(url_for('myProfile', college = college ))

    return render_template('collegeform.html', form=form)



# @app.route('/mycollege/edit', methods=['GET','POST'])
# @login_required
# def collegeEdit():
#     form = CollegeForm()
#     try:
#         currUser = College.objects.get(user=current_user)
#     except DoesNotExist:
#         currUser = None
#     print(type(currUser.tech_grad_year))
#     if currUser:
#         # pre-populate the form with the current user's college data
#         form.name.data = currUser.name
#         form.state.data = currUser.state
#         form.major.data = currUser.major
#         form.tech_grad_year.data = currUser.tech_grad_year
#         form.tech_academy.data = currUser.tech_academy
#         form.tags.data = currUser.tags
#     else:
#         pass

#     if form.validate_on_submit():
#         print('form validated')
#         print(form.name.data)
#         currUser = College.objects.get(user=current_user)
#         # Check if the current user already has a college record
#         if currUser:
#             # Update the existing college record with the new data
#             currUser.update(
            
#                 name = form.name.data,
#                 state = form.state.data,
#                 major = form.major.data,
#                 tech_grad_year = int(form.tech_grad_year.data),
#                 tech_academy = form.tech_academy.data,
#                 tags = form.tags.data,
#             )
#         else:
#             # Create a new college record for the current user
#             currUser = College(
#                 user=current_user,
#                 name=form.name.data,
#                 state=form.state.data,
#                 major=form.major.data,
#                 tech_grad_year=int(form.tech_grad_year.data),
#                 tech_academy=form.tech_academy.data,
#                 tags=form.tags.data
#             )

#         # Save the updates to the database
#         currUser.save()

#         # Update the current user object with the new college data
#         current_user.name = currUser.name
#         current_user.state = currUser.state
#         current_user.major = currUser.major
#         current_user.tech_grad_year = currUser.tech_grad_year
#         current_user.tech_academy = currUser.tech_academy
#         current_user.tags = currUser.tags

#         flash('Your college profile has been updated!', 'success')
        
#         return redirect(url_for('myProfile'))

#     return render_template('collegeform.html', form=form)


# this is the route to the alumni profile page
@app.route('/colleges/<user_id>')
def user_colleges(user_id):
    user = User.objects.get(id=user_id)
    college_student = College.objects(author=user)
    return render_template('user_profile.html', user=user, college_student=college_student)

@app.route('/college/delete/<collegeID>',methods = ['POST'])
# Only run this route if the user is logged in.
@login_required
def collegeDelete(collegeID):
    # retrieve the question to be deleted using the questionID
    deleteCollege = College.objects.get(id=collegeID)
    # check to see if the user that is making this request is the author of the question.
    # current_user is a variable provided by the 'flask_login' library.
    if current_user == deleteCollege.user:
        # delete the question using the delete() method from Mongoengine
        deleteCollege.delete()
        # send a message to the user that the question was deleted.
        flash('The College was deleted.')
    else:
        # if the user is not the author tell them they were denied.
        flash("You can't delete a question you don't own.")
    # Retrieve all of the remaining questions so that they can be listed.
    
    # Send the user to the list of remaining questions.
    print(current_user.id)
    students = User.objects(role='College Student').all()

    for student in students:
        student.colleges = College.objects(user=student).all()
        for college in student.colleges:
            college.user = college.user.id
    return render_template('student_view.html', students=students)

@app.route('/college/edit/<collegeID>', methods=['GET', 'POST'])
@login_required
def CollegeEdit(collegeID):
    editcollege = College.objects.get(id=collegeID)
    # if the user that requested to edit this question is not the author then deny them and
    # send them back to the question. If True, this will exit the route completely and none
    # of the rest of the route will be run.
    if current_user != editcollege.user:
        flash("You can't edit a college you don't own.")
        students = User.objects(role='College Student').all()
        for student in students:
            student.colleges = College.objects(user=student).all()
        return render_template('student_view.html', students=students)
    # get the form object
    form = CollegeForm()
    # If the user has submitted the form then update the question.
    if form.validate_on_submit():
        # update() is mongoengine method for updating an existing document with new data.
        editcollege.update(
            name=form.name.data,
            state=form.state.data,
            major=form.major.data,
            tech_grad_year=form.tech_grad_year.data,
            tech_academy=form.tech_academy.data,
            tags=form.tags.data
        )
        # After updating the document, send the user to the updated question using a redirect.
        students = User.objects(role='College Student').all()
        for student in students:
            student.colleges = College.objects(user=student).all()
        return render_template('student_view.html', students=students)

    # if the form has NOT been submitted then take the data from the editquestion object
    # and place it in the form object so it will be displayed to the user on the template.
    form.name.data = editcollege.name
    form.state.data = editcollege.state
    form.major.data = editcollege.major
    form.tech_grad_year.data = editcollege.tech_grad_year
    form.tech_academy.data = editcollege.tech_academy
    form.tags.data = editcollege.tags


    # Send the user to the question form that is now filled out with the current information
    # from the form.
    students = User.objects(role='College Student').all()
    for student in students:
        student.colleges = College.objects(user=student).all()
    return render_template('student_view.html', students=students)
