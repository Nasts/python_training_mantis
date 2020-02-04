from model.project import Project
import random


def  test_delete_project(app):
    app.session.login("administrator", "root")
    # old_projects_list = app.project.get_project_list()
    old_projects_list = app.soap.get_soap_list("administrator", "root")
    if len(old_projects_list) == 0:
        new_project = Project(name="TestProject", description="FIRST Project Description")
        app.project.create(new_project)
    old_projects_list_for_choice = app.project.get_project_list()
    old_projects_list = app.soap.get_soap_list("administrator", "root")
    project_for_del = random.choice(old_projects_list_for_choice)
    app.project.delete_project(project_for_del)
    new_projects_list = sorted(app.soap.get_soap_list("administrator", "root"), key=Project.id_or_max)
    assert len(old_projects_list) == len(new_projects_list) + 1
    old_projects_list.remove(project_for_del)
    assert app.project.compare(old_projects_list, new_projects_list)



