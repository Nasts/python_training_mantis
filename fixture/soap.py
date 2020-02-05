from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        wd = self.app.wd
        сlient = Client(self.app.base_url + "/api/soap/mantisconnect.php" + "?wsdl")
        try:
            сlient.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_soap_list(self, username, password):
        wd = self.app.wd
        сlient = Client(self.app.base_url + "/api/soap/mantisconnect.php" + "?wsdl")
        try:
            return сlient.service.mc_projects_get_user_accessible(username, password)
        except WebFault:
            return []
