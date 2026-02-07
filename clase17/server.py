# Ejemplo de servidor MCP con Fast MCP
from fastmcp import FastMCP

server = FastMCP(name='ServidorMCP')


@server.tool
def get_status():
  return 'El servidor está ejecutándose correctamente.'


@server.tool
def get_user_info(user_id):
  return f'Información del usuario {user_id}.'


# Herramienta para raíces cuadradas
@server.tool
def calcular_raiz(numero):
  return numero**0.5


# Configuración de endpoints múltiples
tools_endpoints = {
  'weather_tool': 'weather.service.example.com',
  'database_tool': 'database.service.example.com',
}
