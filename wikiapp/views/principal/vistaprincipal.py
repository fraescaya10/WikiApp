from pyramid.response import Response
from pyramid.view import (
    view_config,
    forbidden_view_config,
    )
from pyramid.security import (
    remember,
    forget,
    )   

from sqlalchemy.exc import DBAPIError

from pyramid.httpexceptions import(
    HTTPFound,
    HTTPNotFound,
    )

from wikiapp.models.principal import DBSession
from wikiapp.models.wiki import Pagina
from wikiapp.utils.security import USERS

@view_config(route_name="home", renderer="templates/principal/principal.jinja2")
@forbidden_view_config(renderer="templates/principal/principal.jinja2")
def vista_principal(request): 
    if "ingreso" in request.params:
        usuario = request.params['login']
        clave = request.params['password']        
        if USERS.get(usuario) == clave:
            headers = remember(request,usuario)
            return HTTPFound(location=request.route_url('ver_wiki'),headers=headers) # Esto se hace al hacer click en el boton ingresar   
    elif request.authenticated_userid is not None:
        return HTTPFound(location=request.route_url('ver_wiki'))    
    return {'estado':1,'vista':'Principal'}

@view_config(route_name="acerca", renderer="templates/principal/acerca.jinja2")
def acercade(request):
    return {'estado':1,'vista':'Acerca'}

@view_config(route_name="logout")
def logout(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('home'),headers=headers)
