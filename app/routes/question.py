# These routes are an example of how to use data, forms and routes to create
# a forum where a questions and comments on those questions can be
# Created, Read, Updated or Deleted (CRUD)

from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Question, Comment, Question
from app.classes.forms import QuestionForm, CommentForm, QuestionForm
from flask_login import login_required
import datetime as dt

# This is the route to list all questions
@app.route('/question/list')
@app.route('/questions')
# This means the user must be logged in to see this page
@login_required
def questionList():
    # This retrieves all of the 'questions' that are stored in MongoDB and places them in a
    # mongoengine object as a list of dictionaries name 'questions'.
    questions = Question.objects()
    print(questions)
    # This renders (shows to the user) the questions.html template. it also sends the questions object 
    # to the template as a variable named questions.  The template uses a for loop to display
    # each question.
    return render_template('questions.html',questions=questions)

# This route will get one specific question and any comments associated with that question.  
# The questionID is a variable that must be passsed as a parameter to the function and 
# can then be used in the query to retrieve that question from the database. This route 
# is called when the user clicks a link on questionlist.html template.
# The angle brackets (<>) indicate a variable. 
@app.route('/question/<questionID>')
# This route will only run if the user is logged in.
@login_required
def question(questionID):
    # retrieve the question using the questionID
    thisQuestion = Question.objects.get(id=questionID)
    # If there are no comments the 'comments' object will have the value 'None'. Comments are 
    # related to questions meaning that every comment contains a reference to a question. In this case
    # there is a field on the comment collection called 'question' that is a reference the question
    # document it is related to.  You can use the questionID to get the question and then you can use
    # the question object (thisquestion in this case) to get all the comments.
    theseComments = Comment.objects(question=thisQuestion)
    # Send the question object and the comments object to the 'question.html' template.
    return render_template('question.html',question=thisQuestion,comments=theseComments)

# This route will delete a specific question.  You can only delete the question if you are the author.
# <questionID> is a variable sent to this route by the user who clicked on the trash can in the 
# template 'question.html'. 
# TODO add the ability for an administrator to delete questions. 
@app.route('/question/delete/<questionID>',methods = ['POST'])
# Only run this route if the user is logged in.
@login_required
def questionDelete(questionID):
    # retrieve the question to be deleted using the questionID
    deleteQuestion = Question.objects.get(id=questionID)
    # check to see if the user that is making this request is the author of the question.
    # current_user is a variable provided by the 'flask_login' library.
    if current_user == deleteQuestion.author:
        # delete the question using the delete() method from Mongoengine
        deleteQuestion.delete()
        # send a message to the user that the question was deleted.
        flash('The Question was deleted.')
    else:
        # if the user is not the author tell them they were denied.
        flash("You can't delete a question you don't own.")
    # Retrieve all of the remaining questions so that they can be listed.
    questions = Question.objects()  
    # Send the user to the list of remaining questions.
    return render_template('questions.html',questions=questions)

# This route actually does two things depending on the state of the if statement 
# 'if form.validate_on_submit()'. When the route is first called, the form has not 
# been submitted yet so the if statement is False and the route renders the form.
# If the user has filled out and succesfully submited the form then the if statement
# is True and this route creates the new question based on what the user put in the form.
# Because this route includes a form that both gets and questions data it needs the 'methods'
# in the route decorator.
@app.route('/question/new', methods=['GET', 'POST'])
# This means the user must be logged in to see this page
@login_required
# This is a function that is run when the user requests this route.
def questionNew():
    # This gets the form object from the form.py classes that can be displayed on the template.
    form = QuestionForm()

    # This is a conditional that evaluates to 'True' if the user submitted the form successfully.
    # validate_on_submit() is a method of the form object. 
    if form.validate_on_submit():

        # This stores all the values that the user entered into the new question form. 
        # question() is a mongoengine method for creating a new question. 'newquestion' is the variable 
        # that stores the object that is the result of the question() method.  
        newquestion = Question(
            # the left side is the name of the field from the data table
            # the right side is the data the user entered which is held in the form object.
            subject = form.subject.data,
            content = form.content.data,
            tag = form.tag.data,
            author = current_user.id,
            # This sets the modifydate to the current datetime.
            modify_date = dt.datetime.utcnow
        )
        # This is a method that saves the data to the mongoDB database.
        newquestion.save()

        # Once the new question is saved, this sends the user to that question using redirect.
        # and url_for. Redirect is used to redirect a user to different route so that 
        # routes code can be run. In this case the user just created a question so we want 
        # to send them to that question. url_for takes as its argument the function name
        # for that route (the part after the def key word). You also need to send any
        # other values that are needed by the route you are redirecting to.
        return redirect(url_for('question',questionID=newquestion.id))

    # if form.validate_on_submit() is false then the user either has not yet filled out
    # the form or the form had an error and the user is sent to a blank form. Form errors are 
    # stored in the form object and are displayed on the form. take a look at questionform.html to 
    # see how that works.
    return render_template('questionform.html',form=form)


# This route enables a user to edit a question.  This functions very similar to creating a new 
# question except you don't give the user a blank form.  You have to present the user with a form
# that includes all the values of the original question. Read and understand the new question route 
# before this one. 
@app.route('/question/edit/<questionID>', methods=['GET', 'POST'])
@login_required
def questionEdit(questionID):
    editquestion = question.objects.get(id=questionID)
    # if the user that requested to edit this question is not the author then deny them and
    # send them back to the question. If True, this will exit the route completely and none
    # of the rest of the route will be run.
    if current_user != editquestion.author:
        flash("You can't edit a question you don't own.")
        return redirect(url_for('question',questionID=questionID))
    # get the form object
    form = QuestionForm()
    # If the user has submitted the form then update the question.
    if form.validate_on_submit():
        # update() is mongoengine method for updating an existing document with new data.
        editquestion.update(
            subject = form.subject.data,
            content = form.content.data,
            tag = form.tag.data,
            modify_date = dt.datetime.utcnow
        )
        # After updating the document, send the user to the updated question using a redirect.
        return redirect(url_for('question',questionID=questionID))

    # if the form has NOT been submitted then take the data from the editquestion object
    # and place it in the form object so it will be displayed to the user on the template.
    form.subject.data = editquestion.subject
    form.content.data = editquestion.content
    form.tag.data = editquestion.tag


    # Send the user to the question form that is now filled out with the current information
    # from the form.
    return render_template('questionform.html',form=form)

#####
# the routes below are the CRUD for the comments that are related to the questions. This
# process is exactly the same as for questions with one addition. Each comment is related to
# a specific question via a field on the comment called 'question'. The 'question' field contains a 
# reference to the question document. See the @app.route('/question/<questionID>') above for more details
# about how comments are related to questions.  Additionally, take a look at data.py to see how the
# relationship is defined in the question and the Comment collections.

@app.route('/comment/new/<questionID>', methods=['GET', 'POST'])
@login_required
def question_commentNew(questionID):
    question = question.objects.get(id=questionID)
    form = CommentForm()
    if form.validate_on_submit():
        newComment = Comment(
            author = current_user.id,
            question = questionID,
            content = form.content.data
        )
        newComment.save()
        return redirect(url_for('question',questionID=questionID))
    return render_template('commentform.html',form=form,question=question)

@app.route('/comment/edit/<commentID>', methods=['GET', 'POST'])
@login_required
def question_commentEdit(commentID):
    editComment = Comment.objects.get(id=commentID)
    if current_user != editComment.author:
        flash("You can't edit a comment you didn't write.")
        return redirect(url_for('question',questionID=editComment.question.id))
    question = question.objects.get(id=editComment.question.id)
    form = CommentForm()
    if form.validate_on_submit():
        editComment.update(
            content = form.content.data,
            modifydate = dt.datetime.utcnow
        )
        return redirect(url_for('question',questionID=editComment.question.id))

    form.content.data = editComment.content

    return render_template('commentform.html',form=form,question=question)   

@app.route('/comment/delete/<commentID>')
@login_required
def question_commentDelete(commentID): 
    deleteComment = Comment.objects.get(id=commentID)
    deleteComment.delete()
    flash('The comments was deleted.')
    return redirect(url_for('question',questionID=deleteComment.question.id)) 