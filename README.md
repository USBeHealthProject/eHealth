**********************************************
*************** SISTEMA eHEALTH **************
**********************************************


requerimientos: archivo requirements.txt
version python: python2.7

Ambiente virtual:
    - instalar virtualenvwrapper
    - crear entorno virtual: mkvirtualenv --no-site-packages -r requirements.txt <NombreEntornoVirtual>

para ejecutar: ./manage.py runserver


* PARA PRUEBAS DE SELENIUM *
selenium==2.53.6
firefox=41.0.2+build2-0ubuntu1

crear un usuario medico con username "rr" y password "rr"
o modificarlo en el codigo


* PARA LAS BUSQUEDAS *
Para crear el index que usa el search engine:
     manage.py rebuild_index
