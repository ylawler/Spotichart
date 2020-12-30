import Project.AudioFeatures as af
import unittest

# 100% lines covered with coverage

class test_AudioFeatures(unittest.TestCase):

    def setup_audio_features(self):
        self.audioFeats = af.AudioFeatures()

        self.song_ids = ['5sLjenGt5pNrDd92Sc4HEw', '3iPwmwKYxRKchDa1oegQRg', '3ZCTVFBt2Brf31RLEnCkWJ']
        self.song_names = [('HYENA’S', 'Idaly'), ('Nu Heb Ik Paper', 'Glades'), ('everything i wanted', 'Billie Eilish')]

        self.audio_feats = {
            '5sLjenGt5pNrDd92Sc4HEw': [0.711, 0.694, 10, -8.288, 0, 0.355, 0.399, 1.69e-06, 0.393, 93.584],
            '3iPwmwKYxRKchDa1oegQRg': [0.824, 0.818, 9, -7.779, 1, 0.206, 0.0128, 0, 0.567, 104.997],
            '3ZCTVFBt2Brf31RLEnCkWJ': [0.704, 0.225, 6, -14.454, 0, 0.0994, 0.902, 0.657, 0.243, 120.006]
        }

    def check_file(self, filename, n_lines):
        with open(filename, 'r') as rf:
            lines = rf.readlines()
            counter = len(lines)
            return counter == n_lines

    ### TEST FUNCTIONS

    def test_get_features(self):
        self.setup_audio_features()
        self.audioFeats.get_features(self.song_ids)
        self.assertEqual(self.audioFeats.features, self.audio_feats)


    def test_get_features_one_song(self):
        self.setup_audio_features()
        one_song_id = ['5sLjenGt5pNrDd92Sc4HEw']
        one_song_feat = {'5sLjenGt5pNrDd92Sc4HEw': [0.711, 0.694, 10, -8.288, 0, 0.355, 0.399, 1.69e-06, 0.393, 93.584]}
        self.audioFeats.get_features(one_song_id)
        self.assertEqual(self.audioFeats.features, one_song_feat)

    def test_get_features_empty(self):
        self.setup_audio_features()

        song_ids = []
        self.audioFeats.get_features(song_ids)
        self.assertEqual(self.audioFeats.features, {})
        #assert x.features == {}

    def test_get_features_invalid(self):
        self.setup_audio_features()
        invalid_song_id = ['kjdsflkjlkajdlkf']
        self.assertEqual(self.audioFeats.get_features(invalid_song_id),{})




    def test_save_features(self):
        self.setup_audio_features()
        country_code = 'save'
        filename = f'testing_{country_code}_features.txt'
        n_lines = len(self.song_ids)

        self.audioFeats.save_features(filename, self.audio_feats)
        self.assertTrue(self.check_file(filename, n_lines))

    def test_load_features(self):
        self.setup_audio_features()
        country_code = 'load'
        filename = f'test_{country_code}_feats.txt'

        self.audioFeats.load_features(filename)
        self.assertEqual(self.audioFeats.features, self.audio_feats)


if __name__ == '__main__':
    unittest.main()