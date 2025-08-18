import spacy
from spacy.matcher import PhraseMatcher
from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor

nlp=spacy.load("en_core_web_md")
skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)
def extract_skills(text):
    if not text:
        return []
    annotations = skill_extractor.annotate(text)

    skills_found = []

    for category in ["full_matches", "ngram_scored", "abbreviations"]:
        for match in annotations["results"].get(category, []):
            if "skill_name" in match:
                skills_found.append(match["skill_name"].lower())
            elif category == "ngram_scored" and "doc_node_value" in match:
                skills_found.append(match["doc_node_value"].lower())

    return list(set(skills_found))