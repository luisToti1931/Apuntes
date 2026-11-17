"""BIBLIOTECA DE MÉTODOS CON SELF · TEMÁTICA CANINA
====================================================================
Recopilación de TODOS los métodos válidos de los exámenes y proyectos
trabajados (BiciAlerta, CanAlerta, PatitasAdopta, Tienda canina y los
proyectos 02, 03 y 04 del repaso final) adaptados a perros, más métodos
EXTRA que pueden servir en otros ejercicios.

Etiquetas en cada docstring:
    [EXAMEN] -> el método (o su idea) apareció en un examen/ejercicio.
    [EXTRA]  -> añadido como ampliación.

REGLAS que cumple todo el archivo (las del enunciado):
    * Ningún método imprime ni pide datos: devuelven valores, booleanos,
      listas, diccionarios o códigos de estado ("OK", "DUPLICADO"...).
    * Primero se VALIDA y después se MODIFICA: una operación inválida
      nunca deja cambios parciales.
    * Solo biblioteca estándar. print()/input() únicamente en main().

ÍNDICE
    0. Helpers privados de validación
    1. PerroPerdido / RegistroPerdidos      (BiciAlerta y CanAlerta)
    2. Perro / Protectora                   (PatitasAdopta)
    3. Producto / LineaVenta / Venta / Tienda (Tienda canina, proyecto 01)
    4. CartaRaza / ColeccionRazas           (proyecto 02: cartas e intercambios)
    5. Participante / Taller / Inscripcion / EscuelaCanina (proyecto 03)
    6. ServicioCanino / Peluqueria / Teleconsulta / GestorServicios
                                            (proyecto 04: herencia)

Ejecuta `python metodos_con_self.py` para lanzar las comprobaciones.
"""
import math


# =====================================================================
# 0. HELPERS PRIVADOS DE VALIDACIÓN (lanzan ValueError si algo es inválido)
# =====================================================================
def _texto(valor, nombre):
    """Texto no vacío (sin espacios sobrantes)."""
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{nombre} no puede estar vacío")
    return valor.strip()


def _entero(valor, nombre, minimo=None, maximo=None):
    """Entero real: rechaza bool, 3.5, 'abc'. Acepta '4', 4 y 4.0."""
    if isinstance(valor, bool):
        raise ValueError(f"{nombre} debe ser un número entero")
    if isinstance(valor, float):
        if not valor.is_integer():
            raise ValueError(f"{nombre} debe ser un número entero")
        valor = int(valor)
    else:
        try:
            valor = int(valor)
        except (TypeError, ValueError):
            raise ValueError(f"{nombre} debe ser un número entero") from None
    if minimo is not None and valor < minimo:
        raise ValueError(f"{nombre} debe ser como mínimo {minimo}")
    if maximo is not None and valor > maximo:
        raise ValueError(f"{nombre} debe ser como máximo {maximo}")
    return valor


def _decimal(valor, nombre, minimo=None, estricto=False):
    """Número finito. Acepta coma decimal ('3,5'). Rechaza nan e inf.

    minimo + estricto=True  -> valor > minimo
    minimo + estricto=False -> valor >= minimo
    """
    if isinstance(valor, bool):
        raise ValueError(f"{nombre} debe ser numérico")
    if isinstance(valor, str):
        valor = valor.strip().replace(",", ".")
    try:
        numero = float(valor)
    except (TypeError, ValueError):
        raise ValueError(f"{nombre} debe ser numérico") from None
    if not math.isfinite(numero):
        raise ValueError(f"{nombre} debe ser un número finito")
    if minimo is not None:
        if estricto and numero <= minimo:
            raise ValueError(f"{nombre} debe ser mayor que {minimo:g}")
        if not estricto and numero < minimo:
            raise ValueError(f"{nombre} debe ser como mínimo {minimo:g}")
    return numero


def _estado(valor, permitidos, nombre="El estado"):
    """Estado normalizado en mayúsculas que debe estar en `permitidos`."""
    if not isinstance(valor, str) or valor.strip().upper() not in permitidos:
        raise ValueError(f"{nombre} no es válido")
    return valor.strip().upper()


def _clave(valor):
    """Normaliza un código para usarlo como clave de diccionario."""
    return str(valor).strip().upper()


def _email(valor):
    """Email sencillo normalizado en minúsculas."""
    if not isinstance(valor, str):
        raise ValueError("El email no es válido")
    valor = valor.strip().lower()
    usuario, arroba, dominio = valor.partition("@")
    if (not usuario or arroba != "@" or "@" in dominio or " " in valor
            or "." not in dominio.strip(".")):
        raise ValueError("El email no es válido")
    return valor


# =====================================================================
# 1. PERRO PERDIDO / REGISTRO  (BiciAlerta -> CanAlerta)
# =====================================================================
class PerroPerdido:
    """Aviso de un perro perdido. Estados: PERDIDO / ENCONTRADO."""

    ESTADOS = ("PERDIDO", "ENCONTRADO")

    def __init__(self, codigo, propietario, raza, recompensa, estado="PERDIDO"):
        self.codigo = _texto(codigo, "El código").upper()
        self.propietario = _texto(propietario, "El propietario")
        self.raza = _texto(raza, "La raza")
        self.recompensa = _decimal(recompensa, "La recompensa", minimo=0, estricto=True)
        self.estado = _estado(estado, self.ESTADOS)

    def esta_perdido(self):
        """[EXTRA] True si sigue perdido."""
        return self.estado == "PERDIDO"

    def marcar_encontrado(self):
        """[EXAMEN] PERDIDO -> ENCONTRADO. False si ya estaba encontrado."""
        if self.estado != "PERDIDO":
            return False
        self.estado = "ENCONTRADO"
        return True

    def cambiar_recompensa(self, nueva):
        """[EXTRA] Cambia la recompensa solo si sigue perdido y el valor es válido."""
        if not self.esta_perdido():
            return False
        try:
            self.recompensa = _decimal(nueva, "La recompensa", minimo=0, estricto=True)
        except ValueError:
            return False
        return True

    def a_fila(self):
        """[EXTRA] Diccionario listo para csv.DictWriter."""
        return {"codigo": self.codigo, "propietario": self.propietario,
                "raza": self.raza, "recompensa": self.recompensa, "estado": self.estado}

    def __str__(self):
        return (f"{self.codigo} | {self.propietario} | {self.raza} | "
                f"{self.recompensa:.2f} € | {self.estado}")


class RegistroPerdidos:
    """Diccionario codigo -> PerroPerdido."""

    def __init__(self):
        self.perros = {}

    def registrar(self, perro):
        """[EXAMEN] True si se incorpora; False si el código ya existía."""
        if perro.codigo in self.perros:
            return False
        self.perros[perro.codigo] = perro
        return True

    def listar(self):
        """[EXAMEN] Copia de la lista de perros (no expone el diccionario)."""
        return list(self.perros.values())

    def obtener(self, codigo):
        """[EXTRA] El perro con ese código, o None."""
        return self.perros.get(_clave(codigo))

    def encontrar(self, codigo):
        """[EXAMEN] Marca como ENCONTRADO. False si no existe o ya lo estaba."""
        perro = self.obtener(codigo)
        if perro is None:
            return False
        return perro.marcar_encontrado()

    def eliminar(self, codigo):
        """[EXAMEN] True si existía y se ha eliminado."""
        return self.perros.pop(_clave(codigo), None) is not None

    def buscar(self, texto):
        """[EXAMEN] Fragmento en propietario o raza, sin distinguir mayúsculas."""
        texto = str(texto).strip().casefold()
        if not texto:
            return []
        return [p for p in self.perros.values()
                if texto in p.propietario.casefold() or texto in p.raza.casefold()]

    def filtrar_por_estado(self, estado):
        """[EXTRA] Perros con el estado indicado (PERDIDO / ENCONTRADO)."""
        estado = str(estado).strip().upper()
        return [p for p in self.perros.values() if p.estado == estado]

    def resumen(self):
        """[EXAMEN] Totales y recompensa pendiente (suma de los todavía perdidos)."""
        perdidos = 0
        encontrados = 0
        pendiente = 0.0
        for perro in self.perros.values():
            if perro.estado == "PERDIDO":
                perdidos += 1
                pendiente += perro.recompensa
            elif perro.estado == "ENCONTRADO":
                encontrados += 1
        return {"total": len(self.perros), "perdidos": perdidos,
                "encontrados": encontrados, "recompensa_pendiente": pendiente}

    def top_recompensas(self, n=3):
        """[EXTRA] Los n perros perdidos con mayor recompensa."""
        if n <= 0:
            return []
        perdidos = self.filtrar_por_estado("PERDIDO")
        return sorted(perdidos, key=lambda p: (-p.recompensa, p.codigo))[:n]

    def recompensa_media_pendiente(self):
        """[EXTRA] Media de recompensa de los perdidos (0.0 si no hay ninguno)."""
        perdidos = self.filtrar_por_estado("PERDIDO")
        if not perdidos:
            return 0.0
        return sum(p.recompensa for p in perdidos) / len(perdidos)


# =====================================================================
# 2. PERRO / PROTECTORA  (PatitasAdopta)
# =====================================================================
class Perro:
    """Perro de una protectora. Estados: DISPONIBLE / ADOPTADO."""

    ESTADOS = ("DISPONIBLE", "ADOPTADO")

    def __init__(self, codigo, nombre, raza, edad, peso, estado="DISPONIBLE"):
        self.codigo = _texto(codigo, "El código").upper()
        self.nombre = _texto(nombre, "El nombre")
        self.raza = _texto(raza, "La raza")
        self.edad = _entero(edad, "La edad", minimo=0, maximo=30)
        self.peso = _decimal(peso, "El peso", minimo=0, estricto=True)
        self.estado = _estado(estado, self.ESTADOS)

    def esta_disponible(self):
        """[EXTRA]"""
        return self.estado == "DISPONIBLE"

    def adoptar(self):
        """[EXAMEN] DISPONIBLE -> ADOPTADO. False si no estaba disponible."""
        if self.estado != "DISPONIBLE":
            return False
        self.estado = "ADOPTADO"
        return True

    def devolver(self):
        """[EXTRA] ADOPTADO -> DISPONIBLE (devolución a la protectora)."""
        if self.estado != "ADOPTADO":
            return False
        self.estado = "DISPONIBLE"
        return True

    def etapa_vida(self):
        """[EXTRA] CACHORRO (<1 año), ADULTO (<8) o SENIOR."""
        if self.edad < 1:
            return "CACHORRO"
        if self.edad < 8:
            return "ADULTO"
        return "SENIOR"

    def categoria_peso(self):
        """[EXTRA] PEQUEÑO (<10 kg), MEDIANO (<25), GRANDE (<45) o GIGANTE."""
        if self.peso < 10:
            return "PEQUEÑO"
        if self.peso < 25:
            return "MEDIANO"
        if self.peso < 45:
            return "GRANDE"
        return "GIGANTE"

    def a_fila(self):
        """[EXTRA] Diccionario listo para csv.DictWriter."""
        return {"codigo": self.codigo, "nombre": self.nombre, "raza": self.raza,
                "edad": self.edad, "peso": self.peso, "estado": self.estado}

    def __str__(self):
        return (f"{self.codigo} | {self.nombre} | {self.raza} | "
                f"{self.edad} años | {self.peso:.1f} kg | {self.estado}")


class Protectora:
    """Diccionario codigo -> Perro."""

    def __init__(self):
        self.perros = {}

    def registrar(self, perro):
        """[EXAMEN] True si ingresa; False si el código ya existía."""
        if perro.codigo in self.perros:
            return False
        self.perros[perro.codigo] = perro
        return True

    def listar(self):
        """[EXAMEN]"""
        return list(self.perros.values())

    def obtener(self, codigo):
        """[EXTRA]"""
        return self.perros.get(_clave(codigo))

    def adoptar(self, codigo):
        """[EXAMEN] DISPONIBLE -> ADOPTADO. False si no existe o ya adoptado."""
        perro = self.obtener(codigo)
        if perro is None:
            return False
        return perro.adoptar()

    def devolver(self, codigo):
        """[EXTRA] ADOPTADO -> DISPONIBLE."""
        perro = self.obtener(codigo)
        if perro is None:
            return False
        return perro.devolver()

    def dar_de_baja(self, codigo):
        """[EXAMEN] True si existía y se ha eliminado (dict.pop con valor por defecto)."""
        return self.perros.pop(_clave(codigo), None) is not None

    def disponibles_por_edad(self):
        """[EXAMEN] DISPONIBLES de menor a mayor edad (a igual edad, por nombre)."""
        disponibles = [p for p in self.perros.values() if p.estado == "DISPONIBLE"]
        return sorted(disponibles, key=lambda p: (p.edad, p.nombre.casefold()))

    def buscar(self, texto):
        """[EXTRA] Fragmento en nombre o raza, sin distinguir mayúsculas."""
        texto = str(texto).strip().casefold()
        if not texto:
            return []
        return [p for p in self.perros.values()
                if texto in p.nombre.casefold() or texto in p.raza.casefold()]

    def filtrar_por_raza(self, raza):
        """[EXTRA] Perros de esa raza exacta (sin distinguir mayúsculas)."""
        raza = str(raza).strip().casefold()
        return [p for p in self.perros.values() if p.raza.casefold() == raza]

    def filtrar_por_peso(self, minimo, maximo):
        """[EXTRA] Perros con minimo <= peso <= maximo."""
        return [p for p in self.perros.values() if minimo <= p.peso <= maximo]

    def agrupar_por_raza(self):
        """[EXTRA] Diccionario raza (en minúsculas) -> lista de perros."""
        grupos = {}
        for perro in self.perros.values():
            grupos.setdefault(perro.raza.casefold(), []).append(perro)
        return grupos

    def contar_por_raza(self):
        """[EXTRA] Diccionario raza (en minúsculas) -> cantidad."""
        return {raza: len(lista) for raza, lista in self.agrupar_por_raza().items()}

    def edad_media(self):
        """[EXTRA] Edad media de todos los perros (0.0 si no hay ninguno)."""
        if not self.perros:
            return 0.0
        return sum(p.edad for p in self.perros.values()) / len(self.perros)

    def estadisticas(self):
        """[EXAMEN] Cantidades, peso medio de los disponibles y perro más pesado."""
        disponibles = 0
        adoptados = 0
        suma_peso = 0.0
        mas_pesado = None
        for perro in self.perros.values():
            if perro.estado == "DISPONIBLE":
                disponibles += 1
                suma_peso += perro.peso
            elif perro.estado == "ADOPTADO":
                adoptados += 1
            if mas_pesado is None or perro.peso > mas_pesado.peso:
                mas_pesado = perro
        peso_medio = suma_peso / disponibles if disponibles else 0.0  # evita /0
        return {"total": len(self.perros), "disponibles": disponibles,
                "adoptados": adoptados, "peso_medio_disponibles": peso_medio,
                "mas_pesado": mas_pesado}


# =====================================================================
# 3. TIENDA CANINA  (proyecto 01: inventario y ventas)
# =====================================================================
class Producto:
    """Producto de la tienda canina."""

    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = _texto(codigo, "El código").upper()
        self.nombre = _texto(nombre, "El nombre")
        self.categoria = _texto(categoria, "La categoría")
        self.precio = _decimal(precio, "El precio", minimo=0, estricto=True)
        self.stock = _entero(stock, "El stock", minimo=0)

    def reponer(self, cantidad):
        """[EXAMEN] Suma unidades. False (sin cambios) si la cantidad no es válida."""
        try:
            cantidad = _entero(cantidad, "La cantidad", minimo=1)
        except ValueError:
            return False
        self.stock += cantidad
        return True

    def descontar(self, cantidad):
        """[EXAMEN] Resta unidades. False (sin cambios) si no es válida o no hay stock."""
        try:
            cantidad = _entero(cantidad, "La cantidad", minimo=1)
        except ValueError:
            return False
        if cantidad > self.stock:
            return False
        self.stock -= cantidad
        return True

    def esta_agotado(self):
        """[EXTRA]"""
        return self.stock == 0

    def valor_en_stock(self):
        """[EXTRA] precio x unidades en almacén."""
        return round(self.precio * self.stock, 2)

    def a_fila(self):
        """[EXTRA]"""
        return {"codigo": self.codigo, "nombre": self.nombre, "categoria": self.categoria,
                "precio": self.precio, "stock": self.stock}


class LineaVenta:
    """Línea de una venta; conserva el precio en el momento de la operación."""

    def __init__(self, producto, cantidad, precio_unitario):
        if not isinstance(producto, Producto):
            raise ValueError("La línea necesita un producto válido")
        self.producto = producto
        self.cantidad = _entero(cantidad, "La cantidad", minimo=1)
        self.precio_unitario = _decimal(precio_unitario, "El precio unitario",
                                        minimo=0, estricto=True)

    def importe(self):
        """[EXAMEN] cantidad x precio_unitario."""
        return round(self.cantidad * self.precio_unitario, 2)


class Venta:
    """Venta con varias líneas. El descuento se aplica al TOTAL, nunca por línea."""

    UMBRAL_DESCUENTO = 50.0
    PORCENTAJE_DESCUENTO = 0.10

    def __init__(self, numero, cliente):
        self.numero = _entero(numero, "El número de venta", minimo=1)
        self.cliente = _texto(cliente, "El cliente")
        self.lineas = []

    def agregar_linea(self, producto, cantidad, precio_unitario=None):
        """[EXAMEN] Añade una línea; si ya hay una del mismo producto y precio, suma."""
        if not isinstance(producto, Producto):
            raise ValueError("La línea necesita un producto válido")
        if precio_unitario is None:
            precio_unitario = producto.precio
        nueva = LineaVenta(producto, cantidad, precio_unitario)
        for linea in self.lineas:
            if (linea.producto.codigo == nueva.producto.codigo
                    and linea.precio_unitario == nueva.precio_unitario):
                linea.cantidad += nueva.cantidad
                return linea
        self.lineas.append(nueva)
        return nueva

    def quitar_linea(self, codigo):
        """[EXTRA] Elimina la línea de ese producto y la devuelve (None si no hay)."""
        codigo = _clave(codigo)
        for posicion, linea in enumerate(self.lineas):
            if linea.producto.codigo == codigo:
                return self.lineas.pop(posicion)
        return None

    def unidades(self):
        """[EXTRA] Total de unidades de la venta."""
        return sum(linea.cantidad for linea in self.lineas)

    def subtotal(self):
        """[EXAMEN] Suma de los importes de las líneas."""
        return round(sum(linea.importe() for linea in self.lineas), 2)

    def descuento(self):
        """[EXAMEN] 10 % del subtotal si es >= 50 €; 0 en caso contrario."""
        subtotal = self.subtotal()
        if subtotal >= self.UMBRAL_DESCUENTO:
            return round(subtotal * self.PORCENTAJE_DESCUENTO, 2)
        return 0.0

    def total(self):
        """[EXAMEN] subtotal - descuento."""
        return round(self.subtotal() - self.descuento(), 2)


class Tienda:
    """Gestor: catálogo, venta en curso e historial de ventas cerradas."""

    def __init__(self):
        self.productos = {}
        self.ventas_cerradas = []
        self.venta_actual = []