# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MarcaBmx(models.Model):
    _name = 'tallerbmx.marca'
    _description = 'Marca de la Bmx'
    id = fields.Integer('id')
    name = fields.Char('Marca', required=True, help='Es obligatorio indicar la marca') #campo obligatorio, y la ayuda lo mostrar como etiqueta flotante
    precio = fields.Float('Precio')
    segnda_mano = fields.Boolean('Segunda mano')
    estado = fields.Selection([
        ('0', 'Bueno'),
        ('1', 'Regular'),
        ('2', 'Malo')
    ], string='Estado')

class ModeloBmx(models.Model):
    _name = 'tallerbmx.modelo'
    _description = 'Modelo de la Bmx'

class Empleado(models.Model):
    _name = 'is.model.taller.empleado'
    _description = 'Empleado dedicado a ciertos modelos'
    
# class tallerbmx(models.Model):
#     _name = 'tallerbmx.tallerbmx'
#     _description = 'tallerbmx.tallerbmx'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
