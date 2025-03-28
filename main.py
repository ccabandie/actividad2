clients = [
    " Ana López ", "Pedro Gómez", "maria martínez", "Pedro Gómez ", "",
    " Luis Rodríguez ", None, "ana lópez", "JUAN PÉREZ", "MARTA SUÁREZ",
    "luis rodríguez", "maría martínez ", " claudia torres", "CLAUDIA TORRES",
    " ", "pedro gómez", "Juan Pérez", None, "Ricardo Fernández", "LAURA RAMOS",
    "carlos mendes", "RICARDO FERNÁNDEZ ", " Laura ramos", "CARLOS MENDES",
    "alejandro gonzález", " ALEJANDRO GONZÁLEZ ", "Patricia Vega",
    "patricia VEGA", "Andrés Ocampo", " andrés ocampo", "Monica Herrera",
    "MONICA HERRERA ", "gabriela ruíz", "Gabriela Ruíz", "sandra morales",
    "SANDRA MORALES", "miguel ángel", "Miguel Ángel ", " Damián Castillo",
    "Damián Castillo ", None, "", " "
]
def clean_clients(clients):
    """Eliminar espacios en blanco, convertir a título, eliminar duplicados y valores nulos."""
    # Eliminar espacios extra y convertir a título
    cleaned_clients = [client.strip().title() for client in clients if client]
    
    # Eliminar duplicados
    cleaned_clients = list(set(cleaned_clients))
    
    return cleaned_clients