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
# Generated from file `SlottedContainer.ice'
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
import omero_model_Container_ice

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

if not _M_omero.model.__dict__.has_key('ContainerStatus'):
    _M_omero.model._t_ContainerStatus = IcePy.declareClass('::omero::model::ContainerStatus')
    _M_omero.model._t_ContainerStatusPrx = IcePy.declareProxy('::omero::model::ContainerStatus')

if not _M_omero.model.__dict__.has_key('Action'):
    _M_omero.model._t_Action = IcePy.declareClass('::omero::model::Action')
    _M_omero.model._t_ActionPrx = IcePy.declareProxy('::omero::model::Action')

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('SlottedContainer'):
    _M_omero.model.SlottedContainer = Ice.createTempClass()
    class SlottedContainer(_M_omero.model.Container):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _vid=None, _label=None, _creationDate=None, _action=None, _lastUpdate=None, _barcode=None, _status=None, _numberOfSlots=None):
            if __builtin__.type(self) == _M_omero.model.SlottedContainer:
                raise RuntimeError('omero.model.SlottedContainer is an abstract class')
            _M_omero.model.Container.__init__(self, _id, _details, _loaded, _version, _vid, _label, _creationDate, _action, _lastUpdate, _barcode, _status)
            self._numberOfSlots = _numberOfSlots

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Container', '::omero::model::IObject', '::omero::model::SlottedContainer', '::omero::model::VLCollection')

        def ice_id(self, current=None):
            return '::omero::model::SlottedContainer'

        def ice_staticId():
            return '::omero::model::SlottedContainer'
        ice_staticId = staticmethod(ice_staticId)

        def getNumberOfSlots(self, current=None):
            pass

        def setNumberOfSlots(self, theNumberOfSlots, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_SlottedContainer)

        __repr__ = __str__

    _M_omero.model.SlottedContainerPrx = Ice.createTempClass()
    class SlottedContainerPrx(_M_omero.model.ContainerPrx):

        def getNumberOfSlots(self, _ctx=None):
            return _M_omero.model.SlottedContainer._op_getNumberOfSlots.invoke(self, ((), _ctx))

        def begin_getNumberOfSlots(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.SlottedContainer._op_getNumberOfSlots.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getNumberOfSlots(self, _r):
            return _M_omero.model.SlottedContainer._op_getNumberOfSlots.end(self, _r)

        def setNumberOfSlots(self, theNumberOfSlots, _ctx=None):
            return _M_omero.model.SlottedContainer._op_setNumberOfSlots.invoke(self, ((theNumberOfSlots, ), _ctx))

        def begin_setNumberOfSlots(self, theNumberOfSlots, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.SlottedContainer._op_setNumberOfSlots.begin(self, ((theNumberOfSlots, ), _response, _ex, _sent, _ctx))

        def end_setNumberOfSlots(self, _r):
            return _M_omero.model.SlottedContainer._op_setNumberOfSlots.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.SlottedContainerPrx.ice_checkedCast(proxy, '::omero::model::SlottedContainer', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.SlottedContainerPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_SlottedContainerPrx = IcePy.defineProxy('::omero::model::SlottedContainer', SlottedContainerPrx)

    _M_omero.model._t_SlottedContainer = IcePy.declareClass('::omero::model::SlottedContainer')

    _M_omero.model._t_SlottedContainer = IcePy.defineClass('::omero::model::SlottedContainer', SlottedContainer, (), True, _M_omero.model._t_Container, (), (('_numberOfSlots', (), _M_omero._t_RInt),))
    SlottedContainer._ice_type = _M_omero.model._t_SlottedContainer

    SlottedContainer._op_getNumberOfSlots = IcePy.Operation('getNumberOfSlots', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RInt, ())
    SlottedContainer._op_setNumberOfSlots = IcePy.Operation('setNumberOfSlots', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RInt),), (), None, ())

    _M_omero.model.SlottedContainer = SlottedContainer
    del SlottedContainer

    _M_omero.model.SlottedContainerPrx = SlottedContainerPrx
    del SlottedContainerPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero