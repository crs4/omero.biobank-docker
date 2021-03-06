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
# Generated from file `IlluminaArrayOfArraysClass.ice'
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

# Start of module omero.model.enums
_M_omero.model.enums = Ice.openModule('omero.model.enums')
__name__ = 'omero.model.enums'

_M_omero.model.enums.IlluminaArrayOfArraysClassSlide = "Slide"

_M_omero.model.enums.IlluminaArrayOfArraysClassUNKNOWN = "UNKNOWN"

# End of module omero.model.enums

__name__ = 'omero.model'

if not _M_omero.model.__dict__.has_key('Details'):
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if not _M_omero.model.__dict__.has_key('IlluminaArrayOfArraysClass'):
    _M_omero.model.IlluminaArrayOfArraysClass = Ice.createTempClass()
    class IlluminaArrayOfArraysClass(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _value=None):
            if __builtin__.type(self) == _M_omero.model.IlluminaArrayOfArraysClass:
                raise RuntimeError('omero.model.IlluminaArrayOfArraysClass is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._value = _value

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::IObject', '::omero::model::IlluminaArrayOfArraysClass')

        def ice_id(self, current=None):
            return '::omero::model::IlluminaArrayOfArraysClass'

        def ice_staticId():
            return '::omero::model::IlluminaArrayOfArraysClass'
        ice_staticId = staticmethod(ice_staticId)

        def getValue(self, current=None):
            pass

        def setValue(self, theValue, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_IlluminaArrayOfArraysClass)

        __repr__ = __str__

    _M_omero.model.IlluminaArrayOfArraysClassPrx = Ice.createTempClass()
    class IlluminaArrayOfArraysClassPrx(_M_omero.model.IObjectPrx):

        def getValue(self, _ctx=None):
            return _M_omero.model.IlluminaArrayOfArraysClass._op_getValue.invoke(self, ((), _ctx))

        def begin_getValue(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.IlluminaArrayOfArraysClass._op_getValue.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getValue(self, _r):
            return _M_omero.model.IlluminaArrayOfArraysClass._op_getValue.end(self, _r)

        def setValue(self, theValue, _ctx=None):
            return _M_omero.model.IlluminaArrayOfArraysClass._op_setValue.invoke(self, ((theValue, ), _ctx))

        def begin_setValue(self, theValue, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.IlluminaArrayOfArraysClass._op_setValue.begin(self, ((theValue, ), _response, _ex, _sent, _ctx))

        def end_setValue(self, _r):
            return _M_omero.model.IlluminaArrayOfArraysClass._op_setValue.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.IlluminaArrayOfArraysClassPrx.ice_checkedCast(proxy, '::omero::model::IlluminaArrayOfArraysClass', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.IlluminaArrayOfArraysClassPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_IlluminaArrayOfArraysClassPrx = IcePy.defineProxy('::omero::model::IlluminaArrayOfArraysClass', IlluminaArrayOfArraysClassPrx)

    _M_omero.model._t_IlluminaArrayOfArraysClass = IcePy.declareClass('::omero::model::IlluminaArrayOfArraysClass')

    _M_omero.model._t_IlluminaArrayOfArraysClass = IcePy.defineClass('::omero::model::IlluminaArrayOfArraysClass', IlluminaArrayOfArraysClass, (), True, _M_omero.model._t_IObject, (), (('_value', (), _M_omero._t_RString),))
    IlluminaArrayOfArraysClass._ice_type = _M_omero.model._t_IlluminaArrayOfArraysClass

    IlluminaArrayOfArraysClass._op_getValue = IcePy.Operation('getValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (), (), _M_omero._t_RString, ())
    IlluminaArrayOfArraysClass._op_setValue = IcePy.Operation('setValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), _M_omero._t_RString),), (), None, ())

    _M_omero.model.IlluminaArrayOfArraysClass = IlluminaArrayOfArraysClass
    del IlluminaArrayOfArraysClass

    _M_omero.model.IlluminaArrayOfArraysClassPrx = IlluminaArrayOfArraysClassPrx
    del IlluminaArrayOfArraysClassPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
