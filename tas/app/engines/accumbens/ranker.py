class AccumbensRanker:
    """
    Juiz Final: Decide a ordem baseada em probabilidade de engajamento.
    Pesos: Share > Comment > Like > Click
    """
    def __init__(self):
        self.weights = {
            "share": 10.0,
            "comment": 5.0,
            "like": 2.0,
            "click": 1.0
        }

    async def rank(self, candidates, elo_map=None):
        if elo_map is None:
            elo_map = {}
        for c in candidates:
            # Cálculo de score baseado em comportamento (simulado por enquanto)
            engagement_score = (
                c.get("predicted_shares", 0) * self.weights["share"] +
                c.get("predicted_likes", 0) * self.weights["like"]
            )
            
            author_id = str(c.get("author_id", ""))
            author_elo = elo_map.get(author_id, 1400)
            # Bônus proporcional ao prestígio Elo do autor (ex: 1500 Elo dá +5 pontos de score)
            elo_bonus = (author_elo - 1400) * 0.05
            
            # Soma a afinidade da SARA (0 a 1) multiplicada por um fator de peso + ELO
            c["final_score"] = (c.get("sara_score", 0.5) * 50) + engagement_score + elo_bonus
            
        return [str(c["id"]) for c in sorted(candidates, key=lambda x: x["final_score"], reverse=True)]

accumbens_ranker = AccumbensRanker()