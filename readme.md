## Daniel Alberto Garzon Fraile

# Patrones de Diseño 
---

## Estructura del proyecto

```
├── 01_singleton.py
├── 02_factory.py
├── 03_factory_decorator.py
└── 04_factory_decorator_observer.py
```

---

## 1 — Patrón Singleton
**Categoría:** Creacional

### ¿Qué hace?
Garantiza que una clase tenga **una sola instancia** durante toda la ejecución del programa. Cada vez que intentas crear un nuevo objeto, obtienes el mismo de siempre.

### Contexto del videojuego
Una clase `Counter` lleva la cuenta de un valor global. Sin importar cuántas veces se instancie, todas las variables apuntan al mismo objeto, por lo que el contador siempre es compartido y consistente.

### Concepto clave
```python
def __new__(cls):
    if cls._instance is None:
        cls._instance = super().__new__(cls)
    return cls._instance
```
`__new__` se llama antes que `__init__` en cada instanciación. Al interceptarlo, controlamos si se crea un objeto nuevo o se devuelve el existente.

### ¿Cuándo usarlo?
- Configuración global del juego
- Un logger o bus de eventos compartido
- Un gestor de base de datos o de archivos de guardado

---

## 02 — Patrón Factory
**Categoría:** Creacional

### ¿Qué hace?
Delega la responsabilidad de crear objetos a una **función fábrica**, en lugar de llamar constructores directamente en todo el código.

### Contexto del videojuego
Una función `create_character()` recibe un string como `"mage"` y devuelve el objeto de personaje correcto (`Warrior`, `Mage` o `Archer`), cada uno con su propio comportamiento de `attack()`.

### Concepto clave
```python
def create_character(character_type):
    characters = {"warrior": Warrior, "mage": Mage, "archer": Archer}
    return characters[character_type]()
```
El que llama a la función nunca necesita saber qué clase se está instanciando — solo pide un tipo y recibe un objeto.

### ¿Cuándo usarlo?
- Spawnear personajes o enemigos según datos o archivos de configuración
- Dejar que el jugador elija una clase al inicio del juego
- Crear objetos o armas desde una tabla de botín

---

## 03 — Patrones Factory + Decorator
**Categorías:** Creacional + Estructural

### ¿Qué hace?
Combina el Factory para **crear enemigos** y el Decorator para **añadirles mejoras** en tiempo de ejecución, sin modificar las clases originales.

### Contexto del videojuego
Los enemigos (`Goblin`, `Orc`, `Dragon`) se crean con `spawn_enemy()`. Luego, decoradores como `Shielded`, `Enraged` y `Poisoned` envuelven los objetos enemigo para agregar comportamientos extra en capas.

### Concepto clave
```python
dragon = Poisoned(Enraged(spawn_enemy("dragon")))
dragon.describe()
```
Cada decorador envuelve al anterior, llama primero al método del objeto interno y luego añade su propio comportamiento. Se pueden combinar libremente.

### ¿Cuándo usarlo?
- Agregar efectos de estado a enemigos o jugadores (fuego, hielo, aturdimiento)
- Aplicar modificadores de objetos sin crear una subclase por cada combinación
- Extender comportamientos dinámicamente según eventos del juego

---

## 04 — Patrones Factory + Decorator + Observer
**Categorías:** Creacional + Estructural + Comportamiento

### ¿Qué hace?
Extiende el ejemplo anterior añadiendo el patrón Observer, que permite que los sistemas del juego **reaccionen automáticamente** cuando un enemigo muere, sin que el enemigo sepa nada sobre esos sistemas.

### Contexto del videojuego
Cuando los HP de un enemigo llegan a 0, notifica a todos los observadores registrados. Cada sistema responde de forma independiente:
- `ScoreSystem` otorga puntos
- `QuestSystem` registra la baja
- `LootSystem` suelta oro

### Concepto clave
```python
# Registrar observadores
goblin.add_observer(score)
goblin.add_observer(quests)

# Dentro de Enemy.take_damage()
if self.hp <= 0:
    for obs in self._observers:
        obs.on_enemy_died(self)
```
El enemigo simplemente recorre su lista de observadores y llama a `on_enemy_died()`. No le importa qué hace cada sistema — están completamente desacoplados.

### ¿Cuándo usarlo?
- Actualizar la interfaz cuando cambia el estado del juego (barra de vida, marcador)
- Notificar a múltiples sistemas con un solo evento (muerte, subida de nivel, recolección de objeto)
- Mantener los sistemas del juego independientes y fáciles de agregar o eliminar

---

##  Resumen de patrones

| Archivo | Patrón(es) | Categoría |
|---------|-----------|-----------|
| `01_singleton.py` | Singleton | Creacional |
| `02_factory.py` | Factory | Creacional |
| `03_factory_decorator.py` | Factory + Decorator | Creacional + Estructural |
| `04_factory_decorator_observer.py` | Factory + Decorator + Observer | Creacional + Estructural + Comportamiento |

---

##  Cómo ejecutarlo

Cada archivo es independiente. Simplemente ejecuta cualquiera con Python 3:

```bash
python 01_singleton.py
python 02_factory.py
python 03_factory_decorator.py
python 04_factory_decorator_observer.py
```

No se requieren dependencias externas.
