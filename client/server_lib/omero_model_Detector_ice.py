# **********************************************************************
#
# Copyright (c) 2003-2011 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.4.2
#
# <auto-generated>
#
# Generated from file `Detector.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy, __builtin__
import omero_model_IObject_ice
import omero_RTypes_ice
import omero_System_ice
import omero_Collections_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Start of module omero
__name__ = 'omero'

# Start of module omero.model
__name__ = 'omero.model'

if not _M_omero.model.__dict__.has_key('DetectorType'):
    _M_omero.model._t_DetectorType = IcePy.declareClass('::omero::model::DetectorType')
    _M_omero.model._t_DetectorTypePrx = IcePy.declareProxy('::omero::model::DetectorType')

if not _M_omero.model.__dict__.has_key('Instrument'):
    _M_omero.model._t_Instrument = IcePy.declareClass('::omero::model::Instrument')
    _M_omero.model._t_InstrumentPrx = IcePy.declareProxy('::omero::model::Instrument')

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('Detector'):
    _M_omero.model.Detector = Ice.createTempClass()
    class Detector(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _manufacturer=None, _model=None, _lotNumber=None, _serialNumber=None, _voltage=None, _gain=None, _offsetValue=None, _zoom=None, _amplificationGain=None, _type=None, _instrument=None):
            if __builtin__.type(self) == _M_omero.model.Detector:
                raise RuntimeError('omero.model.Detector is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._version = _version
            self._manufacturer = _manufacturer
            self._model = _model
            self._lotNumber = _lotNumber
            self._serialNumber = _serialNumber
            self._voltage = _voltage
            self._gain = _gain
            self._offsetValue = _offsetValue
            self._zoom = _zoom
            self._amplificationGain = _amplificationGain
            self._type = _type
            self._instrument = _instrument

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Detector', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::Detector'

        def ice_staticId():
            return '::omero::model::Detector'
        ice_staticId = staticmethod(ice_staticId)

        def getVersion(self, current=None):
            pass

        def setVersion(self, theVersion, current=None):
            pass

        def getManufacturer(self, current=None):
            pass

        def setManufacturer(self, theManufacturer, current=None):
            pass

        def getModel(self, current=None):
            pass

        def setModel(self, theModel, current=None):
            pass

        def getLotNumber(self, current=None):
            pass

        def setLotNumber(self, theLotNumber, current=None):
            pass

        def getSerialNumber(self, current=None):
            pass

        def setSerialNumber(self, theSerialNumber, current=None):
            pass

        def getVoltage(self, current=None):
            pass

        def setVoltage(self, theVoltage, current=None):
            pass

        def getGain(self, current=None):
            pass

        def setGain(self, theGain, current=None):
            pass

        def getOffsetValue(self, current=None):
            pass

        def setOffsetValue(self, theOffsetValue, current=None):
            pass

        def getZoom(self, current=None):
            pass

        def setZoom(self, theZoom, current=None):
            pass

        def getAmplificationGain(self, current=None):
            pass

        def setAmplificationGain(self, theAmplificationGain, current=None):
            pass

        def getType(self, current=None):
            pass

        def setType(self, theType, current=None):
            pass

        def getInstrument(self, current=None):
            pass

        def setInstrument(self, theInstrument, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_Detector)

        __repr__ = __str__

    _M_omero.model.DetectorPrx = Ice.createTempClass()
    class DetectorPrx(_M_omero.model.IObjectPrx):

        def getVersion(self, _ctx=None):
            return _M_omero.model.Detector._op_getVersion.invoke(self, ((), _ctx))

        def begin_getVersion(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getVersion.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVersion(self, _r):
            return _M_omero.model.Detector._op_getVersion.end(self, _r)

        def setVersion(self, theVersion, _ctx=None):
            return _M_omero.model.Detector._op_setVersion.invoke(self, ((theVersion, ), _ctx))

        def begin_setVersion(self, theVersion, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setVersion.begin(self, ((theVersion, ), _response, _ex, _sent, _ctx))

        def end_setVersion(self, _r):
            return _M_omero.model.Detector._op_setVersion.end(self, _r)

        def getManufacturer(self, _ctx=None):
            return _M_omero.model.Detector._op_getManufacturer.invoke(self, ((), _ctx))

        def begin_getManufacturer(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getManufacturer.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getManufacturer(self, _r):
            return _M_omero.model.Detector._op_getManufacturer.end(self, _r)

        def setManufacturer(self, theManufacturer, _ctx=None):
            return _M_omero.model.Detector._op_setManufacturer.invoke(self, ((theManufacturer, ), _ctx))

        def begin_setManufacturer(self, theManufacturer, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setManufacturer.begin(self, ((theManufacturer, ), _response, _ex, _sent, _ctx))

        def end_setManufacturer(self, _r):
            return _M_omero.model.Detector._op_setManufacturer.end(self, _r)

        def getModel(self, _ctx=None):
            return _M_omero.model.Detector._op_getModel.invoke(self, ((), _ctx))

        def begin_getModel(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getModel.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getModel(self, _r):
            return _M_omero.model.Detector._op_getModel.end(self, _r)

        def setModel(self, theModel, _ctx=None):
            return _M_omero.model.Detector._op_setModel.invoke(self, ((theModel, ), _ctx))

        def begin_setModel(self, theModel, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setModel.begin(self, ((theModel, ), _response, _ex, _sent, _ctx))

        def end_setModel(self, _r):
            return _M_omero.model.Detector._op_setModel.end(self, _r)

        def getLotNumber(self, _ctx=None):
            return _M_omero.model.Detector._op_getLotNumber.invoke(self, ((), _ctx))

        def begin_getLotNumber(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getLotNumber.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getLotNumber(self, _r):
            return _M_omero.model.Detector._op_getLotNumber.end(self, _r)

        def setLotNumber(self, theLotNumber, _ctx=None):
            return _M_omero.model.Detector._op_setLotNumber.invoke(self, ((theLotNumber, ), _ctx))

        def begin_setLotNumber(self, theLotNumber, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setLotNumber.begin(self, ((theLotNumber, ), _response, _ex, _sent, _ctx))

        def end_setLotNumber(self, _r):
            return _M_omero.model.Detector._op_setLotNumber.end(self, _r)

        def getSerialNumber(self, _ctx=None):
            return _M_omero.model.Detector._op_getSerialNumber.invoke(self, ((), _ctx))

        def begin_getSerialNumber(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getSerialNumber.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getSerialNumber(self, _r):
            return _M_omero.model.Detector._op_getSerialNumber.end(self, _r)

        def setSerialNumber(self, theSerialNumber, _ctx=None):
            return _M_omero.model.Detector._op_setSerialNumber.invoke(self, ((theSerialNumber, ), _ctx))

        def begin_setSerialNumber(self, theSerialNumber, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setSerialNumber.begin(self, ((theSerialNumber, ), _response, _ex, _sent, _ctx))

        def end_setSerialNumber(self, _r):
            return _M_omero.model.Detector._op_setSerialNumber.end(self, _r)

        def getVoltage(self, _ctx=None):
            return _M_omero.model.Detector._op_getVoltage.invoke(self, ((), _ctx))

        def begin_getVoltage(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getVoltage.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVoltage(self, _r):
            return _M_omero.model.Detector._op_getVoltage.end(self, _r)

        def setVoltage(self, theVoltage, _ctx=None):
            return _M_omero.model.Detector._op_setVoltage.invoke(self, ((theVoltage, ), _ctx))

        def begin_setVoltage(self, theVoltage, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setVoltage.begin(self, ((theVoltage, ), _response, _ex, _sent, _ctx))

        def end_setVoltage(self, _r):
            return _M_omero.model.Detector._op_setVoltage.end(self, _r)

        def getGain(self, _ctx=None):
            return _M_omero.model.Detector._op_getGain.invoke(self, ((), _ctx))

        def begin_getGain(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getGain.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getGain(self, _r):
            return _M_omero.model.Detector._op_getGain.end(self, _r)

        def setGain(self, theGain, _ctx=None):
            return _M_omero.model.Detector._op_setGain.invoke(self, ((theGain, ), _ctx))

        def begin_setGain(self, theGain, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setGain.begin(self, ((theGain, ), _response, _ex, _sent, _ctx))

        def end_setGain(self, _r):
            return _M_omero.model.Detector._op_setGain.end(self, _r)

        def getOffsetValue(self, _ctx=None):
            return _M_omero.model.Detector._op_getOffsetValue.invoke(self, ((), _ctx))

        def begin_getOffsetValue(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getOffsetValue.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getOffsetValue(self, _r):
            return _M_omero.model.Detector._op_getOffsetValue.end(self, _r)

        def setOffsetValue(self, theOffsetValue, _ctx=None):
            return _M_omero.model.Detector._op_setOffsetValue.invoke(self, ((theOffsetValue, ), _ctx))

        def begin_setOffsetValue(self, theOffsetValue, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setOffsetValue.begin(self, ((theOffsetValue, ), _response, _ex, _sent, _ctx))

        def end_setOffsetValue(self, _r):
            return _M_omero.model.Detector._op_setOffsetValue.end(self, _r)

        def getZoom(self, _ctx=None):
            return _M_omero.model.Detector._op_getZoom.invoke(self, ((), _ctx))

        def begin_getZoom(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getZoom.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getZoom(self, _r):
            return _M_omero.model.Detector._op_getZoom.end(self, _r)

        def setZoom(self, theZoom, _ctx=None):
            return _M_omero.model.Detector._op_setZoom.invoke(self, ((theZoom, ), _ctx))

        def begin_setZoom(self, theZoom, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setZoom.begin(self, ((theZoom, ), _response, _ex, _sent, _ctx))

        def end_setZoom(self, _r):
            return _M_omero.model.Detector._op_setZoom.end(self, _r)

        def getAmplificationGain(self, _ctx=None):
            return _M_omero.model.Detector._op_getAmplificationGain.invoke(self, ((), _ctx))

        def begin_getAmplificationGain(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getAmplificationGain.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getAmplificationGain(self, _r):
            return _M_omero.model.Detector._op_getAmplificationGain.end(self, _r)

        def setAmplificationGain(self, theAmplificationGain, _ctx=None):
            return _M_omero.model.Detector._op_setAmplificationGain.invoke(self, ((theAmplificationGain, ), _ctx))

        def begin_setAmplificationGain(self, theAmplificationGain, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setAmplificationGain.begin(self, ((theAmplificationGain, ), _response, _ex, _sent, _ctx))

        def end_setAmplificationGain(self, _r):
            return _M_omero.model.Detector._op_setAmplificationGain.end(self, _r)

        def getType(self, _ctx=None):
            return _M_omero.model.Detector._op_getType.invoke(self, ((), _ctx))

        def begin_getType(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getType.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getType(self, _r):
            return _M_omero.model.Detector._op_getType.end(self, _r)

        def setType(self, theType, _ctx=None):
            return _M_omero.model.Detector._op_setType.invoke(self, ((theType, ), _ctx))

        def begin_setType(self, theType, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setType.begin(self, ((theType, ), _response, _ex, _sent, _ctx))

        def end_setType(self, _r):
            return _M_omero.model.Detector._op_setType.end(self, _r)

        def getInstrument(self, _ctx=None):
            return _M_omero.model.Detector._op_getInstrument.invoke(self, ((), _ctx))

        def begin_getInstrument(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_getInstrument.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getInstrument(self, _r):
            return _M_omero.model.Detector._op_getInstrument.end(self, _r)

        def setInstrument(self, theInstrument, _ctx=None):
            return _M_omero.model.Detector._op_setInstrument.invoke(self, ((theInstrument, ), _ctx))

        def begin_setInstrument(self, theInstrument, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Detector._op_setInstrument.begin(self, ((theInstrument, ), _response, _ex, _sent, _ctx))

        def end_setInstrument(self, _r):
            return _M_omero.model.Detector._op_setInstrument.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.DetectorPrx.ice_checkedCast(proxy, '::omero::model::Detector', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.DetectorPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_DetectorPrx = IcePy.defineProxy('::omero::model::Detector', DetectorPrx)

    _M_omero.model._t_Detector = IcePy.declareClass('::omero::model::Detector')

    _M_omero.model._t_Detector = IcePy.defineClass('::omero::model::Detector', Detector, (), True, _M_omero.model._t_IObject, (), (
        ('_version', (), _M_omero._t_RInt),
        ('_manufacturer', (), _M_omero._t_RString),
        ('_model', (), _M_omero._t_RString),
        ('_lotNumber', (), _M_omero._t_RString),
        ('_serialNumber', (), _M_omero._t_RString),
        ('_voltage', (), _M_omero._t_RDouble),
        ('_gain', (), _M_omero._t_RDouble),
        ('_offsetValue', (), _M_omero._t_RDouble),
        ('_zoom', (), _M_omero._t_RDouble),
        ('_amplificationGain', (), _M_omero._t_RDouble),
        ('_type', (), _M_omero.model._t_DetectorType),
        ('_instrument', (), _M_omero.model._t_Instrument)
    ))
    Detector._ice_type = _M_omero.model._t_Detector

    Detector._op_getVersion = IcePy.Operation('getVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RInt, ())
    Detector._op_setVersion = IcePy.Operation('setVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RInt),), (), None, ())
    Detector._op_getManufacturer = IcePy.Operation('getManufacturer', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    Detector._op_setManufacturer = IcePy.Operation('setManufacturer', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())
    Detector._op_getModel = IcePy.Operation('getModel', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    Detector._op_setModel = IcePy.Operation('setModel', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())
    Detector._op_getLotNumber = IcePy.Operation('getLotNumber', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    Detector._op_setLotNumber = IcePy.Operation('setLotNumber', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())
    Detector._op_getSerialNumber = IcePy.Operation('getSerialNumber', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    Detector._op_setSerialNumber = IcePy.Operation('setSerialNumber', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())
    Detector._op_getVoltage = IcePy.Operation('getVoltage', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RDouble, ())
    Detector._op_setVoltage = IcePy.Operation('setVoltage', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RDouble),), (), None, ())
    Detector._op_getGain = IcePy.Operation('getGain', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RDouble, ())
    Detector._op_setGain = IcePy.Operation('setGain', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RDouble),), (), None, ())
    Detector._op_getOffsetValue = IcePy.Operation('getOffsetValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RDouble, ())
    Detector._op_setOffsetValue = IcePy.Operation('setOffsetValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RDouble),), (), None, ())
    Detector._op_getZoom = IcePy.Operation('getZoom', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RDouble, ())
    Detector._op_setZoom = IcePy.Operation('setZoom', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RDouble),), (), None, ())
    Detector._op_getAmplificationGain = IcePy.Operation('getAmplificationGain', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RDouble, ())
    Detector._op_setAmplificationGain = IcePy.Operation('setAmplificationGain', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RDouble),), (), None, ())
    Detector._op_getType = IcePy.Operation('getType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_DetectorType, ())
    Detector._op_setType = IcePy.Operation('setType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_DetectorType),), (), None, ())
    Detector._op_getInstrument = IcePy.Operation('getInstrument', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_Instrument, ())
    Detector._op_setInstrument = IcePy.Operation('setInstrument', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_Instrument),), (), None, ())

    _M_omero.model.Detector = Detector
    del Detector

    _M_omero.model.DetectorPrx = DetectorPrx
    del DetectorPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
