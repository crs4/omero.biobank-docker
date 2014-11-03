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
# Generated from file `Action.ice'
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

if not _M_omero.model.__dict__.has_key('ActionSetup'):
    _M_omero.model._t_ActionSetup = IcePy.declareClass('::omero::model::ActionSetup')
    _M_omero.model._t_ActionSetupPrx = IcePy.declareProxy('::omero::model::ActionSetup')

if not _M_omero.model.__dict__.has_key('Device'):
    _M_omero.model._t_Device = IcePy.declareClass('::omero::model::Device')
    _M_omero.model._t_DevicePrx = IcePy.declareProxy('::omero::model::Device')

if not _M_omero.model.__dict__.has_key('ActionCategory'):
    _M_omero.model._t_ActionCategory = IcePy.declareClass('::omero::model::ActionCategory')
    _M_omero.model._t_ActionCategoryPrx = IcePy.declareProxy('::omero::model::ActionCategory')

if not _M_omero.model.__dict__.has_key('Study'):
    _M_omero.model._t_Study = IcePy.declareClass('::omero::model::Study')
    _M_omero.model._t_StudyPrx = IcePy.declareProxy('::omero::model::Study')

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('Action'):
    _M_omero.model.Action = Ice.createTempClass()
    class Action(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _vid=None, _beginTime=None, _endTime=None, _setup=None, _device=None, _actionCategory=None, _operator=None, _context=None, _description=None):
            if __builtin__.type(self) == _M_omero.model.Action:
                raise RuntimeError('omero.model.Action is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._version = _version
            self._vid = _vid
            self._beginTime = _beginTime
            self._endTime = _endTime
            self._setup = _setup
            self._device = _device
            self._actionCategory = _actionCategory
            self._operator = _operator
            self._context = _context
            self._description = _description

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Action', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::Action'

        def ice_staticId():
            return '::omero::model::Action'
        ice_staticId = staticmethod(ice_staticId)

        def getVersion(self, current=None):
            pass

        def setVersion(self, theVersion, current=None):
            pass

        def getVid(self, current=None):
            pass

        def setVid(self, theVid, current=None):
            pass

        def getBeginTime(self, current=None):
            pass

        def setBeginTime(self, theBeginTime, current=None):
            pass

        def getEndTime(self, current=None):
            pass

        def setEndTime(self, theEndTime, current=None):
            pass

        def getSetup(self, current=None):
            pass

        def setSetup(self, theSetup, current=None):
            pass

        def getDevice(self, current=None):
            pass

        def setDevice(self, theDevice, current=None):
            pass

        def getActionCategory(self, current=None):
            pass

        def setActionCategory(self, theActionCategory, current=None):
            pass

        def getOperator(self, current=None):
            pass

        def setOperator(self, theOperator, current=None):
            pass

        def getContext(self, current=None):
            pass

        def setContext(self, theContext, current=None):
            pass

        def getDescription(self, current=None):
            pass

        def setDescription(self, theDescription, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_Action)

        __repr__ = __str__

    _M_omero.model.ActionPrx = Ice.createTempClass()
    class ActionPrx(_M_omero.model.IObjectPrx):

        def getVersion(self, _ctx=None):
            return _M_omero.model.Action._op_getVersion.invoke(self, ((), _ctx))

        def begin_getVersion(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_getVersion.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVersion(self, _r):
            return _M_omero.model.Action._op_getVersion.end(self, _r)

        def setVersion(self, theVersion, _ctx=None):
            return _M_omero.model.Action._op_setVersion.invoke(self, ((theVersion, ), _ctx))

        def begin_setVersion(self, theVersion, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_setVersion.begin(self, ((theVersion, ), _response, _ex, _sent, _ctx))

        def end_setVersion(self, _r):
            return _M_omero.model.Action._op_setVersion.end(self, _r)

        def getVid(self, _ctx=None):
            return _M_omero.model.Action._op_getVid.invoke(self, ((), _ctx))

        def begin_getVid(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_getVid.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVid(self, _r):
            return _M_omero.model.Action._op_getVid.end(self, _r)

        def setVid(self, theVid, _ctx=None):
            return _M_omero.model.Action._op_setVid.invoke(self, ((theVid, ), _ctx))

        def begin_setVid(self, theVid, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_setVid.begin(self, ((theVid, ), _response, _ex, _sent, _ctx))

        def end_setVid(self, _r):
            return _M_omero.model.Action._op_setVid.end(self, _r)

        def getBeginTime(self, _ctx=None):
            return _M_omero.model.Action._op_getBeginTime.invoke(self, ((), _ctx))

        def begin_getBeginTime(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_getBeginTime.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getBeginTime(self, _r):
            return _M_omero.model.Action._op_getBeginTime.end(self, _r)

        def setBeginTime(self, theBeginTime, _ctx=None):
            return _M_omero.model.Action._op_setBeginTime.invoke(self, ((theBeginTime, ), _ctx))

        def begin_setBeginTime(self, theBeginTime, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_setBeginTime.begin(self, ((theBeginTime, ), _response, _ex, _sent, _ctx))

        def end_setBeginTime(self, _r):
            return _M_omero.model.Action._op_setBeginTime.end(self, _r)

        def getEndTime(self, _ctx=None):
            return _M_omero.model.Action._op_getEndTime.invoke(self, ((), _ctx))

        def begin_getEndTime(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_getEndTime.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getEndTime(self, _r):
            return _M_omero.model.Action._op_getEndTime.end(self, _r)

        def setEndTime(self, theEndTime, _ctx=None):
            return _M_omero.model.Action._op_setEndTime.invoke(self, ((theEndTime, ), _ctx))

        def begin_setEndTime(self, theEndTime, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_setEndTime.begin(self, ((theEndTime, ), _response, _ex, _sent, _ctx))

        def end_setEndTime(self, _r):
            return _M_omero.model.Action._op_setEndTime.end(self, _r)

        def getSetup(self, _ctx=None):
            return _M_omero.model.Action._op_getSetup.invoke(self, ((), _ctx))

        def begin_getSetup(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_getSetup.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getSetup(self, _r):
            return _M_omero.model.Action._op_getSetup.end(self, _r)

        def setSetup(self, theSetup, _ctx=None):
            return _M_omero.model.Action._op_setSetup.invoke(self, ((theSetup, ), _ctx))

        def begin_setSetup(self, theSetup, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_setSetup.begin(self, ((theSetup, ), _response, _ex, _sent, _ctx))

        def end_setSetup(self, _r):
            return _M_omero.model.Action._op_setSetup.end(self, _r)

        def getDevice(self, _ctx=None):
            return _M_omero.model.Action._op_getDevice.invoke(self, ((), _ctx))

        def begin_getDevice(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_getDevice.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getDevice(self, _r):
            return _M_omero.model.Action._op_getDevice.end(self, _r)

        def setDevice(self, theDevice, _ctx=None):
            return _M_omero.model.Action._op_setDevice.invoke(self, ((theDevice, ), _ctx))

        def begin_setDevice(self, theDevice, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_setDevice.begin(self, ((theDevice, ), _response, _ex, _sent, _ctx))

        def end_setDevice(self, _r):
            return _M_omero.model.Action._op_setDevice.end(self, _r)

        def getActionCategory(self, _ctx=None):
            return _M_omero.model.Action._op_getActionCategory.invoke(self, ((), _ctx))

        def begin_getActionCategory(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_getActionCategory.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getActionCategory(self, _r):
            return _M_omero.model.Action._op_getActionCategory.end(self, _r)

        def setActionCategory(self, theActionCategory, _ctx=None):
            return _M_omero.model.Action._op_setActionCategory.invoke(self, ((theActionCategory, ), _ctx))

        def begin_setActionCategory(self, theActionCategory, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_setActionCategory.begin(self, ((theActionCategory, ), _response, _ex, _sent, _ctx))

        def end_setActionCategory(self, _r):
            return _M_omero.model.Action._op_setActionCategory.end(self, _r)

        def getOperator(self, _ctx=None):
            return _M_omero.model.Action._op_getOperator.invoke(self, ((), _ctx))

        def begin_getOperator(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_getOperator.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getOperator(self, _r):
            return _M_omero.model.Action._op_getOperator.end(self, _r)

        def setOperator(self, theOperator, _ctx=None):
            return _M_omero.model.Action._op_setOperator.invoke(self, ((theOperator, ), _ctx))

        def begin_setOperator(self, theOperator, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_setOperator.begin(self, ((theOperator, ), _response, _ex, _sent, _ctx))

        def end_setOperator(self, _r):
            return _M_omero.model.Action._op_setOperator.end(self, _r)

        def getContext(self, _ctx=None):
            return _M_omero.model.Action._op_getContext.invoke(self, ((), _ctx))

        def begin_getContext(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_getContext.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getContext(self, _r):
            return _M_omero.model.Action._op_getContext.end(self, _r)

        def setContext(self, theContext, _ctx=None):
            return _M_omero.model.Action._op_setContext.invoke(self, ((theContext, ), _ctx))

        def begin_setContext(self, theContext, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_setContext.begin(self, ((theContext, ), _response, _ex, _sent, _ctx))

        def end_setContext(self, _r):
            return _M_omero.model.Action._op_setContext.end(self, _r)

        def getDescription(self, _ctx=None):
            return _M_omero.model.Action._op_getDescription.invoke(self, ((), _ctx))

        def begin_getDescription(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_getDescription.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getDescription(self, _r):
            return _M_omero.model.Action._op_getDescription.end(self, _r)

        def setDescription(self, theDescription, _ctx=None):
            return _M_omero.model.Action._op_setDescription.invoke(self, ((theDescription, ), _ctx))

        def begin_setDescription(self, theDescription, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Action._op_setDescription.begin(self, ((theDescription, ), _response, _ex, _sent, _ctx))

        def end_setDescription(self, _r):
            return _M_omero.model.Action._op_setDescription.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.ActionPrx.ice_checkedCast(proxy, '::omero::model::Action', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.ActionPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_ActionPrx = IcePy.defineProxy('::omero::model::Action', ActionPrx)

    _M_omero.model._t_Action = IcePy.declareClass('::omero::model::Action')

    _M_omero.model._t_Action = IcePy.defineClass('::omero::model::Action', Action, (), True, _M_omero.model._t_IObject, (), (
        ('_version', (), _M_omero._t_RInt),
        ('_vid', (), _M_omero._t_RString),
        ('_beginTime', (), _M_omero._t_RTime),
        ('_endTime', (), _M_omero._t_RTime),
        ('_setup', (), _M_omero.model._t_ActionSetup),
        ('_device', (), _M_omero.model._t_Device),
        ('_actionCategory', (), _M_omero.model._t_ActionCategory),
        ('_operator', (), _M_omero._t_RString),
        ('_context', (), _M_omero.model._t_Study),
        ('_description', (), _M_omero._t_RString)
    ))
    Action._ice_type = _M_omero.model._t_Action

    Action._op_getVersion = IcePy.Operation('getVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RInt, ())
    Action._op_setVersion = IcePy.Operation('setVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RInt),), (), None, ())
    Action._op_getVid = IcePy.Operation('getVid', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    Action._op_setVid = IcePy.Operation('setVid', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())
    Action._op_getBeginTime = IcePy.Operation('getBeginTime', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RTime, ())
    Action._op_setBeginTime = IcePy.Operation('setBeginTime', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RTime),), (), None, ())
    Action._op_getEndTime = IcePy.Operation('getEndTime', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RTime, ())
    Action._op_setEndTime = IcePy.Operation('setEndTime', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RTime),), (), None, ())
    Action._op_getSetup = IcePy.Operation('getSetup', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_ActionSetup, ())
    Action._op_setSetup = IcePy.Operation('setSetup', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_ActionSetup),), (), None, ())
    Action._op_getDevice = IcePy.Operation('getDevice', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_Device, ())
    Action._op_setDevice = IcePy.Operation('setDevice', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_Device),), (), None, ())
    Action._op_getActionCategory = IcePy.Operation('getActionCategory', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_ActionCategory, ())
    Action._op_setActionCategory = IcePy.Operation('setActionCategory', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_ActionCategory),), (), None, ())
    Action._op_getOperator = IcePy.Operation('getOperator', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    Action._op_setOperator = IcePy.Operation('setOperator', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())
    Action._op_getContext = IcePy.Operation('getContext', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero.model._t_Study, ())
    Action._op_setContext = IcePy.Operation('setContext', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero.model._t_Study),), (), None, ())
    Action._op_getDescription = IcePy.Operation('getDescription', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    Action._op_setDescription = IcePy.Operation('setDescription', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())

    _M_omero.model.Action = Action
    del Action

    _M_omero.model.ActionPrx = ActionPrx
    del ActionPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero