import time
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    projects_cache = None

    def open_manage_proj(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/manage_proj_page.php')):
            wd.get("http://localhost:8080/mantisbt-1.2.20/manage_proj_page.php")
        time.sleep(1)

    def create(self, project):
        wd = self.app.wd
        self.open_manage_proj()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_project_list(self):
        if self.projects_cache is None:
            wd = self.app.wd
            self.open_manage_proj()
            self.projects_cache = []
            for row in wd.find_elements_by_xpath(
                    "//table[@class='width100'][2]/tbody/tr[(@class='row-1'|@class='row-2')]"):
                projects = row.text
                list_of_projects = projects.split(" ")
                name = list_of_projects[0]
                # description = list_of_projects[5]
                self.projects_cache.append(Project(name=name))
            self.projects_cache.pop(0)
        return self.projects_cache

    def delete_project(self, project_for_del):
        wd = self.app.wd
        wd.find_element_by_link_text(project_for_del.name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        time.sleep(1)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.projects_cache = None















