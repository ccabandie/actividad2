# Definición de funciones
def start_count(players):
    """Inicializa el diccionario de estadisticas y puntajes."""
    stats = {}
    for player in players:
        stats[player] = {
            'kills': 0,
            'assists': 0,
            'deaths': 0,
            'mvp_count': 0,
            'total_points': 0
            }
    return stats

def calculate_points_round(data_player):
    """calcula el puntaje de cada jugador en la ronda"""
    kills = data_player['kills']
    assists = data_player['assists']
    deaths = -1 if data_player['deaths'] else 0
    
    return kills * 3 + assists * 1 + deaths

def sum_points (stats, player, kills, assists, deaths, points):
    """Recibe el diccionario de estadisticas, el jugador, kills, assists, deaths y puntos y lo actualiza."""
    stats[player]['kills'] += kills
    stats[player]['assists'] += assists
    stats[player]['deaths'] += (1 if deaths else 0)
    stats[player]['total_points'] += points

def define_mvp(round_scores):                          
    """Determina el MVP de la ronda"""
    return max(round_scores.items(), key=lambda x: x[1]) 

def  show_ranking(stats):
    """Ordena a los jugadores por puntos totales y muestra una tabla."""
    print("\n--- Ranking ---")
    print("Jugador   | Kills | Asistencias | Muertes | MVPs | Puntos")
    print("-" * 50)
    sorted_players = sorted(stats.items(), key=lambda x: x[1]['total_points'], reverse=True)
    for player, data in sorted_players:
        print(f"{player.ljust(8)} | {str(data['kills']).ljust(5)} | {str(data['assists']).ljust(11)} | {str(data['deaths']).ljust(7)} | {str(data['mvp_count']).ljust(4)} | {data['total_points']}")

# Función principal
def simulate_games(rounds):
    players = list(rounds[0].keys())                   
    stats = start_count (players)                          
    for i, round in enumerate(rounds, 1):              
        print(f"\n--- Ronda {i} ---")
        round_scores = {}                               
        
        for player in players:                         
            data = round[player]                       
            points = calculate_points_round(data)      
            round_scores[player] = points              
            sum_points (stats, player, data['kills'], data['assists'], data['deaths'], points)  
            
        mvp, points_mvp = define_mvp(round_scores)    
        stats[mvp]['mvp_count'] += 1                   
        print(f" MVP de la Ronda: {mvp} (Puntos: {points_mvp})")             
        
        show_ranking(stats)      
    
    return stats