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
# Generated from file `Tube.ice'
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
import omero_model_Vessel_ice

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

if not _M_omero.model.__dict__.has_key('VesselContent'):
    _M_omero.model._t_VesselContent = IcePy.declareClass('::omero::model::VesselContent')
    _M_omero.model._t_VesselContentPrx = IcePy.declareProxy('::omero::model::VesselContent')

if not _M_omero.model.__dict__.has_key('VesselStatus'):
    _M_omero.model._t_VesselStatus = IcePy.declareClass('::omero::model::VesselStatus')
    _M_omero.model._t_VesselStatusPrx = IcePy.declareProxy('::omero::model::VesselStatus')

if not _M_omero.model.__dict__.has_key('Action'):
    _M_omero.model._t_Action = IcePy.declareClass('::omero::model::Action')
    _M_omero.model._t_ActionPrx = IcePy.declareProxy('::omero::model::Action')

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('Tube'):
    _M_omero.model.Tube = Ice.createTempClass()
    class Tube(_M_omero.model.Vessel):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _vid=None, _activationDate=None, _destructionDate=None, _currentVolume=None, _initialVolume=None, _content=None, _status=None, _action=None, _lastUpdate=None, _label=None, _barcode=None):
            if __builtin__.type(self) == _M_omero.model.Tube:
                raise RuntimeError('omero.model.Tube is an abstract class')
            _M_omero.model.Vessel.__init__(self, _id, _details, _loaded, _version, _vid, _activationDate, _destructionDate, _currentVolume, _initialVolume, _content, _status, _action, _lastUpdate)
            self._label = _label
            self._barcode = _barcode

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::IObject', '::omero::model::Tube', '::omero::model::Vessel')

        def ice_id(self, current=None):
            return '::omero::model::Tube'

        def ice_staticId():
            return '::omero::model::Tube'
        ice_staticId = staticmethod(ice_staticId)

        def getLabel(self, current=None):
            pass

        def setLabel(self, theLabel, current=None):
            pass

        def getBarcode(self, current=None):
            pass

        def setBarcode(self, theBarcode, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_Tube)

        __repr__ = __str__

    _M_omero.model.TubePrx = Ice.createTempClass()
    class TubePrx(_M_omero.model.VesselPrx):

        def getLabel(self, _ctx=None):
            return _M_omero.model.Tube._op_getLabel.invoke(self, ((), _ctx))

        def begin_getLabel(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Tube._op_getLabel.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getLabel(self, _r):
            return _M_omero.model.Tube._op_getLabel.end(self, _r)

        def setLabel(self, theLabel, _ctx=None):
            return _M_omero.model.Tube._op_setLabel.invoke(self, ((theLabel, ), _ctx))

        def begin_setLabel(self, theLabel, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Tube._op_setLabel.begin(self, ((theLabel, ), _response, _ex, _sent, _ctx))

        def end_setLabel(self, _r):
            return _M_omero.model.Tube._op_setLabel.end(self, _r)

        def getBarcode(self, _ctx=None):
            return _M_omero.model.Tube._op_getBarcode.invoke(self, ((), _ctx))

        def begin_getBarcode(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Tube._op_getBarcode.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getBarcode(self, _r):
            return _M_omero.model.Tube._op_getBarcode.end(self, _r)

        def setBarcode(self, theBarcode, _ctx=None):
            return _M_omero.model.Tube._op_setBarcode.invoke(self, ((theBarcode, ), _ctx))

        def begin_setBarcode(self, theBarcode, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Tube._op_setBarcode.begin(self, ((theBarcode, ), _response, _ex, _sent, _ctx))

        def end_setBarcode(self, _r):
            return _M_omero.model.Tube._op_setBarcode.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.TubePrx.ice_checkedCast(proxy, '::omero::model::Tube', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.TubePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_TubePrx = IcePy.defineProxy('::omero::model::Tube', TubePrx)

    _M_omero.model._t_Tube = IcePy.declareClass('::omero::model::Tube')

    _M_omero.model._t_Tube = IcePy.defineClass('::omero::model::Tube', Tube, (), True, _M_omero.model._t_Vessel, (), (
        ('_label', (), _M_omero._t_RString),
        ('_barcode', (), _M_omero._t_RString)
    ))
    Tube._ice_type = _M_omero.model._t_Tube

    Tube._op_getLabel = IcePy.Operation('getLabel', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    Tube._op_setLabel = IcePy.Operation('setLabel', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())
    Tube._op_getBarcode = IcePy.Operation('getBarcode', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    Tube._op_setBarcode = IcePy.Operation('setBarcode', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())

    _M_omero.model.Tube = Tube
    del Tube

    _M_omero.model.TubePrx = TubePrx
    del TubePrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
