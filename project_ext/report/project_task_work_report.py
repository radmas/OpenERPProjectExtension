
# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields,osv
import tools

class project_task_work_report(osv.osv):
    _name = "project.task.work.report"
    _auto = False

    _columns = {
        'name': fields.char('Name', size=64, required=False, readonly=True),
        'day': fields.char('Day', size=128, readonly=True),
        'month':fields.selection([('01', 'January'), ('02', 'February'), \
                                  ('03', 'March'), ('04', 'April'),\
                                  ('05', 'May'), ('06', 'June'), \
                                  ('07', 'July'), ('08', 'August'),\
                                  ('09', 'September'), ('10', 'October'),\
                                  ('11', 'November'), ('12', 'December')], 'Month', readonly=True),
        'year': fields.char('Year', size=128, readonly=True),
        'hours': fields.float('Hours', size=64, required=False, readonly=True),
        'date': fields.date('Date'),
        'company_id': fields.many2one('res.company', 'Company', readonly=True),
        'project_id':fields.many2one('project.project', 'Project',readonly=True),
        'user_id' : fields.many2one('res.users', 'Assigned to',readonly=True),
        'task_id': fields.many2one('project.task', 'Task'),
        'task_category_id': fields.many2one('project.task.category', 'Task'),
        'work_type_id': fields.many2one('project.task.work.type', 'Task'),
    }

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'project_task_work_report')
        cr.execute("""
            CREATE OR REPLACE VIEW project_task_work_report AS (
                SELECT
                    c.id as id,
                    c.name as name,
                    to_char(c.create_date, 'YYYY') as year,
                    to_char(c.create_date, 'MM') as month,
                    to_char(c.create_date, 'DD') as day,
                    c.hours as hours,
                    c.date as date,
                    c.company_id as company_id,
                    (SELECT project_id FROM project_task WHERE id=c.task_id) AS project_id,                    
                    c.task_id,
                    c.user_id as user_id,
                    (SELECT project_task_category_id FROM project_task WHERE id=c.task_id) AS task_category_id,
                    c.work_type_id as work_type_id

                FROM
                    project_task_work c
            )""")

project_task_work_report()