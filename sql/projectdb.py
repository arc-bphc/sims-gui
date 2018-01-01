from .insert_data_users import *
import datetime
class projectDB:
	def __init__(self,dbname):
		self.user=db(dbname)
	
	def getProjectsList(self):
		self.project_list = self.user.selectQuery('Projects',['*'])
		return self.project_list
	def updateProject(self,project_id,name,lead_id):
		if name=='' or lead_id==None:
			return 0
		self.user.updateQueryNew('Projects',[str(name),str(lead_id)],['Name','Lead_ID'],['Project_ID='+str(project_id)])
		return 1
	def newProject(self,name,lead_id):
		if name=='' or lead_id==None:
			return 0
		try:
			id_list = [i[0] for i in self.project_list]
			project_id=max(id_list)+1
		except:
			project_id=1
		self.user.insertTuple('Projects',[project_id,name,lead_id],['Project_ID','Name','Lead_ID'])
		return 1
	def deleteProject(self,project_id,lead_id):
		if project_id==None or lead_id==None:
			return 0	
		self.user.deleteQuery('Projects',['Project_ID='+str(project_id)])
		return 1
