# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class MarcaVehiculo(models.Model):
    _name = 'taller.marca_vehiculo'
    _description = 'Marca de Vehiculo'

    name = fields.Char(string='Nombre', required=True)


class Vehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Vehiculo'

    name = fields.Char(string='Nombre', required=True)
    placa = fields.Char(string='Placa', required=True)
    marca_id = fields.Many2one(
        comodel_name='taller.marca_vehiculo', string='Marca')

    pasajeros_line_ids = fields.One2many(
        comodel_name='vehiculo.pasajero.line', inverse_name='vehiculo_id',
        string='Pasajeros'
    )

    def copy(self, default=None):
        import ipdb; ipdb.set_trace()
        return super().copy(default)


class VehiculoPasajero(models.Model):
    _name = 'vehiculo.pasajero.line'
    _description = 'Vehiculo Pasajero'

    vehiculo_id = fields.Many2one(
        comodel_name='taller.vehiculo', string='Vehiculo', required=True)
    pasajero_id = fields.Many2one(
        comodel_name='taller.pasajero', string='Pasajero',
        required=True)

    # _sql_constraints = [
    #     ('vehiculo_pasajero_uniq', 'unique(pasajero_id)',
    #      'El pasajero ya se encuentra registrado en un vehiculo')
    # ]


class Pasajero(models.Model):
    _name = 'taller.pasajero'
    _description = 'Pasajero'

    name = fields.Char(string='Nombre', required=True)

class VehiculoHijo(models.Model):
    _name = 'taller.vehiculo_hijo'
    _description = 'Vehiculo Hijo'
    _inherits = {'taller.vehiculo': 'vehiculo_id'}

    vehiculo_id = fields.Many2one(
        comodel_name='taller.vehiculo', string='Vehiculo', required=True, ondelete='cascade')
