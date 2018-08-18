import pygit2
import os
from database import *


class Repo:
	def __init__(self,repo_url,repo_branch='master',new_repo=False,repo_path,access_method='ssh',**kwargs):
		self.repo_url = repo_url
		self.repo_branch = repo_branch
		self.repo_path = repo_path
		self.repo_name = self.repo_url.split('/')[len(self.repo_url.split('/'))-1]
		self.access_method = access_method
		if self.access_method == 'https':
			userpass = pygit2.UserPass(kwargs['username'],kwargs['access_key'])
			self.callbacks = pygit2.RemoteCallbacks(credentials=self.userpass)
		else:
			# "all" (that's gonna get proven wrong,just you watch) 
			# git servers just hardcode git as the pubkey auth user
			keypair = pygit2.Keypair('git',kwargs['access_key']+'.pub',kwargs['access_key'],'')
			self.callbacks = pygit2.RemoteCallbacks(credentials=keypair)
		
		try:
			self.repo = pygit2.Repository(self.repo_path+'/'+self.repo_name)
		except KeyError:
			# if no repo found
			self.repo = self.clone_repo()

	def clone_repo(self):
		pygit2.clone_repository(self.repo_url,self.repo_path+'/'+self.repo_name,callbacks=self.callbacks)

	def update_repo(self):
		for remote in repo.remotes:
			# pull from remote repo branch
			if remote.name == self.repo_branch:
				


