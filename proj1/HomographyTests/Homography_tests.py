import os
from glob import glob
import unittest
from random import uniform
from inspect import isclass
from Homography import *


class HomographyTestSuite(unittest.TestCase):

    # This flag will delete all mismatched images at the end of any full run.
    # Set to False if you want to investigate the images.
    deleteMismatched = True

    frontPoints = [(159.0, 136.0), (345.0, 85.0), (160.0, 276.0), (309.0, 216.0)]
    topPoints = [(84.0, 34.0), (239.0, 5.0), (159.0, 136.0), (345.0, 85.0)]
    effectPoints = [(84.0, 34.0), (239.0, 5.0), (160.0, 276.0), (309.0, 216.0)]

    effectList = ["rotate90", "rotate180", "rotate270", "flipHorizontally", "flipVertically", "transpose"]

    def test_EffectEnumExists(self):
        """
        Test for the existence of the Effect enum.
        """

        self.assertTrue(isclass(Effect))

    def test_EffectEnumMembers(self):
        """
        Test for the existence of the Effect enum members.
        """
        expectedValues = self.effectList

        for expectedValue in expectedValues:

            with self.subTest(expectedValue):
                self.assertIn(expectedValue, Effect.__members__)

    def test_HomographyInitializerWithMatrix(self):
        """
        Test the behavior of the homography initializer with a matrix.
        """
        with self.subTest(key="Good Matrix"):
            mat = [[1.2, 2.3, 4.5], [9.0, 4.4, 5.5], [0.0, 0.0, 1.0]]
            h = Homography(homographyMatrix=mat)
            self.assertIsInstance(h, Homography)

        with self.subTest(key="Bad Matrix 1"):
            # Not a 3 x 3
            mat = [[1.2, 2.3, 4.5], [9.0, 4.4, 5.5]]

            self.assertRaises(ValueError, Homography, homographyMatrix=mat)

        with self.subTest(key="Bad Matrix 2"):
            # Not all are floats.
            mat = [[1.2, 2.3, 4.5], [9.0, 4.4, 5.5], [0, 0, 1]]

            self.assertRaises(ValueError, Homography, homographyMatrix=mat)

        with self.subTest(key="Incorrect Parameter"):
            # Not all are floats.
            mat = [[1.2, 2.3, 4.5], [9.0, 4.4, 5.5], [0.0, 0.0, 1.0]]

            self.assertRaises(ValueError, Homography, homographyMat=mat)

    def test_HomographyInitializerWithPoints(self):
        """
        Test the behavior of the homography initializer with points.
        """
        u = lambda: (uniform(1.0, 10.0), uniform(1.0, 10.0))
        s = [u() for _ in range(4)]
        t = [u() for _ in range(4)]

        with self.subTest(key="Good Points"):
            h = Homography(sourcePoints=s, targetPoints=t)

            self.assertIsInstance(h, Homography)

        with self.subTest(key="Incorrect Parameter 1"):

            self.assertRaises(ValueError, Homography, sourcePts=s, targetPoints=t)

        with self.subTest(key="Incorrect Parameter 2"):

            self.assertRaises(ValueError, Homography, sourcePoints=s, targetPts=t)

        with self.subTest(key="Bad Points"):
            del s[-1]
            del t[0]

            self.assertRaises(ValueError, Homography, sourcePoints=s, targetPoints=t)

    def test_HomographyInitializerWithPointsAndEffect(self):
        """
        Test the behavior of the homography initializer with points.
        """
        u = lambda: (uniform(1.0, 10.0), uniform(1.0, 10.0))
        s = [u() for _ in range(4)]
        t = [u() for _ in range(4)]

        with self.subTest(key="Good Effect 1"):
            h = Homography(sourcePoints=s, targetPoints=t, effect=None)

            self.assertIsInstance(h, Homography)

        with self.subTest(key="Good Effect 2"):
            h = Homography(sourcePoints=s, targetPoints=t, effect=Effect.rotate90)

            self.assertIsInstance(h, Homography)

        with self.subTest(key="Incorrect Type"):

            self.assertRaises(TypeError, Homography, sourcePoints=s, targetPoints=t, effect="rotate90")

    def test_forwardProject(self):
        """
        Test the expected outcome of forward projection.
        """
        with self.subTest(key="No Rounding"):
            p = 3.5, 2.0
            affineH = np.array([[2, 0, 0], [0, 3, 0], [0, 0, 1]], dtype=np.float64).tolist()
            h = Homography(homographyMatrix=affineH)

            expectedValue = 7.0, 6.0
            actualValue = h.forwardProject(p)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="With Rounding"):
            p = 3.46, 1.89
            affineH = np.array([[1.75, 0, 0], [0, 3.5, 0], [0, 0, 1]], dtype=np.float64).tolist()
            h = Homography(homographyMatrix=affineH)

            expectedValue = 6.06, 6.61
            actualValue = h.forwardProject(p)

            self.assertEqual(expectedValue, actualValue)

    def test_inverseProject(self):
        """
        Test the expected outcome of inverse projection.
        """
        with self.subTest(key="No Rounding"):
            p = 7.0, 6.0
            affineH = np.array([[2, 0, 0], [0, 3, 0], [0, 0, 1]], dtype=np.float64).tolist()
            h = Homography(homographyMatrix=affineH)

            expectedValue = 3.5, 2.0
            actualValue = h.inverseProject(p)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="With Rounding"):
            p = 6.06, 6.62
            affineH = np.array([[1.75, 0, 0], [0, 3.5, 0], [0, 0, 1]], dtype=np.float64).tolist()
            h = Homography(homographyMatrix=affineH)

            expectedValue = 3.46, 1.89
            actualValue = h.inverseProject(p)

            self.assertEqual(expectedValue, actualValue)

    def test_computeHomography(self):
        """
        Test the homography computation using correspondences.
        """

        with self.subTest(key="Identity"):

            p = 3.4, 6.7
            s = [(0.0, 0.0), (150.0, 0.0), (0.0, 200.0), (150.0, 200.0)]
            t = [(0.0, 0.0), (150.0, 0.0), (0.0, 200.0), (150.0, 200.0)]
            h = Homography(sourcePoints=s, targetPoints=t)

            expectedValue = p
            actualValue = h.forwardProject(p)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Translation"):
            # Translate x by 10 and y by 20
            p = 3.4, 6.7
            s = [(0.0, 0.0), (150.0, 0.0), (0.0, 200.0), (150.0, 200.0)]
            t = [(10.0, 20.0), (160.0, 20.0), (10.0, 220.0), (160.0, 220.0)]
            h = Homography(sourcePoints=s, targetPoints=t)

            expectedValue = 13.4, 26.7
            actualValue = h.forwardProject(p)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Scaling"):
            # Scale x by 1.5 and y by 2.5
            p = 3.4, 6.7
            s = [(0.0, 0.0), (150.0, 0.0), (0.0, 200.0), (150.0, 200.0)]
            t = [(0.0, 0.0), (225.0, 0.0), (0.0, 500.0), (225.0, 500.0)]
            h = Homography(sourcePoints=s, targetPoints=t)

            expectedValue = 5.1, 16.75
            actualValue = h.forwardProject(p)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Rotation"):
            # 180° Rotation applied.
            p = 70.0, 80.0
            s = [(0.0, 0.0), (150.0, 0.0), (0.0, 200.0), (150.0, 200.0)]
            h = Homography(sourcePoints=s, targetPoints=s, effect=Effect.rotate180)

            expectedValue = 80.0, 120.0
            actualValue = h.forwardProject(p)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Random Matrix (Forward)"):
            p = 100.5, 55.3
            s = [(0.0, 0.0), (166.0, 0.0), (0.0, 150.0), (166.0, 150.0)]
            t = [(635, 545), (1380, 340), (640, 1105), (1235, 865)]
            h = Homography(sourcePoints=s, targetPoints=t)

            expectedValue = 1076.83, 641.56
            actualValue = h.forwardProject(p)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Random Matrix (Inverse)"):
            p = 1330.09, 792.18
            s = [(0.0, 0.0), (166.0, 0.0), (0.0, 150.0), (166.0, 150.0)]
            t = [(635, 545), (1380, 340), (640, 1105), (1235, 865)]
            h = Homography(sourcePoints=s, targetPoints=t)

            expectedValue = 193.35, 136.09
            actualValue = h.inverseProject(p)

            self.assertEqual(expectedValue, actualValue)

    def test_TransformationInitializer(self):
        """
        Test the behavior of the Transformation initializer.
        """
        with self.subTest(key="Good Image 1"):
            img = np.ones([10, 10], dtype=np.uint8)
            trans = Transformation(img)

            self.assertIsInstance(trans, Transformation)

        with self.subTest(key="Good Image 2"):
            img = np.ones([10, 10], dtype=np.uint8)
            trans = Transformation(img, None)

            self.assertIsInstance(trans, Transformation)

        with self.subTest(key="Good Homography"):
            img = np.ones([10, 10], dtype=np.uint8)
            mat = [[1.2, 2.3, 4.5], [9.0, 4.4, 5.5], [0.0, 0.0, 1.0]]
            h = Homography(homographyMatrix=mat)
            trans = Transformation(img, h)

            self.assertIsInstance(trans, Transformation)

        with self.subTest(key="Bad Image"):
            img = [[0, 0], [1, 1]]

            self.assertRaises(TypeError, Transformation, sourceImage=img)

        with self.subTest(key="Bad Homography"):
            img = np.ones([10, 10], dtype=np.uint8)
            h = [[1.2, 2.3, 4.5], [9.0, 4.4, 5.5], [0.0, 0.0, 1.0]]
            self.assertRaises(TypeError, Transformation, sourceImage=img, homography=h)

    def test_transformImageWhenImageIsBad(self):
        """
        Test the behavior of the transformImage against bad data.
        """
        img = np.ones([10, 10], dtype=np.uint8)
        mat = [[1.2, 2.3, 4.5], [9.0, 4.4, 5.5], [0.0, 0.0, 1.0]]
        h = Homography(homographyMatrix=mat)
        trans = Transformation(img, h)

        with self.subTest(key="Bad Type"):
            targetImg = [[1.2, 2.3, 4.5], [9.0, 4.4, 5.5], [0.0, 0.0, 1.0]]

            self.assertRaises(TypeError, trans.transformImage, targetImg)

        with self.subTest(key="Bad Dimensions"):
            targetImg = np.ones([10, 10, 3], dtype=np.uint8)

            self.assertRaises(ValueError, trans.transformImage, targetImg)

    def test_transformImageGray(self):
        """
        Test the transformation of several gray images.
        """
        filePaths = glob(r"TestImages\Gray*.png")
        for filePath in filePaths:
            fileName = os.path.basename(filePath)[:-4]

            with self.subTest(key=fileName + "Front"):
                areEqual = self.checkTransformation(Transformation, filePath, self.frontPoints, "WhiteSmall", "Front")
                self.assertTrue(areEqual)

            with self.subTest(key=fileName + "Top"):
                areEqual = self.checkTransformation(Transformation, filePath, self.topPoints, "WhiteSmall", "Top")
                self.assertTrue(areEqual)

    def test_transformImageGrayWithEffects(self):
        """
        Test the transformation of several gray images with effects.
        """
        filePaths = glob(r"TestImages\Gray*.png")
        for filePath in filePaths:

            fileName = os.path.basename(filePath)[:-4]
            for effect in self.effectList:

                with self.subTest(key=fileName + "_" + effect):

                    areEqual = self.checkTransformationWithEffects(Transformation, effect, filePath, "WhiteSmall")
                    self.assertTrue(areEqual)

    def test_colorTransformationInitializer(self):
        """
        Test the behavior of the ColorTransformation initializer.
        """
        with self.subTest(key="Good Image 1"):
            img = np.ones([10, 10, 3], dtype=np.uint8)
            trans = ColorTransformation(img)

            self.assertIsInstance(trans, ColorTransformation)

        with self.subTest(key="Good Image 2"):
            img = np.ones([10, 10, 3], dtype=np.uint8)
            trans = ColorTransformation(img, None)

            self.assertIsInstance(trans, ColorTransformation)

        with self.subTest(key="Good Homography"):
            img = np.ones([10, 10, 3], dtype=np.uint8)
            mat = [[1.2, 2.3, 4.5], [9.0, 4.4, 5.5], [0.0, 0.0, 1.0]]
            h = Homography(homographyMatrix=mat)
            trans = ColorTransformation(img, h)

            self.assertIsInstance(trans, ColorTransformation)

        with self.subTest(key="Bad Image Type"):
            img = [[0, 0], [1, 1]]

            self.assertRaises(TypeError, ColorTransformation, sourceImage=img)

        with self.subTest(key="Bad Image Dimensions"):
            img = np.ones([10, 10], dtype=np.uint8)

            self.assertRaises(ValueError, ColorTransformation, sourceImage=img)

        with self.subTest(key="Bad Homography"):
            img = np.ones([10, 10, 3], dtype=np.uint8)
            h = [[1.2, 2.3, 4.5], [9.0, 4.4, 5.5], [0.0, 0.0, 1.0]]

            self.assertRaises(TypeError, ColorTransformation, sourceImage=img, homography=h)

    def test_transformImageColor(self):
        """
        Test the transformation of several color images.
        """
        filePaths = glob(r"TestImages\Color*.png")
        for filePath in filePaths:

            fileName = os.path.basename(filePath)[:-4]

            with self.subTest(key=fileName + "Front"):
                areEqual = self.checkTransformation(ColorTransformation, filePath, self.frontPoints, "White3Small", "Front")
                self.assertTrue(areEqual)

            with self.subTest(key=fileName + "Top"):
                areEqual = self.checkTransformation(ColorTransformation, filePath, self.topPoints, "White3Small", "Top")
                self.assertTrue(areEqual)

    def test_transformImageColorWithEffects(self):
        """
        Test the transformation of several color images with effects.
        """
        filePaths = glob(r"TestImages\Color*.png")
        for filePath in filePaths:

            fileName = os.path.basename(filePath)[:-4]
            for effect in self.effectList:

                with self.subTest(key=fileName + "_" + effect):

                    areEqual = self.checkTransformationWithEffects(ColorTransformation, effect, filePath, "White3Small")
                    self.assertTrue(areEqual)

    def checkTransformation(self, TransType, filePath, frontPoints, baseContainerName, fileTag):
        """
        This is a support method to simplify transformation code.
        """
        fileName = os.path.basename(filePath)[:-4]
        sourceImage = imread(filePath)

        targetImagePath = r"TestImages\Target_{0}_{1}.png".format(fileName, fileTag)
        expectedImage = imread(targetImagePath)

        transformer = TransType(sourceImage)

        transformer.setupTransformation(frontPoints)
        containerImage = imread(r"TestImages\{0}.png".format(baseContainerName))
        actualImage = transformer.transformImage(containerImage)

        differenceFilePath = r"TestImages\Target_{0}_{1}_Mismatch.png".format(fileName, fileTag)
        areEqual = self.areImagesEqual(expectedImage, actualImage, differenceFilePath)

        return areEqual

    def checkTransformationWithEffects(self, TransType, eff, filePath, baseContainerName):
        """
        This is a support method to simplify effect checking.
        """
        fileName = os.path.basename(filePath)[:-4]
        sourceImage = imread(filePath)

        targetImagePath = r"TestImages\Target_{0}_{1}.png".format(fileName, eff)
        expectedImage = imread(targetImagePath)

        transformer = TransType(sourceImage)
        transformer.setupTransformation(self.effectPoints, Effect[eff])

        containerImage = imread(r"TestImages\{0}.png".format(baseContainerName))
        actualImage = transformer.transformImage(containerImage)

        differenceFilePath = r"TestImages\Target_{0}_{1}_Mismatch.png".format(fileName, eff)
        areEqual = self.areImagesEqual(expectedImage, actualImage, differenceFilePath)

        return areEqual

    def areImagesEqual(self, firstImage, secondImage, differenceFilePath):
        """
        Check if the two images are equal, and return True if they are, otherwise return False. Also, this method saves the
        difference image for later comparison.
        """
        difference = firstImage != secondImage

        if not np.any(difference):
            return True

        if firstImage.ndim == 3:
            differenceMap = np.any(difference, 2)
        else:
            differenceMap = difference

        differenceImage = 255 * np.array(differenceMap, np.uint8)

        print("Non zero = {0} in {1}".format(np.count_nonzero(differenceImage), differenceFilePath))
        imsave(differenceFilePath, differenceImage)

        # # Output file: Enable if you want to save the actual file.
        # outputFilePath = differenceFilePath.replace("Mismatch", "Output")
        # imsave(outputFilePath, secondImage)

        return False

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the created files, as unit tests are not supposed to change the environment.
        """

        if not cls.deleteMismatched:
            return

        mismatchedFiles = glob(r"TestImages\*Mismatch*")
        for filePath in mismatchedFiles:

            if os.path.exists(filePath):
                os.remove(filePath)


if __name__ == "__main__":
    unittest.main()
