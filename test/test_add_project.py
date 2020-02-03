from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects_list = app.project.get_project_list()
    project_new = Project(name="ProjectTest ", description="Project Description")
    app.project.create(project_new)
    new_projects_list = app.project.get_project_list()
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)
