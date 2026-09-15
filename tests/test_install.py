import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'aios-bootstrap-atelier/scripts/install.py'


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.target = self.root / 'Mon AIOS'
        self.profile = self.root / 'profile.json'
        self.source = self.root / 'grill.md'
        self.source.write_text('# Entretien fictif\nUn guide choisi, un podcast seulement envisagé.\n\n', encoding='utf-8')
        self.data = {'name': 'Camille Exemple', 'context': 'Consultante fictive.',
                     'projects': [{'slug': 'guide', 'title': 'Guide', 'description': 'Guide choisi.', 'status': 'actif'}],
                     'open_questions': ['Podcast non engagé.']}

    def run_install(self):
        self.profile.write_text(json.dumps(self.data), encoding='utf-8')
        return subprocess.run([sys.executable, str(SCRIPT), '--target', str(self.target), '--profile', str(self.profile),
                               '--grill-me', str(self.source)], capture_output=True, text=True)

    def snapshot(self):
        return {str(p.relative_to(self.target)): p.read_bytes() for p in self.target.rglob('*') if p.is_file()}

    def test_fresh_profile_and_shared_methods(self):
        result = self.run_install()
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertGreater(report['links_checked'], 25)
        self.assertEqual((self.target / '.ai/inputs/grill-me.md').read_text(), self.source.read_text())
        self.assertTrue((self.target / '1 - Projets/guide/guide.md').is_file())
        self.assertFalse((self.target / '1 - Projets/podcast').exists())
        self.assertEqual({p.name for p in (self.target / '3 - Ressources').iterdir()}, {'ressources.md', 'Personnel'})
        for app in ('.agents', '.claude'):
            for name in ('close', 'decisions', 'gerer-aios'):
                wrapper = self.target / app / 'skills' / name / 'SKILL.md'
                self.assertFalse(wrapper.is_symlink())
                self.assertTrue((wrapper.parent / f'../../../.ai/skills/{name}/SKILL.md').resolve().is_file())

    def test_existing_content_preserved(self):
        self.target.mkdir()
        (self.target / 'decision.md').write_text('Choix à préserver')
        before = self.snapshot()
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertEqual(before, self.snapshot())

    def test_second_install_preserved(self):
        self.assertEqual(self.run_install().returncode, 0)
        before = self.snapshot()
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertEqual(before, self.snapshot())

    def test_slug_cannot_escape_and_no_partial_target(self):
        self.data['projects'][0]['slug'] = '../../escape'
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertFalse(self.target.exists())
        self.assertFalse((self.root / 'escape').exists())

    def test_status_is_not_assumed(self):
        del self.data['projects'][0]['status']
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertFalse(self.target.exists())

    def test_no_project_is_required(self):
        self.data['projects'] = []
        self.assertEqual(self.run_install().returncode, 0)
        self.assertEqual(list((self.target / '1 - Projets').iterdir()), [self.target / '1 - Projets/projets.md'])


if __name__ == '__main__':
    unittest.main()
