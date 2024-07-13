from EmotionDetection.emotion_detection import emotion_detector
import unittest
class TestEmotion_Detection(unittest.TestCase):
    def test_emotion_detector(self):
        resultat = emotion_detector('I am glad this happened')
        self.assertEqual(resultat['dominant_emotion'], 'joy')
        resultat_1 = emotion_detector('I am really mad about this')
        self.assertEqual(resultat_1['dominant_emotion'], 'anger')
        resultat_2 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(resultat_2['dominant_emotion'], 'disgust')
        resultat_3 = emotion_detector('I am so sad about this')
        self.assertEqual(resultat_3['dominant_emotion'], 'sadness')
        resultat_4 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(resultat_4['dominant_emotion'], 'fear')

unittest.main()
