from typing import List, Dict

class Player:
    def __init__(self, name: str, team: str, role: str):
        self.name = name
        self.team = team
        self.role = role

    def __repr__(self):
        return f"{self.name} ({self.role}) - {self.team}"

class Game:
    def __init__(self, date: str, game_name: str, teams: List[str]):
        self.date = date
        self.game_name = game_name
        self.teams = teams

    def __repr__(self):
        return f"{self.date} - {self.game_name} | {', '.join(self.teams)}"

class Modality:
    def __init__(self, name: str, players: List[Player], games: List[Game]):
        self.name = name
        self.players = players
        self.games = games

    def __repr__(self):
        return f"Modalidade: {self.name}, Jogadores: {len(self.players)}, Jogos: {len(self.games)}"

class FuriaBotData:
    def __init__(self):
        self.modalities: Dict[str, Modality] = {}

    def add_modality(self, modality: Modality):
        self.modalities[modality.name] = modality

    def get_modality(self, name: str) -> Modality:
        return self.modalities.get(name)

    def get_all_modalities(self) -> List[Modality]:
        return list(self.modalities.values())

# Exemplo de como usar
if __name__ == "__main__":
    # Jogadores de CS2
    cs2_players = [
        Player(name="KSCERATO", team="FURIA", role="AWPer"),
        Player(name="yuurih", team="FURIA", role="Rifler"),
        Player(name="FalleN", team="FURIA", role="AWPer"),
    ]

    # Jogos de CS2
    cs2_games = [
        Game(date="2025-05-01", game_name="FURIA vs Team A", teams=["FURIA", "Team A"]),
        Game(date="2025-05-05", game_name="FURIA vs Team B", teams=["FURIA", "Team B"]),
    ]

    # Criando a modalidade de CS2
    cs2_modality = Modality(name="CS2", players=cs2_players, games=cs2_games)

    # Criando o objeto FuriaBotData para armazenar as modalidades
    furia_bot_data = FuriaBotData()
    furia_bot_data.add_modality(cs2_modality)

    # Exibindo os dados da modalidade CS2
    print(furia_bot_data.get_modality("CS2"))
