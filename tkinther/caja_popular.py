import tkinter as tk

class Cuenta:
    def __init__(self, numero, titular, edad, saldo):
        self.numero = numero
        self.titular = titular
        self.edad = edad
        self.saldo = saldo
        
    def consultar_saldo(self):
        return self.saldo

    def ingresar_efectivo(self, cantidad):
        self.saldo += cantidad

    def retirar_efectivo(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def depositar_otra_cuenta(self, cuenta_destino, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            cuenta_destino.ingresar_efectivo(cantidad)
        else:
            print("Saldo insuficiente")