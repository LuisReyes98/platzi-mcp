# Curso de Model Context Protocol (MCP) en Platzi

repositorio del curso: https://github.com/platzi/curso-mcp

Docs de Fast MCP https://gofastmcp.com/getting-started/welcome

https://thetalkingapp.medium.com/optimizing-api-output-for-use-as-tools-in-model-context-protocol-mcp-07d93a084fbc

# Clase 1


Resumen
La revolución de la inteligencia artificial no está en los modelos más grandes, sino en la forma en que nos comunicamos con ellos. El Model Context Protocol (MCP) representa un cambio de paradigma en cómo interactuamos con sistemas de IA, transformando desarrolladores en arquitectos de sistemas inteligentes. Este protocolo establece el puente crucial entre nuestro código y los modelos de lenguaje avanzados, abriendo posibilidades que van mucho más allá de simples consultas a ChatGPT.

¿Qué es el Model Context Protocol y por qué es importante?
El Model Context Protocol (MCP) es el estándar que permite que el software se comunique con sistemas de inteligencia artificial de manera integrada y eficiente. Similar a lo que representó HTTP para la web en los años noventa, MCP está posicionándose como el protocolo fundamental que dominarán los líderes en el desarrollo de IA.

Este protocolo no es simplemente una herramienta más, sino la base para construir productos inteligentes, escalables y conversacionales. A diferencia de enfoques tradicionales, MCP reconoce que el futuro de la inteligencia artificial no depende de un modelo aislado, sino de un ecosistema completo e interconectado.

La importancia de MCP radica en su capacidad para crear una arquitectura cliente-servidor específica para IA, donde:

El cliente puede ser un editor de código, un navegador web o incluso un bot de voz.
El servidor actúa como orquestador de inteligencia artificial, definiendo contextos y controlando respuestas.
¿Cómo implementar MCP en tus proyectos?
La implementación de MCP es sorprendentemente accesible, incluso para desarrolladores que apenas comienzan a explorar el campo de la inteligencia artificial. El proceso puede dividirse en etapas concretas y manejables:

En 10 minutos: Configurar tu primer servidor MCP funcionando.
En 20 minutos: Lograr integración con un modelo de lenguaje.
En menos de una hora: Desplegar a producción utilizando Server Send Events (SSE).
Herramientas como VS Code se transforman en clientes inteligentes dentro de este ecosistema, mientras que servicios como Azure OpenAI se convierten en proveedores de la capacidad computacional necesaria. Lo verdaderamente revolucionario es que tú mantienes el control sobre aspectos críticos como:

Qué contexto se almacena.
Cómo se optimizan las respuestas.
De qué manera se enrutan las solicitudes.
Funcionalidades avanzadas del protocolo
MCP ofrece capacidades sofisticadas que transforman completamente la manera en que desarrollamos aplicaciones basadas en IA:

RootContext: Permite mantener conversaciones persistentes, conservando el historial y contexto de interacciones previas.
Enrutamiento inteligente: Facilita la distribución de tareas entre diversos agentes de IA según su especialización.
Arquitectura cliente-servidor: Separa claramente las responsabilidades entre la interfaz de usuario y el procesamiento de la inteligencia artificial.
¿Por qué aprender MCP cambia tu rol como desarrollador?
Dominar MCP representa un cambio fundamental en tu relación con la inteligencia artificial. Ya no serás simplemente un usuario de IA, sino un arquitecto de sistemas inteligentes. Esta transformación tiene implicaciones profundas:

Tu código deja de ejecutarse de manera aislada para integrarse en un sistema cognitivo completo.
Adquieres control sobre cómo los modelos de lenguaje interpretan y responden a las solicitudes.
Puedes desarrollar aplicaciones con conversaciones persistentes y contextualmente ricas.
Los productos más innovadores de los próximos años no se construirán únicamente con APIs tradicionales. El futuro pertenece a quienes dominen:

Protocolos de control de mensajes como MCP.
Arquitecturas persistentes para mantener el contexto conversacional.
Herramientas de integración multimodal que combinen diferentes formas de procesamiento de información.
Este cambio de paradigma representa una oportunidad única para los desarrolladores que estén dispuestos a adaptarse. La pregunta ya no es si deberías aprender a trabajar con MCP, sino cuándo comenzarás a hacerlo, porque la revolución de la IA conversacional ya está en marcha.

El dominio del Model Context Protocol abre las puertas a un nuevo nivel de desarrollo en inteligencia artificial, permitiéndote crear soluciones más sofisticadas, contextuales y naturales. ¿Estás listo para dar el salto de usuario a creador? El futuro de la IA espera por aquellos dispuestos a construir los cimientos de la próxima generación de aplicaciones inteligentes.

# Clase 2

Resumen
El protocolo MCP comprende varios conceptos imprescindibles que, al dominarlos, facilitan enormemente la programación en cualquier lenguaje deseado. Conocer estos principios permite gestionar sin dificultad cualquier implementación relacionada con MCP.

¿Qué es un servidor y cuál es su función en MCP?
El servidor es un componente fundamental en el protocolo MCP. Su rol principal es integrar todas las piezas que se quieran gestionar en MCP. Funciona recibiendo solicitudes y generando respuestas usando diferentes fuentes de información:

Información contextual: obtenida mediante conversaciones o interacción con algún LLM.
Fuentes de conocimiento externas: documentos y enlaces externos.
Archivos locales: interacciones específicas con archivos almacenados localmente.
APIs o servicios web: comunicación con servicios externos para extraer información.
¿Cómo interactúan cliente y host con el servidor en MCP?
El cliente desempeña la tarea de recibir y estructurar las respuestas del servidor para presentarlas de forma clara y comprensible. Primero, recibe la pregunta del usuario, la procesa y realiza una petición apropiada al servidor. Posteriormente, recibe la respuesta del servidor y la transforma a un formato amigable.

Finalmente, el host es la interfaz que permite la interacción directa de los usuarios con MCP. Es el elemento final donde el cliente presenta la información procesada. Ejemplos comunes de host incluyen diversas aplicaciones y entornos de desarrollo integrados como VS Code, Visual Studio o Eclipse.

¿Cuál es el flujo detallado de información dentro del MCP?
El flujo de información inicia con una pregunta del usuario específica al contexto del MCP activo. El cliente procesa esta pregunta, transfiere la solicitud al servidor, y este utiliza de manera autónoma las cuatro fuentes de información para generar una respuesta adecuada. Luego, el cliente estructura dicha respuesta, transfiriéndola posteriormente al host para su presentación final al usuario.

Este flujo se resume en:

El usuario formula la pregunta en función del contexto del MCP.
El cliente interpreta la pregunta y solicita información al servidor.
El servidor analiza las fuentes de información disponibles y genera una respuesta.
El cliente reorganiza esa respuesta de manera organizada y clara.
El host presenta la información procesada al usuario.
Comprender claramente estas bases te permite aplicar fácilmente estos conceptos dentro del código, tarea que será abordada más adelante en clases posteriores.

Te invito a compartir tus dudas y sugerencias en los comentarios para seguir profundizando en estos conceptos esenciales del MCP.

# Clase 16 Gestión de contexto dinámico en agentes de IA con MCP y Python

## Resumen

El contexto es clave al hablar de agentes con inteligencia artificial, especialmente cuando diferenciamos un simple bot conversacional de un agente verdaderamente inteligente. La capacidad para mantener el contexto es fundamental, pues permite relacionar preguntas previas con conversaciones actuales, mejorando significativamente la precisión y relevancia de las respuestas.

¿Por qué el contexto mejora un agente de IA?
El contexto permite que un agente relacione información actual con interacciones anteriores, brindando respuestas más naturales y coherentes. Por ejemplo, si primero hablas de Superman y luego introduces a Batman en la conversación, un agente que maneja contexto adecuadamente podría señalar la relación amistosa entre ambos personajes, añadiendo valor y naturalidad a la interacción.

¿Cómo implementar contexto dinámico con MCP y Python?
Implementar una gestión sencilla del contexto en tu agente inteligente utilizando MCP (Modelo de Contexto Persistente) en Python implica tres sencillos pasos prácticos:

Creando servidor y contexto raíz
Primero debes crear una carpeta denominada clase16 sin espacios y dentro de esta un archivo del servidor MCP con extensión .py.
Importa la librería MCP, inicializando después el servidor junto al contexto raíz (root context). Este último comienza acumulando información desde el principio.
import mcp.server.fastmcpy

# Inicialización del servidor
root_context = {"bienvenida": "Bienvenido"}
Creando herramienta para actualizar el contexto
Define una herramienta específica, denominada UpdateContext, que actualiza dinámicamente tu contexto raíz cada vez que se recibe información nueva del usuario.
Los datos proporcionados se almacenan automáticamente en el diccionario.
def UpdateContext(user_data):
    root_context.update(user_data)
Ejecutando y visualizando el contexto actualizado
Ejecuta tu servidor MCP y observa cómo el contexto se actualiza con cada entrada del usuario.
Al utilizar la herramienta desde el explorador, verás cómo el contenido se va acumulando secuencialmente, proporcionando a tu modelo de lenguaje avanzado información más robusta y detallada para sus respuestas.
Este método es sencillo para implementar y provee una interacción más natural y precisa entre usuarios y agentes de inteligencia artificial avanzados, permitiendo contextos más completos y respuestas acordes con las expectativas del usuario.

¿Tienes experiencia manejando contextos en tus aplicaciones de inteligencia artificial? ¡Comparte tus comentarios abajo!


# Clase 18 Enrutamiento de herramientas con MCP Server

Resumen
¿Te has preguntado cómo optimizar el uso de múltiples herramientas en un servidor MCP para mejorar tus aplicaciones y procesos? El enrutamiento con MCP Server te permite acceder a diferentes herramientas según las necesidades específicas de tu trabajo, mejorando eficiencia y organización.

¿Qué es el enrutamiento en MCP Server?
El enrutamiento es una funcionalidad del MCP Server que organiza y administra la manera en que accedes a diversas herramientas o recursos desde una misma interfaz. Funcionan de manera similar a una API, donde tú eliges cuál método utilizar según lo que necesites.

¿Cómo utilizar las herramientas del MCP Server?
Las herramientas incluidas en MCP Server se configuran fácilmente a través de aplicaciones Python que usan Fast MCP. Puedes crear distintos endpoints, configurar parámetros personalizados y obtener resultados al interactuar con herramientas diversas.

Entre los ejemplos prácticos se encuentran:

Herramienta de chequeo de estado de servidor (get status).
Recuperación de información de usuario (get user info).
Función de cálculo de operaciones matemáticas (como raíces cuadradas).
```python
# Ejemplo de servidor MCP con Fast MCP
from fast_mcp import MCPServer

server = MCPServer(name='ServidorMCP')

@server.tool
def get_status():
    return "El servidor está ejecutándose correctamente."

@server.tool
def get_user_info(user_id):
    return f"Información del usuario {user_id}."
```

```python
# Herramienta para raíces cuadradas
@server.tool
def calcular_raiz(numero):
    return numero ** 0.5
```
¿Cómo definir múltiples endpoints en MCP Server?
Si trabajas con varios servicios externos como bases de datos, servicios climáticos u otras APIs, puedes utilizarlos todos desde un mismo servidor mediante el enrutamiento por endpoints.

Cada uno de estos endpoints está vinculado a una URL específica:

weather service: para información climática.
database service: para consultas de base de datos.
```python

# Configuración de endpoints múltiples
tools_endpoints = {
    "weather_tool": "weather.service.example.com",
    "database_tool": "database.service.example.com",
}
```

Esto permite con facilidad y eficacia decidir a qué servicio se dirige una solicitud específica, optimizando el trabajo con diferentes recursos, aun cuando la ejecución se realice desde una sola herramienta.

¿Cómo comprobar el enrutamiento en MCP Server?
Puedes verificar fácilmente que tu enrutamiento funcione con diferentes pruebas para cada herramienta y endpoint. Por ejemplo, si pruebas una herramienta llamada "Weather Tool":

```python
tool_name = "Weather Tool"
parameters = { "city": "New York" }
# El resultado debería mostrar conexión a weather.service.example.com
# Para una base de datos:

tool_name = "Database Tool"
parameters = { "ID_user": "Amin Espinoza" }
# El resultado indicaría conexión a database.service.example.com
```

Estos resultados te permiten confirmar que MCP Server dirige correctamente tus solicitudes según sus configuraciones no importa si surge un error puntual por conexión, lo importante es verificar que la dirección aplicada sea la adecuada.

# Clase 19 Creación de servidor MCP con SERP API para búsqueda web

Resumen
Crear un sistema de búsqueda web eficiente puede ser sencillo con las herramientas adecuadas. En este contenido aprenderás cómo desarrollar un servidor MCP usando SERP API, un servicio para búsqueda web que permite integraciones rápidas y accesibles. Este recurso gratuito y fácil de configurar aporta versatilidad y potencia a tus proyectos tecnológicos.

¿Qué es SERP API y cómo configurar tu cuenta?
SERP API es una herramienta gratuita que permite realizar búsquedas web con facilidad, generando resultados efectivos de forma rápida y accesible. Registrarte es sencillo mediante cuenta de GitHub, Gmail o número de teléfono; el proceso de obtención del API key es inmediato:

Ingresa al sitio web de SERP API.
Selecciona método de registro y autentícate.
Copia la llave API proporcionada para empezar a usar el servicio.
¿Cómo configurar SERP API con tu proyecto?
Integra la API key en tu entorno de desarrollo a través de un archivo .env para garantizar seguridad y accesibilidad en tu configuración:

Crea un archivo .env y agrega tu llave SERP API entre comillas.
Usa un archivo env-sample como referencia para compartir configuraciones.
Esta práctica te permite mantener ordenado tu proyecto y salvaguardar tus datos sensibles.

¿Cómo construir un servidor web MCP con Fast MCP y SERP API?
El desarrollo del servidor incluye módulos básicos y avanzados que potenciarán tus aplicaciones:

Importación de módulos fundamentales como OS, json, HTTPX, Fast MCP Server, y manejo del ambiente.
Implementación de un método específico para peticiones (make SERP API request).
Integración de todos los parámetros necesarios para búsquedas generales: consulta, resultados esperados y contexto.
La importancia del registro (logging) radica en asegurar una transparencia operacional que identifique aciertos y fallos, brindando claridad en todo momento sobre el rendimiento del sistema.

Además, es recomendable considerar documentación multilingüe (español e inglés) para ampliar el alcance de tus aplicaciones y mejorar su accesibilidad global.

Al implementar estas recomendaciones simples y estructuradas, tu servidor MCP estará listo para realizar búsquedas web efectivas con una herramienta poderosa como SERP API.

¿Quieres compartir alguna experiencia implementando un MCP con SERP API o tienes dudas sobre el proceso? ¡Déjanos tu comentario abajo!
