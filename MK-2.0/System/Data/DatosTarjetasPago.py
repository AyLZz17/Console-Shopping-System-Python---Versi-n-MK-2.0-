"""
 ============================================================
 DatosTarjetasPago.py
 ------------------------------------------------------------
 Este archivo contiene tarjetas de pago simuladas para el
 sistema de compras en consola.

 Cada tarjeta tiene:
   - "numero": un número identificador de la tarjeta (string).
   - "saldo":  el saldo disponible para compras (float/int).

 IMPORTANTE:
   - Este archivo simula una base de datos de tarjetas.
   - Los datos son estáticos y no se guardan cambios permanentes.
   - Cada vez que reinicies el programa, los saldos se restauran.
 ============================================================
"""
tarjetas = {
    
    "tar1": {"numero":"001", "saldo":100},
    "tar2": {"numero":"002", "saldo":50},
    "tar3": {"numero":"003", "saldo":500},
    "tar4": {"numero":"004", "saldo":300},
    "tar5": {"numero":"005", "saldo":20}
            
            }

