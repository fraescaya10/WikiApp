from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from wikiapp.utils.security import groupfinder

from wikiapp.models.principal import (
    DBSession,
    Base,
    )
from wikiapp.views.principal.rutas_principal import rutasprincipal 
from wikiapp.views.wiki.rutas_wiki import rutaswiki 


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    authn_policy = AuthTktAuthenticationPolicy('sosecret',
                                                callback=groupfinder,
                                                hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings,root_factory='wikiapp.models.login.RootFactory')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    # Agregando las rutas
    rutasprincipal(config)
    rutaswiki(config)
    config.scan()
    return config.make_wsgi_app()
