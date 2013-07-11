
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

from osv import osv
from osv import fields
from tools.translate import _
import time


class project_task_activity(osv.osv):

    _name = 'project.task.activity'
    _description = 'Project Task Activity'
   
    _columns = {# Texto
                'text': fields.text('Text', required=True),
                # Fecha
                'date': fields.date('Date', required=True),
                # Usuario
                'user_id': fields.many2one('res.users', 'User', required=True),
                # Tarea
                'task_id': fields.many2one('project.task', 'Task'),
                }
    
    _defaults = {
        'date': lambda *a: time.strftime('%Y-%m-%d'),
        'user_id': lambda self, cr, uid, ctx: uid
        }
    
project_task_activity()