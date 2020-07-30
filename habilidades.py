from flask import Flask, request
from flask_restful import Resource, Api
import json

lista_habilidades = ['Python','C++','Java','Django']

class habilidades(Resource):
    def get(self):
        return lista_habilidades
