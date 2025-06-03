def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem vindo, Adiministrador')
    else:
        print('Bem vindo, Usuário')

loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')