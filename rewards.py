from .state import save_player
def end_session_rewards(player):
    xp_gain = player.cards_correct
    player.add_xp(xp_gain)
    if player.mission_completed and  player.cards_wrong == 0 :
        player.gain_discipline(4)
        player.add_xp(10)
        player.mission_réussie+=1
    elif player.mission_completed:
        player.gain_discipline(2)
        player.mission_réussie+=1
        
    else:
        player.lose_discipline(1)
    
    player.pourcentage_de_réussite=player.mission_réussie//player.total_mission
    save_player(player)