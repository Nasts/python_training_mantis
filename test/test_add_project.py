from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    # old_projects_list = app.project.get_project_list()
    old_projects_list = app.soap.get_soap_list("administrator", "root")
    project_new = Project(name="TestNew", description="Project Description")
    app.project.create(project_new)
    # new_projects_list = app.project.get_project_list()
    new_projects_list = sorted(app.soap.get_soap_list("administrator", "root"), key=Project.id_or_max)
    old_projects_list.append(project_new)
    old_projects_list = sorted(app.soap.get_soap_list("administrator", "root"), key=Project.id_or_max)
    assert app.project.compare(old_projects_list, new_projects_list)
