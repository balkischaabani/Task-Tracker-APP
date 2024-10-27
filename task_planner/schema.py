import graphene
from graphene_django.types import DjangoObjectType
from .models import Task, Utilisateur, Project, Deadline, Comment

class TaskType(DjangoObjectType):
    class Meta:
        model = Task

class UtilisateurType(DjangoObjectType):
    class Meta:
        model = Utilisateur

class DeadlineType(DjangoObjectType):
    class Meta:
        model = Deadline

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class Query(graphene.ObjectType):
    all_tasks = graphene.List(TaskType)
    all_users = graphene.List(UtilisateurType)
    all_deadlines = graphene.List(DeadlineType)
    all_projects = graphene.List(ProjectType)
    all_comments = graphene.List(CommentType)

    def resolve_all_tasks(self, info, **kwargs):
        return Task.objects.all()

    def resolve_all_users(self, info, **kwargs):
        return Utilisateur.objects.all()

    def resolve_all_deadlines(self, info, **kwargs):
        return Deadline.objects.all()

    def resolve_all_projects(self, info, **kwargs):
        return Project.objects.all()

    def resolve_all_comments(self, info, **kwargs):
        return Comment.objects.all()

class CreateTask(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        descriptionT = graphene.String()
        completed = graphene.Boolean()

    task = graphene.Field(TaskType)

    def mutate(self, info, title, descriptionT, completed):
        task = Task.objects.create(title=title, descriptionT=descriptionT, completed=completed)
        return CreateTask(task=task)

class UpdateTask(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        descriptionT = graphene.String()
        completed = graphene.Boolean()

    task = graphene.Field(TaskType)
    
    def mutate(self, info, id, title, descriptionT, completed):
        task = Task.objects.get(pk=id)
        if title:
            task.title = title
        if descriptionT:
            task.descriptionT = descriptionT
        if completed is not None:
            task.completed = completed
        task.save()
        return UpdateTask(task=task)

class DeleteTask(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    task = graphene.Field(TaskType)

    def mutate(self, info, id):
        task = Task.objects.get(pk=id)
        task.delete()
        return DeleteTask(task=None)

class CreateUtilisateur(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        birth_date = graphene.Date()

    utilisateur = graphene.Field(UtilisateurType)

    def mutate(self, info, first_name, last_name, email, birth_date):
        utilisateur = Utilisateur.objects.create(first_name=first_name, last_name=last_name, email=email, birth_date=birth_date)
        return CreateUtilisateur(utilisateur=utilisateur)

class UpdateUtilisateur(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        birth_date = graphene.Date()

    utilisateur = graphene.Field(UtilisateurType)

    def mutate(self, info, id, first_name, last_name, email, birth_date):
        utilisateur = Utilisateur.objects.get(pk=id)
        if first_name:
            utilisateur.first_name = first_name
        if last_name:
            utilisateur.last_name = last_name
        if email:
            utilisateur.email = email
        if birth_date:
            utilisateur.birth_date = birth_date
        utilisateur.save()
        return UpdateUtilisateur(utilisateur=utilisateur)

class DeleteUtilisateur(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    utilisateur = graphene.Field(UtilisateurType)

    def mutate(self, info, id):
        utilisateur = Utilisateur.objects.get(pk=id)
        utilisateur.delete()
        return DeleteUtilisateur(utilisateur=None)

class CreateDeadline(graphene.Mutation):
    class Arguments:
        date = graphene.Date()

    deadline = graphene.Field(DeadlineType)

    def mutate(self, info, date):
        deadline = Deadline.objects.create(date=date)
        return CreateDeadline(deadline=deadline)

class UpdateDeadline(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        date = graphene.Date()

    deadline = graphene.Field(DeadlineType)

    def mutate(self, info, id, date):
        deadline = Deadline.objects.get(pk=id)
        if date:
            deadline.date = date
        deadline.save()
        return UpdateDeadline(deadline=deadline)

class DeleteDeadline(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    deadline = graphene.Field(DeadlineType)

    def mutate(self, info, id):
        deadline = Deadline.objects.get(pk=id)
        deadline.delete()
        return DeleteDeadline(deadline=None)

class CreateProject(graphene.Mutation):
    class Arguments:
        utilisateur_id = graphene.ID()
        task_id = graphene.ID()
        name = graphene.String()
        descriptionP = graphene.String()
        deadline_id = graphene.ID()

    project = graphene.Field(ProjectType)

    def mutate(self, info, utilisateur_id, task_id, name, descriptionP, deadline_id):
        utilisateur = Utilisateur.objects.get(pk=utilisateur_id)
        task = Task.objects.get(pk=task_id)
        deadline = Deadline.objects.get(pk=deadline_id)
        project = Project.objects.create(utilisateur=utilisateur, task=task, name=name, descriptionP=descriptionP, deadline=deadline)
        return CreateProject(project=project)

class UpdateProject(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        utilisateur_id = graphene.ID()
        task_id = graphene.ID()
        name = graphene.String()
        descriptionP = graphene.String()
        deadline_id = graphene.ID()

    project = graphene.Field(ProjectType)

    def mutate(self, info, id, utilisateur_id, task_id, name, descriptionP, deadline_id):
        project = Project.objects.get(pk=id)
        if utilisateur_id:
            utilisateur = Utilisateur.objects.get(pk=utilisateur_id)
            project.utilisateur = utilisateur
        if task_id:
            task = Task.objects.get(pk=task_id)
            project.task = task
        if name:
            project.name = name
        if descriptionP:
            project.descriptionP = descriptionP
        if deadline_id:
            deadline = Deadline.objects.get(pk=deadline_id)
            project.deadline = deadline
        project.save()
        return UpdateProject(project=project)

class DeleteProject(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    project = graphene.Field(ProjectType)

    def mutate(self, info, id):
        project = Project.objects.get(pk=id)
        project.delete()
        return DeleteProject(project=None)

class CreateComment(graphene.Mutation):
    class Arguments:
        task_id = graphene.ID()
        user_id = graphene.ID()
        text = graphene.String()

    comment = graphene.Field(CommentType)

    def mutate(self, info, task_id, user_id, text):
        task = Task.objects.get(pk=task_id)
        user = Utilisateur.objects.get(pk=user_id)
        comment = Comment.objects.create(task=task, user=user, text=text)
        return CreateComment(comment=comment)

class UpdateComment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        text = graphene.String()

    comment = graphene.Field(CommentType)

    def mutate(self, info, id, text):
        comment = Comment.objects.get(pk=id)
        if text:
            comment.text = text
        comment.save()
        return UpdateComment(comment=comment)

class DeleteComment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    comment = graphene.Field(CommentType)

    def mutate(self, info, id):
        comment = Comment.objects.get(pk=id)
        comment.delete()
        return DeleteComment(comment=None)

class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()
    delete_task = DeleteTask.Field()

    create_utilisateur = CreateUtilisateur.Field()
    update_utilisateur = UpdateUtilisateur.Field()
    delete_utilisateur = DeleteUtilisateur.Field()

    create_deadline = CreateDeadline.Field()
    update_deadline = UpdateDeadline.Field()
    delete_deadline = DeleteDeadline.Field()

    create_project = CreateProject.Field()
    update_project = UpdateProject.Field()
    delete_project = DeleteProject.Field()

    create_comment = CreateComment.Field()
    update_comment = UpdateComment.Field()
    delete_comment = DeleteComment.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
