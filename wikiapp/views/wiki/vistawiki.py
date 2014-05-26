from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import(
    HTTPFound,
    HTTPNotFound,
    )

from sqlalchemy.exc import DBAPIError
from wikiapp.models.principal import DBSession
from wikiapp.models.wiki import Pagina

@view_config(route_name="ver_wiki", renderer="templates/wiki/ver_wiki.jinja2",permission='view')
def ver_wiki(request):
	permiso = request.has_permission('edit')
	paginas = DBSession.query(Pagina).order_by(Pagina.uid)	
	return{'estado':1,'paginas':paginas ,'permiso':permiso}

@view_config(route_name="ver_pag", renderer="templates/wiki/ver_pag.jinja2",permission='view')
def ver_pag(request):
	permiso = request.has_permission('edit')
	uid = int(request.matchdict['uid'])
	pagina = DBSession.query(Pagina).filter_by(uid=uid).one()
	if 'regresa' in request.params:
		return HTTPFound(request.route_url('ver_wiki'))
	elif 'edita' in request.params:
		return HTTPFound(request.route_url('edi_pag',uid=uid))
	elif 'elimina' in request.params:
		return HTTPFound(request.route_url('elim_pag',uid=uid))
	return{'estado':1,'pagina':pagina,'permiso':permiso}
	
@view_config(route_name="add_pag", renderer="templates/wiki/creaedit_wiki.jinja2",permission='edit')
def add_wiki(request):	
	permiso = request.has_permission('edit')
	if 'guarda' in request.params:
		nombre = request.params['nombre']
		detalle = request.params['detalle']
		pagina = Pagina(nombre=nombre,detalle=detalle)
		DBSession.add(pagina)
		return HTTPFound(request.route_url('ver_wiki'))
	elif 'cancela' in request.params:
		return HTTPFound(request.route_url('ver_wiki'))
	return{'estado':1,'titulo':u'Crear pagina','pagina':{}, 'permiso':permiso}

@view_config(route_name="edi_pag", renderer="templates/wiki/creaedit_wiki.jinja2",permission='edit')
def edit_wiki(request):
	permiso = request.has_permission('edit')
	uid = int(request.matchdict['uid'])
	pagina = DBSession.query(Pagina).filter_by(uid=uid).one()
	if 'guarda' in request.params:
		pagina.nombre = request.params['nombre']
		pagina.detalle = request.params['detalle']
		DBSession.add(pagina)
		return HTTPFound(request.route_url('ver_wiki'))
	elif 'cancela' in request.params:
		return HTTPFound(request.route_url('ver_pag',uid=uid))
	return{'estado':1,'titulo':u'Editar pagina','pagina':pagina, 'permiso':permiso}
	
@view_config(route_name="elim_pag",permission='edit')
def elim_wiki(request):
	uid = int(request.matchdict['uid'])
	pagina = DBSession.query(Pagina).filter_by(uid=uid).one()
	DBSession.delete(pagina)
	return HTTPFound(request.route_url('ver_wiki'))

