import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app.engines.intent import extract_intent
from app.engines.genome_matcher import match_genomes
from app.engines.multi_agent_review import run_multi_agent_review

def test_intent_extraction():
    prompt = "I want Canva + GitHub + Notion"
    intent = extract_intent(prompt)
    assert "domain" in intent
    assert "title" in intent

def test_genome_matching():
    prompt = "I want Discord for hospitals"
    intent = extract_intent(prompt)
    genomes = match_genomes(prompt, intent)
    assert "matches" in genomes
    assert len(genomes["matches"]) > 0

def test_multi_agent_review():
    prompt = "I want self-hosted Datadog alternative"
    intent = {"domain": "Monitoring Platform", "title": "ZeroCost Architect", "scale": "High"}
    arch = {"services": []}
    db = {"tables": []}
    apis = {"endpoints": []}
    deployment = {"docker": {}}
    costs = {"hosting_tiers": []}
    
    review = run_multi_agent_review(prompt, intent, arch, db, apis, deployment, costs)
    assert review["overall_score"] >= 80
    assert len(review["personae"]) == 4
