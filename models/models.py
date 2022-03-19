# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class mimodulo(models.Model):
#     _name = 'mimodulo.mimodulo'
#     _description = 'mimodulo.mimodulo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date

class camion(models.Model):
    _name = 'transportes.camion'
    _description = 'Permite definir características de un camión'

    name = fields.Char("Matrícula", required=True, size=7)
    marca = fields.Char("Marca", required=True)
    modelo = fields.Char("Modelo", required=True)
    potencia = fields.Integer()
    color = fields.Char(help='Color of the vehicle')
    fecha_compra = fields.Date('Fecha de matriculación', required=False, default=fields.Date.today) 
    
    

    #Relacion entre camion y viaje
    viajes_camion = fields.One2many('transportes.viaje', 'camion', string='Viajes')


    #Campo calculado años, en base a la fecha de matriculacion, video odoo whatsapp
    antiguedad = fields.Integer('Años', compute='get_antiguedad')
    @api.depends('fecha_compra')
    def get_antiguedad(self):
        for camion in self:
            fecha_actual = date.today()
            camion.antiguedad = relativedelta(fecha_actual, camion.fecha_compra).years

    


class viaje(models.Model):
    _name = 'transportes.viaje'
    _description = 'Permite definir características de un viaje'

    #Relacion con el conductor que realiza el viaje
    conductor = fields.Many2one('hr.employee', string='Conductor', help='Conductor del camión', required=True)
    
    #Relacion entre el viaje y el camion que lo entregará
    camion = fields.Many2one('transportes.camion', string='Camión', help='Camión que realizará el viaje', required=True)


    provincia = fields.Selection([
        ('lacoruna', 'A Coruña'),
        ('alava', 'Álava'),
        ('albacete', 'Albacete'),
        ('alicante', 'Alicante'),
        ('almeria', 'Almería'),
        ('asturias', 'Asturias'),
        ('avila', 'Ávila'),
        ('badajoz', 'Badajoz'),
        ('baleares', 'Baleares'),
        ('barcelona', 'Barcelona'),
        ('lacoruna', 'A Coruña'),
        ('burgos', 'Burgos'),
        ('caceres', 'Cáceres'),
        ('cadiz', 'Cádiz'),
        ('cantabria', 'Cantabria'),
        ('castellon', 'Cstellón'),
        ('ceuta', 'Ceuta'),
        ('ciudadReal', 'Ciudad Real'),
        ('córdoba', 'Córdoba'),
        ('cuenca', 'Cuenca'),
        ('gerona', 'Gerona'),
        ('granada', 'Granada'),
        ('guadalajara', 'Guadalajara'),
        ('gipuz', 'Guipúzcoa'),
        ('huelva', 'Huelva'),
        ('huesca', 'Huesca'),
        ('jaen', 'Jaén'),
        ('larioja', 'La Rioja'),
        ('palmas', 'Las Palmas'),
        ('leon', 'León'),
        ('lerida', 'Lérida'),
        ('lugo', 'Lugo'),
        ('madrid', 'Madrid'),
        ('malaga', 'Málaga'),
        ('melilla', 'Melilla'),
        ('murcia', 'Murcia'),
        ('navarra', 'Navarra'),
        ('caceres', 'Cáceres'),
        ('ourense', 'Ourense'),
        ('palencias', 'Palencia'),
        ('pontevedra', 'Pontevedra'),
        ('salamanca', 'Salamanca'),
        ('tenerife', 'Tenerife'),
        ('segovia', 'Segovia'),
        ('sevilla', 'Sevilla'),
        ('soria', 'Soria'),
        ('tarragona', 'Tarragona'),
        ('terual', 'Terual'),
        ('toledo', 'Toledo'),
        ('valencia', 'Valencia'),
        ('valladolid', 'Valladolid'),
        ('vizcaya', 'Vizcaya'),
        ('zamora', 'Zamora'),
        ('zaragoza', 'Zaragoza')], string='Provincia de destino', required=True)

    ciudad = fields.Char(string='Ciudad de destino')

    destinatario = fields.Many2one('res.partner', string='Destinatario', required=True)
    mercancia = fields.Many2one('product.product', string='Mercancía a entregar', required=True) 
    entregado = fields.Selection([('noEntregado', 'No entregado'),('entregado', 'Entregado')],string='Entregado', default='noEntregado', required=True)
    
    other = fields.Text(string='Información adicional')
    


   

class conductor(models.Model):
    _inherit = 'hr.employee'
    

    #Viajes realizados por el conductor, la relacion existe pero falta implementarla en la vista
    viajes_conductor = fields.One2many('transportes.viaje', 'conductor', string='Viajes realizados por el conductor')
    carnet = fields.Selection([('c1', 'C1'),('c1e', 'C1 + E'),('c', 'C'),('ce', 'C + E')],string='Tipo de Carnet', required=True)
    