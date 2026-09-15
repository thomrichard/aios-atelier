#!/usr/bin/env python3
"""Install the generic AIOS. Python standard library only; no network operations."""
import argparse
import datetime as dt
import json
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import unquote


def write(root, relative, text):
    p = root / relative
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + '\n', encoding='utf-8')


def validate_profile(p):
    if not isinstance(p, dict):
        raise ValueError('Le profil doit être un objet JSON.')
    for key in ('name', 'context'):
        if not isinstance(p.get(key), str) or not p[key].strip():
            raise ValueError(f'Champ texte requis : {key}')
    for key in ('language', 'preferences'):
        if key in p and not isinstance(p[key], str):
            raise ValueError(f'Champ texte attendu : {key}')
    for key in ('roles', 'projects', 'tools', 'open_questions'):
        if not isinstance(p.get(key, []), list):
            raise ValueError(f'Liste attendue : {key}')
    if any(not isinstance(x, str) for x in p.get('open_questions', [])):
        raise ValueError('Les points ouverts doivent être du texte.')
    for key in ('roles', 'projects'):
        seen = set()
        for obj in p.get(key, []):
            if not isinstance(obj, dict):
                raise ValueError(f'Objet attendu dans {key}')
            slug = obj.get('slug', '')
            if not isinstance(slug, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug) or slug in seen:
                raise ValueError(f'Slug invalide ou dupliqué dans {key}')
            seen.add(slug)
            for field in ('title', 'description'):
                if not isinstance(obj.get(field), str) or not obj[field].strip():
                    raise ValueError(f'{key} : {field} requis')
            if key == 'projects':
                if obj.get('status') not in ('envisage', 'actif', 'en-attente', 'termine', 'abandonne'):
                    raise ValueError('Statut de projet requis et explicite.')
                if not isinstance(obj.get('done_when', 'non précisée'), str):
                    raise ValueError('Condition de fin : texte attendu.')
    for obj in p.get('tools', []):
        if not isinstance(obj, dict) or any(not isinstance(obj.get(k), str) for k in ('name', 'usage')):
            raise ValueError('Outil : name et usage requis.')


def inline(s):
    return str(s).replace('\n', ' ').replace('|', '\\|').replace('[', '\\[').replace(']', '\\]')


def check_links(root):
    errors = []
    count = 0
    for path in root.rglob('*.md'):
        if '.ai/inputs' in path.as_posix():
            continue  # supplied source can reference documents not installed
        for target in re.findall(r'\]\((<[^>]+>|[^)]+)\)', path.read_text(encoding='utf-8')):
            target = target.strip('<>')
            if re.match(r'^[a-z]+:', target) or target.startswith('#'):
                continue
            local = unquote(target.split('#')[0])
            count += 1
            if not (path.parent / local).exists():
                errors.append(f'{path.relative_to(root)} -> {local}')
    if errors:
        raise ValueError('Liens invalides : ' + '; '.join(errors))
    return count


def render(root, profile, source):
    assets = Path(__file__).resolve().parents[1] / 'assets' / 'vault'
    shutil.copytree(assets, root, dirs_exist_ok=True)
    today = dt.date.today().isoformat()
    sections = [('0 - Inbox', 'inbox', 'Captures à traiter'), ('1 - Projets', 'projets', 'Projets'),
                ('2 - Casquettes', 'casquettes', 'Casquettes'), ('3 - Ressources', 'ressources', 'Ressources'),
                ('4 - Archives', 'archives', 'Archives')]
    for folder, index, title in sections:
        write(root, f'{folder}/{index}.md', f'# {title}\n')
    write(root, '3 - Ressources/ressources.md', '# Ressources\n\n[Contexte personnel](Personnel/contexte.md)\n\nDocuments et références ajoutés selon les besoins de l’activité.')
    source_path = root / '.ai/inputs/grill-me.md'
    source_path.parent.mkdir(parents=True, exist_ok=True)
    source_path.write_text(source, encoding='utf-8')
    # Use the profile as text, never as code or paths; private content is not in public indexes.
    write(root, '3 - Ressources/Personnel/contexte.md',
          '# Contexte personnel et activité\n\n' + profile['context'] +
          '\n\n## Préférences de travail\n\n' + profile.get('preferences', 'Non précisées.') +
          '\n\n## Points ouverts\n\n' + ('\n'.join('- ' + x for x in profile.get('open_questions', [])) or 'Aucun point renseigné.') +
          '\n\nProvenance : [Grill-me fourni](../../.ai/inputs/grill-me.md). Reformulation issue du profil préparé par l’assistant ; la source conserve les nuances et attributions.')
    write(root, '.ai/configuration.md', '# Configuration\n\nPersonne : ' + profile['name'] +
          '\n\nLangue : ' + profile.get('language', 'français') +
          '\n\n[Contexte et préférences](../3%20-%20Ressources/Personnel/contexte.md).\n\n' +
          'La demande actuelle fait référence pour les engagements. Les accès externes, sauvegardes et routines restent à configurer selon les besoins. Aucun rythme imposé.')
    tool_lines = ['# Outils et connexions', '', '| Outil | Usage déclaré | Vérification |', '|---|---|---|']
    for obj in profile.get('tools', []):
        tool_lines.append(f'| {inline(obj["name"])} | {inline(obj["usage"])} | Non vérifiée |')
    tool_lines.extend(['', 'Avant utilisation : identifier compte, source des données, opérations autorisées et date du test. Ne jamais écrire un secret dans cette fiche.'])
    write(root, '.ai/connexions.md', '\n'.join(tool_lines))
    for key, folder, kind, index in [('roles', '2 - Casquettes', 'casquette', 'casquettes'), ('projects', '1 - Projets', 'projet', 'projets')]:
        lines = [f'# {index.capitalize()}', '']
        for obj in profile.get(key, []):
            slug = obj['slug']
            status = obj.get('status', 'active')
            body = f'---\nid: {kind}-{slug}\ntype: {kind}\ntitle: {json.dumps(obj["title"], ensure_ascii=False)}\ncreated: {today}\nupdated: {today}\nstatus: {status}\n---\n\n# {obj["title"]}\n\n{obj["description"]}\n'
            if key == 'projects':
                body += '\n## Condition de fin\n\n' + obj.get('done_when', 'Non précisée.') + '\n'
            body += '\nProvenance : [contexte fourni](../../3%20-%20Ressources/Personnel/contexte.md).\n'
            write(root, f'{folder}/{slug}/{slug}.md', body)
            lines.append(f'- [{inline(obj["title"])}]({slug}/{slug}.md) — {status}')
        write(root, f'{folder}/{index}.md', '\n'.join(lines))
    for app in ('.agents', '.claude'):
        for name, desc in [('gerer-aios', 'Ranger, rechercher, intégrer et entretenir cet AIOS.'),
                           ('close', 'Clôturer une discussion et enregistrer le point de reprise de cet AIOS.'),
                           ('decisions', 'Arbitrer et mémoriser les décisions confirmées de cet AIOS.')]:
            write(root, f'{app}/skills/{name}/SKILL.md',
                  f'---\nname: {name}\ndescription: {desc}\n---\n\nLire et appliquer la [méthode commune](../../../.ai/skills/{name}/SKILL.md). Résoudre ses références depuis son dossier `.ai/skills/{name}/`. Ne pas maintenir une seconde méthode ici.')
    home = ['# Mon AIOS', '', '## Parcours', '']
    home += [f'- [{title}](<{folder}/{index}.md>)' for folder, index, title in sections]
    home += ['', '- [Contexte personnel](<3 - Ressources/Personnel/contexte.md>)', '- [Décisions](.ai/decisions/index.md)',
             '- [Bilans et reprise](.ai/bilans/index.md)', '- [Connexions](.ai/connexions.md)', '',
             '## Demandes utiles', '', '« Range cette capture. » · « Retrouve pourquoi nous avons choisi cela. » · « Clôture cette discussion. »', '',
             'Les méthodes vivent dans le noyau partagé. Les commandes disponibles dépendent de l’application ; ces demandes en langage naturel restent utilisables avec accès aux fichiers.']
    write(root, 'accueil.md', '\n'.join(home))
    write(root, 'log.md', f'# Journal\n\n## {today} — Installation\n\nSocle créé depuis le Grill-me fourni. Close, Décisions et gestion interne inclus. Aucun outil externe activé. [Accueil](accueil.md).')
    return check_links(root)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', required=True, type=Path)
    parser.add_argument('--profile', required=True, type=Path)
    parser.add_argument('--grill-me', required=True, type=Path)
    args = parser.parse_args()
    target = args.target.expanduser().absolute()
    if target.is_symlink():
        parser.error('Choisir un dossier réel, pas un lien symbolique.')
    if target.exists() and (not target.is_dir() or any(target.iterdir())):
        parser.error('La cible doit être neuve ou vide ; aucun fichier remplacé.')
    try:
        profile = json.loads(args.profile.read_text(encoding='utf-8'))
        validate_profile(profile)
        source = args.grill_me.read_text(encoding='utf-8')
        if not source.strip():
            raise ValueError('Le Grill-me est vide.')
        target.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='.aios-build-', dir=target.parent) as tmp:
            stage = Path(tmp) / 'vault'
            count = render(stage, profile, source)
            # Recheck after build; never overwrite files added while preparing.
            if target.exists():
                if not target.is_dir() or any(target.iterdir()):
                    raise ValueError('La cible a changé ; installation annulée.')
                target.rmdir()
            stage.rename(target)
        print(json.dumps({'target': str(target), 'files': sum(p.is_file() for p in target.rglob('*')), 'links_checked': count, 'status': 'installed'}, ensure_ascii=False))
    except (ValueError, OSError) as exc:
        parser.exit(1, f'Installation non terminée : {exc}\n')


if __name__ == '__main__':
    main()
