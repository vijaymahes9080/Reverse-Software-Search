from typing import Dict, Any, List

def compare_blueprints(bp1: Dict[str, Any], bp2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Compare two synthesized product blueprints side-by-side.
    """
    title1 = bp1.get("title", "Blueprint A")
    title2 = bp2.get("title", "Blueprint B")
    
    score1 = bp1.get("multi_agent", {}).get("overall_score", 90)
    score2 = bp2.get("multi_agent", {}).get("overall_score", 90)
    
    genomes1 = set(bp1.get("genomes", {}).get("matches", []))
    genomes2 = set(bp2.get("genomes", {}).get("matches", []))
    
    shared_genomes = list(genomes1.intersection(genomes2))
    unique_genomes1 = list(genomes1 - genomes2)
    unique_genomes2 = list(genomes2 - genomes1)
    
    return {
        "title_a": title1,
        "title_b": title2,
        "score_diff": score1 - score2,
        "shared_genomes": shared_genomes,
        "unique_to_a": unique_genomes1,
        "unique_to_b": unique_genomes2,
        "verdict": f"{title1} has a higher health score by {abs(score1 - score2)} points." if score1 != score2 else "Both blueprints have identical health ratings."
    }
