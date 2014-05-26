from pyramid.security import (
	Allow,
	Everyone,
)

class RootFactory(object):
	# acl = access control list -> tiene dos access control entry
	__acl__ = [ (Allow, 'group:viewers','view'),# Permitir ver a cualquiera
			    (Allow, 'group:editors','view'),
			    (Allow, 'group:editors','edit') ]# Permitir a usuarios del grupo editores editar			
	def __init__ (self, request):
		pass
