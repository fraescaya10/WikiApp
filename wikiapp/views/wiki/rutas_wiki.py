def rutaswiki(config):
	config.add_route('ver_wiki', '/ver_wikis')
	config.add_route('ver_pag', '/ver_pagina/{uid}')
	config.add_route('add_pag', '/agregar_pagina')
	config.add_route('edi_pag', '/editar_pagina/{uid}')
	config.add_route('elim_pag', '/eliminar_pagina/{uid}')
	config.add_route('logout','/logout')
