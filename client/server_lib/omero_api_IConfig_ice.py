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
# Generated from file `IConfig.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy, __builtin__
import omero_RTypes_ice
import omero_ServicesF_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Included module omero.grid
_M_omero.grid = Ice.openModule('omero.grid')

# Start of module omero
__name__ = 'omero'

# Start of module omero.api
__name__ = 'omero.api'

if not _M_omero.api.__dict__.has_key('IConfig'):
    _M_omero.api.IConfig = Ice.createTempClass()
    class IConfig(_M_omero.api.ServiceInterface):
        '''See IConfig.html'''
        def __init__(self):
            if __builtin__.type(self) == _M_omero.api.IConfig:
                raise RuntimeError('omero.api.IConfig is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::api::IConfig', '::omero::api::ServiceInterface')

        def ice_id(self, current=None):
            return '::omero::api::IConfig'

        def ice_staticId():
            return '::omero::api::IConfig'
        ice_staticId = staticmethod(ice_staticId)

        def getVersion_async(self, _cb, current=None):
            pass

        def getConfigValue_async(self, _cb, key, current=None):
            pass

        def setConfigValue_async(self, _cb, key, value, current=None):
            pass

        def setConfigValueIfEquals_async(self, _cb, key, value, test, current=None):
            pass

        def getDatabaseUuid_async(self, _cb, current=None):
            pass

        def getDatabaseTime_async(self, _cb, current=None):
            pass

        def getServerTime_async(self, _cb, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.api._t_IConfig)

        __repr__ = __str__

    _M_omero.api.IConfigPrx = Ice.createTempClass()
    class IConfigPrx(_M_omero.api.ServiceInterfacePrx):

        def getVersion(self, _ctx=None):
            return _M_omero.api.IConfig._op_getVersion.invoke(self, ((), _ctx))

        def begin_getVersion(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IConfig._op_getVersion.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVersion(self, _r):
            return _M_omero.api.IConfig._op_getVersion.end(self, _r)

        def getVersion_async(self, _cb, _ctx=None):
            return _M_omero.api.IConfig._op_getVersion.invokeAsync(self, (_cb, (), _ctx))

        def getConfigValue(self, key, _ctx=None):
            return _M_omero.api.IConfig._op_getConfigValue.invoke(self, ((key, ), _ctx))

        def begin_getConfigValue(self, key, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IConfig._op_getConfigValue.begin(self, ((key, ), _response, _ex, _sent, _ctx))

        def end_getConfigValue(self, _r):
            return _M_omero.api.IConfig._op_getConfigValue.end(self, _r)

        def getConfigValue_async(self, _cb, key, _ctx=None):
            return _M_omero.api.IConfig._op_getConfigValue.invokeAsync(self, (_cb, (key, ), _ctx))

        def setConfigValue(self, key, value, _ctx=None):
            return _M_omero.api.IConfig._op_setConfigValue.invoke(self, ((key, value), _ctx))

        def begin_setConfigValue(self, key, value, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IConfig._op_setConfigValue.begin(self, ((key, value), _response, _ex, _sent, _ctx))

        def end_setConfigValue(self, _r):
            return _M_omero.api.IConfig._op_setConfigValue.end(self, _r)

        def setConfigValue_async(self, _cb, key, value, _ctx=None):
            return _M_omero.api.IConfig._op_setConfigValue.invokeAsync(self, (_cb, (key, value), _ctx))

        def setConfigValueIfEquals(self, key, value, test, _ctx=None):
            return _M_omero.api.IConfig._op_setConfigValueIfEquals.invoke(self, ((key, value, test), _ctx))

        def begin_setConfigValueIfEquals(self, key, value, test, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IConfig._op_setConfigValueIfEquals.begin(self, ((key, value, test), _response, _ex, _sent, _ctx))

        def end_setConfigValueIfEquals(self, _r):
            return _M_omero.api.IConfig._op_setConfigValueIfEquals.end(self, _r)

        def setConfigValueIfEquals_async(self, _cb, key, value, test, _ctx=None):
            return _M_omero.api.IConfig._op_setConfigValueIfEquals.invokeAsync(self, (_cb, (key, value, test), _ctx))

        def getDatabaseUuid(self, _ctx=None):
            return _M_omero.api.IConfig._op_getDatabaseUuid.invoke(self, ((), _ctx))

        def begin_getDatabaseUuid(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IConfig._op_getDatabaseUuid.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getDatabaseUuid(self, _r):
            return _M_omero.api.IConfig._op_getDatabaseUuid.end(self, _r)

        def getDatabaseUuid_async(self, _cb, _ctx=None):
            return _M_omero.api.IConfig._op_getDatabaseUuid.invokeAsync(self, (_cb, (), _ctx))

        def getDatabaseTime(self, _ctx=None):
            return _M_omero.api.IConfig._op_getDatabaseTime.invoke(self, ((), _ctx))

        def begin_getDatabaseTime(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IConfig._op_getDatabaseTime.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getDatabaseTime(self, _r):
            return _M_omero.api.IConfig._op_getDatabaseTime.end(self, _r)

        def getDatabaseTime_async(self, _cb, _ctx=None):
            return _M_omero.api.IConfig._op_getDatabaseTime.invokeAsync(self, (_cb, (), _ctx))

        def getServerTime(self, _ctx=None):
            return _M_omero.api.IConfig._op_getServerTime.invoke(self, ((), _ctx))

        def begin_getServerTime(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.IConfig._op_getServerTime.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getServerTime(self, _r):
            return _M_omero.api.IConfig._op_getServerTime.end(self, _r)

        def getServerTime_async(self, _cb, _ctx=None):
            return _M_omero.api.IConfig._op_getServerTime.invokeAsync(self, (_cb, (), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.api.IConfigPrx.ice_checkedCast(proxy, '::omero::api::IConfig', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.api.IConfigPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.api._t_IConfigPrx = IcePy.defineProxy('::omero::api::IConfig', IConfigPrx)

    _M_omero.api._t_IConfig = IcePy.defineClass('::omero::api::IConfig', IConfig, (), True, None, (_M_omero.api._t_ServiceInterface,), ())
    IConfig._ice_type = _M_omero.api._t_IConfig

    IConfig._op_getVersion = IcePy.Operation('getVersion', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (), (), IcePy._t_string, (_M_omero._t_ServerError,))
    IConfig._op_getConfigValue = IcePy.Operation('getConfigValue', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), IcePy._t_string),), (), IcePy._t_string, (_M_omero._t_ServerError,))
    IConfig._op_setConfigValue = IcePy.Operation('setConfigValue', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), IcePy._t_string), ((), IcePy._t_string)), (), None, (_M_omero._t_ServerError,))
    IConfig._op_setConfigValueIfEquals = IcePy.Operation('setConfigValueIfEquals', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (((), IcePy._t_string), ((), IcePy._t_string), ((), IcePy._t_string)), (), IcePy._t_bool, (_M_omero._t_ServerError,))
    IConfig._op_getDatabaseUuid = IcePy.Operation('getDatabaseUuid', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (), (), IcePy._t_string, (_M_omero._t_ServerError,))
    IConfig._op_getDatabaseTime = IcePy.Operation('getDatabaseTime', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (), (), _M_omero._t_RTime, (_M_omero._t_ServerError,))
    IConfig._op_getServerTime = IcePy.Operation('getServerTime', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (), (), _M_omero._t_RTime, (_M_omero._t_ServerError,))

    _M_omero.api.IConfig = IConfig
    del IConfig

    _M_omero.api.IConfigPrx = IConfigPrx
    del IConfigPrx

# End of module omero.api

__name__ = 'omero'

# End of module omero
