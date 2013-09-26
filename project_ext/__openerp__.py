
# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    'name': 'Project Extension',
    'version': '1.0',
    'category': 'Project',
    'description': """
        Este módulo extiende la funcionalidad base del módulo de gestión de proyectos de OpenERP.
        Este módulo está pensado para PYMES que cuya actividad empresarial sea la ejecución de proyectos, y que necesiten un mayor control en cuanto a la dedicación temporal de los empleados de la empresa, a cada uno de los proyectos/tareas/incidencias. 
        Posteriormente ser permite explotar esa información para hacer análisis de dedicación de los empleados a cada uno de los proyectos.
        Además este módulo permite la posibilidad de abrir el ERP a clientes, para que puedan ver el estado actual de los proyectos, y que puedan reportar incidencias.
        
        
        Proyectos:
        - Se permite configurar las categorías y versiones disponibles en el proyecto. Dependiendo de esta configuración se podrán categorizar y versionar las tareas del proyecto.
        - Se permite visualizar el listado de tareas del proyecto desde la ficha.
        
        Tareas:
        - Se muestra el ID de tarea.
        - Se permite ver las incidencias que hay relacionadas con la tarea.
        - Se permite categorizar y versionar la tarea en función de la configuración del proyecto.
        - Se ha agregado la posibilidad de registrar detalladamente los trabajos realizados en una tarea, en vistas a una posible justificación a un cliente.
        - En la vista Kanban se han añadido los campos: ID, usuario asignado, tiempo restante, y prioridad.
        
        Incidencias:
        - Se ha eliminado de la vista el campo versión de incidencia y el botón de Escalar.
        - Se ha establecido una restricción en los campos de información de contacto, para que sólo los puedan ver los grupos Usuario y Responsable.
        
        Análisis de Imputaciones:
        - Se ha creado una pantalla que permite hacer un análisis de las imputaciones de tareas (tiempo), para hacer un seguimiento de las imputaciones del personal.
        - Hay habilitados numerosos filtros y niveles de agrupación, para explotar la información según convenga.
        
        Tipos de Imputaciones:
        - Tabla maestra donde se registran los tipos de imputaciones habilitados, con el fin de poder categorizar cada imputación.
        
        Versiones de Proyecto:
        - Tabla maestra donde se registran las diferentes versiones, que permiten agrupar las tareas en paquetes de versiones.
        
        Catergorías de Tarea:
        - Tabla maestra donde se registran las diferentes categorías, con el fin de categorizar las tareas.
        - Estas categorías se asignan a nivel de proyecto.
        
        Departamentos de Recursos Humanos:
        - Se ha agregado un nivel de agrupación por departamento padre, para poder visualizar de forma jerárquica el árbol departamental de la empresa.

        Grupo de Clientes:
        - Se agrega un nuevo grupo de usarios para los Clientes.
        
        Reglas de Acceso para Grupo Clientes:
        - Se definen reglas de acceso para el grupo clientes, de la siguiente forma:
          - Ver Proyectos de los que el cliente es miembro.
          - Ver Tareas asociadas a los proyectos de los que el cliente es miembro.
          - Ver, Crear y Modificar Incidencias asociadas a los proyectos de los que el cliente es miembro.
        
        Elementos de menú para Grupo Clientes:
        - Se ha creado una estructura de elementos de menú propias para los clientes, de la siguiente forma:
          - Proyectos
            - Proyectos
              - Proyectos
              - Tareas
              - Incidencias

        NOTA: Usuarios que se vayan a asignar al grupo de clientes, deberán estar configurados también como Vista Extendida, para que el cliente pueda ver las pestañas de Comunicación e Historial, e Información Extra, de las Incidencias.
    """,
    'author': 'Radmas Technologies S.L.',
    'maintainer': 'Radmas Technologies S.L.',
    'website': 'http://www.radmas.com',
    'depends': ['base', 'project', 'project_issue'],
    'init_xml': [],
    'update_xml': [
        'security/project_security_ext.xml',
        'project_task_ext_view.xml',
        'project_task_work_type_view.xml',
        'project_version_view.xml',
        'project_project_ext_view.xml',
        'project_task_category_view.xml',
        'project_task_activity_view.xml',
        'project_issue_ext_view.xml',
        'hr_department_ext_view.xml',
        'report/project_task_work_report_view.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'active': False,
}