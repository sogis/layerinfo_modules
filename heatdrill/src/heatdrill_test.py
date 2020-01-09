
from .heatdrill import layer_info
from .heatdrill import _testInit
import unittest

class TestLayerInfo(unittest.TestCase):

    SERVICE_URL: str = 'http://localhost:8080/service/'
    REQUEST_ID: str = 'requestId'
    TEXT_ROWS: str = 'infoTextRows'

    def test_success(self):

        _testInit(TestLayerInfo.SERVICE_URL, 10)
        f_dict = layer_info('fuu', 2637503, 1245807, None, None, None)
        feature = f_dict['features'][0]

        self.assertGreater(_attrValue(feature, TestLayerInfo.REQUEST_ID), 0, 'Module ended with error')

    def test_timeout(self):
        _testInit(TestLayerInfo.SERVICE_URL, 0.001)
        f_dict = layer_info('fuu', 2637503, 1245807, None, None, None)
        feature = f_dict['features'][0]

        self.assertLess(_attrValue(feature, TestLayerInfo.REQUEST_ID), 0, 'Module must fail due to timeout')
        _printRows(feature)

    def test_bogusUrl(self):

        _testInit('http://fuu/bar', 10)
        f_dict = layer_info('fuu', 2637503, 1245807, None, None, None)
        feature = f_dict['features'][0]

        self.assertLess(_attrValue(feature, TestLayerInfo.REQUEST_ID), 0, 'Module must fail due to invalid url')
        _printRows(feature)

    def test_outOfBounds(self):
        _testInit(TestLayerInfo.SERVICE_URL, 10)
        f_dict = layer_info('fuu', 2600000, 1200000, None, None, None)
        feature = f_dict['features'][0]

        self.assertLess(_attrValue(feature, TestLayerInfo.REQUEST_ID), 0, 'Module must fail due to out of bouds call')
        _printRows(feature)

    def test_validWKT_OnSuccess(self):

        _testInit(TestLayerInfo.SERVICE_URL, 10)
        f_dict = layer_info('fuu', 2637503, 1245807, None, None, None)
        feature = f_dict['features'][0]

        self.assertGreater(_attrValue(feature, TestLayerInfo.REQUEST_ID), 0, 'Module ended with error')
        self.assertEqual(feature['geometry'], 'POINT(2637503 1245807)', 'Returned Geometry is not "POINT(2637503 1245807)"')

    def test_validWKT_OnError(self):

        _testInit('http://fuu/bar', 10)
        f_dict = layer_info('fuu', 2637503, 1245807, None, None, None)
        feature = f_dict['features'][0]

        self.assertLess(_attrValue(feature, TestLayerInfo.REQUEST_ID), 0, 'Module must fail due to invalid url')
        self.assertEqual(feature['geometry'], 'POINT(2637503 1245807)', 'Returned Geometry is not "POINT(2637503 1245807)"')
        _printRows(feature)


def _attrValue(feature, attrName):
    res = None

    for d in feature['attributes']:
        if d['name'] is attrName:
            res = d['value']

    if res is None:
        raise Exception("Value for attribute {} not found.".format(attrName))

    return res

def _printRows(feature):
    rows = _attrValue(feature, 'infoTextRows')

    if rows is None:
        return

    for s in rows:
        print(s)


if __name__ == '__main__':
    unittest.main()

