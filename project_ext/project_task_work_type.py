
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

from osv import osv, fields

class project_task_work_type(osv.osv):
    """
    Tipo de trabajo de tarea (tipo de imputación)
    """
    _name = 'project.task.work.type'
    
    _columns = {                
        'sequence': fields.integer('Sequence'),
        'name': fields.char('Name', size=128, required=True),
    }
    _defaults = {
        'sequence': 1
    }

project_task_work_type()