from model.project import Project
import random


def  test_delete_project(app):
    app.session.login("administrator", "root")
    old_projects_list = app.project.get_project_list()
    if len(old_projects_list) == 0:
        new_project = Project(name="TestProject", description="FIRST Project Description")
        app.project.create(new_project)
    old_projects_list = app.project.get_project_list()
    project_for_del = random.choice(old_projects_list)
    app.project.delete_project(project_for_del)
    new_projects_list = app.project.get_project_list()
    assert len(old_projects_list) == len(new_projects_list) + 1
    old_projects_list.remove(project_for_del)
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)



