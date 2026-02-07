# Clase 1

repositorio del curso: https://github.com/platzi/curso-mcp

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


# Clase 17 Enrutamiento de herramientas con MCP Server

