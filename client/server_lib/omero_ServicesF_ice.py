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
# Generated from file `ServicesF.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy, __builtin__
import omero_ServerErrors_ice
import omero_System_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Start of module omero
__name__ = 'omero'

# Start of module omero.api
_M_omero.api = Ice.openModule('omero.api')
__name__ = 'omero.api'

if not _M_omero.api.__dict__.has_key('ServiceInterface'):
    _M_omero.api.ServiceInterface = Ice.createTempClass()
    class ServiceInterface(Ice.Object):
        '''Service marker similar to ome.api.ServiceInterface. Any object which
IS-A ServiceInterface but IS-NOT-A StatefulServiceInterface (below)
is be definition a "stateless service"'''
        def __init__(self):
            if __builtin__.type(self) == _M_omero.api.ServiceInterface:
                raise RuntimeError('omero.api.ServiceInterface is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::api::ServiceInterface')

        def ice_id(self, current=None):
            return '::omero::api::ServiceInterface'

        def ice_staticId():
            return '::omero::api::ServiceInterface'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.api._t_ServiceInterface)

        __repr__ = __str__

    _M_omero.api.ServiceInterfacePrx = Ice.createTempClass()
    class ServiceInterfacePrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.api.ServiceInterfacePrx.ice_checkedCast(proxy, '::omero::api::ServiceInterface', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.api.ServiceInterfacePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.api._t_ServiceInterfacePrx = IcePy.defineProxy('::omero::api::ServiceInterface', ServiceInterfacePrx)

    _M_omero.api._t_ServiceInterface = IcePy.defineClass('::omero::api::ServiceInterface', ServiceInterface, (), True, None, (), ())
    ServiceInterface._ice_type = _M_omero.api._t_ServiceInterface

    _M_omero.api.ServiceInterface = ServiceInterface
    del ServiceInterface

    _M_omero.api.ServiceInterfacePrx = ServiceInterfacePrx
    del ServiceInterfacePrx

if not _M_omero.api.__dict__.has_key('_t_ServiceList'):
    _M_omero.api._t_ServiceList = IcePy.defineSequence('::omero::api::ServiceList', (), _M_omero.api._t_ServiceInterfacePrx)

if not _M_omero.api.__dict__.has_key('StatefulServiceInterface'):
    _M_omero.api.StatefulServiceInterface = Ice.createTempClass()
    class StatefulServiceInterface(_M_omero.api.ServiceInterface):
        '''Service marker for stateful services which permits the closing
of a particular service before the destruction of the session.'''
        def __init__(self):
            if __builtin__.type(self) == _M_omero.api.StatefulServiceInterface:
                raise RuntimeError('omero.api.StatefulServiceInterface is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::api::ServiceInterface', '::omero::api::StatefulServiceInterface')

        def ice_id(self, current=None):
            return '::omero::api::StatefulServiceInterface'

        def ice_staticId():
            return '::omero::api::StatefulServiceInterface'
        ice_staticId = staticmethod(ice_staticId)

        def passivate_async(self, _cb, current=None):
            '''Causes the blitz server to store the service implementation to disk
to free memory. This is typically done automatically by the server
when a pre-defined memory limit is reached, but can be used by the
client if it clear that a stateful service will not be used for some
time.

Activation will happen automatically whether passivation was done
manually or automatically.'''
            pass

        def activate_async(self, _cb, current=None):
            '''Load a service implementation from disk if it was previously
passivated. It is unnecessary to call this method since activation
happens automatically, but calling this may prevent a short
lapse when the service is first accessed after passivation.

It is safe to call this method at any time, even when the service
is not passivated.'''
            pass

        def close_async(self, _cb, current=None):
            '''Frees all resources -- passivated or active -- for the given
stateful service and removes its name from the object adapter.
Any further method calls will fail with a Ice::NoSuchObjectException.

Note: with JavaEE, the close method was called publically,
and internally this called destroy(). As of the OmeroBlitz
migration, this functionality has been combined.'''
            pass

        def getCurrentEventContext_async(self, _cb, current=None):
            '''To free clients from tracking the mapping from session to stateful
service, each stateful service can returns its own context information.'''
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.api._t_StatefulServiceInterface)

        __repr__ = __str__

    _M_omero.api.StatefulServiceInterfacePrx = Ice.createTempClass()
    class StatefulServiceInterfacePrx(_M_omero.api.ServiceInterfacePrx):

        '''Causes the blitz server to store the service implementation to disk
to free memory. This is typically done automatically by the server
when a pre-defined memory limit is reached, but can be used by the
client if it clear that a stateful service will not be used for some
time.

Activation will happen automatically whether passivation was done
manually or automatically.'''
        def passivate(self, _ctx=None):
            return _M_omero.api.StatefulServiceInterface._op_passivate.invoke(self, ((), _ctx))

        '''Causes the blitz server to store the service implementation to disk
to free memory. This is typically done automatically by the server
when a pre-defined memory limit is reached, but can be used by the
client if it clear that a stateful service will not be used for some
time.

Activation will happen automatically whether passivation was done
manually or automatically.'''
        def begin_passivate(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.StatefulServiceInterface._op_passivate.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Causes the blitz server to store the service implementation to disk
to free memory. This is typically done automatically by the server
when a pre-defined memory limit is reached, but can be used by the
client if it clear that a stateful service will not be used for some
time.

Activation will happen automatically whether passivation was done
manually or automatically.'''
        def end_passivate(self, _r):
            return _M_omero.api.StatefulServiceInterface._op_passivate.end(self, _r)

        '''Causes the blitz server to store the service implementation to disk
to free memory. This is typically done automatically by the server
when a pre-defined memory limit is reached, but can be used by the
client if it clear that a stateful service will not be used for some
time.

Activation will happen automatically whether passivation was done
manually or automatically.'''
        def passivate_async(self, _cb, _ctx=None):
            return _M_omero.api.StatefulServiceInterface._op_passivate.invokeAsync(self, (_cb, (), _ctx))

        '''Load a service implementation from disk if it was previously
passivated. It is unnecessary to call this method since activation
happens automatically, but calling this may prevent a short
lapse when the service is first accessed after passivation.

It is safe to call this method at any time, even when the service
is not passivated.'''
        def activate(self, _ctx=None):
            return _M_omero.api.StatefulServiceInterface._op_activate.invoke(self, ((), _ctx))

        '''Load a service implementation from disk if it was previously
passivated. It is unnecessary to call this method since activation
happens automatically, but calling this may prevent a short
lapse when the service is first accessed after passivation.

It is safe to call this method at any time, even when the service
is not passivated.'''
        def begin_activate(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.StatefulServiceInterface._op_activate.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Load a service implementation from disk if it was previously
passivated. It is unnecessary to call this method since activation
happens automatically, but calling this may prevent a short
lapse when the service is first accessed after passivation.

It is safe to call this method at any time, even when the service
is not passivated.'''
        def end_activate(self, _r):
            return _M_omero.api.StatefulServiceInterface._op_activate.end(self, _r)

        '''Load a service implementation from disk if it was previously
passivated. It is unnecessary to call this method since activation
happens automatically, but calling this may prevent a short
lapse when the service is first accessed after passivation.

It is safe to call this method at any time, even when the service
is not passivated.'''
        def activate_async(self, _cb, _ctx=None):
            return _M_omero.api.StatefulServiceInterface._op_activate.invokeAsync(self, (_cb, (), _ctx))

        '''Frees all resources -- passivated or active -- for the given
stateful service and removes its name from the object adapter.
Any further method calls will fail with a Ice::NoSuchObjectException.

Note: with JavaEE, the close method was called publically,
and internally this called destroy(). As of the OmeroBlitz
migration, this functionality has been combined.'''
        def close(self, _ctx=None):
            return _M_omero.api.StatefulServiceInterface._op_close.invoke(self, ((), _ctx))

        '''Frees all resources -- passivated or active -- for the given
stateful service and removes its name from the object adapter.
Any further method calls will fail with a Ice::NoSuchObjectException.

Note: with JavaEE, the close method was called publically,
and internally this called destroy(). As of the OmeroBlitz
migration, this functionality has been combined.'''
        def begin_close(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.StatefulServiceInterface._op_close.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Frees all resources -- passivated or active -- for the given
stateful service and removes its name from the object adapter.
Any further method calls will fail with a Ice::NoSuchObjectException.

Note: with JavaEE, the close method was called publically,
and internally this called destroy(). As of the OmeroBlitz
migration, this functionality has been combined.'''
        def end_close(self, _r):
            return _M_omero.api.StatefulServiceInterface._op_close.end(self, _r)

        '''Frees all resources -- passivated or active -- for the given
stateful service and removes its name from the object adapter.
Any further method calls will fail with a Ice::NoSuchObjectException.

Note: with JavaEE, the close method was called publically,
and internally this called destroy(). As of the OmeroBlitz
migration, this functionality has been combined.'''
        def close_async(self, _cb, _ctx=None):
            return _M_omero.api.StatefulServiceInterface._op_close.invokeAsync(self, (_cb, (), _ctx))

        '''To free clients from tracking the mapping from session to stateful
service, each stateful service can returns its own context information.'''
        def getCurrentEventContext(self, _ctx=None):
            return _M_omero.api.StatefulServiceInterface._op_getCurrentEventContext.invoke(self, ((), _ctx))

        '''To free clients from tracking the mapping from session to stateful
service, each stateful service can returns its own context information.'''
        def begin_getCurrentEventContext(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.StatefulServiceInterface._op_getCurrentEventContext.begin(self, ((), _response, _ex, _sent, _ctx))

        '''To free clients from tracking the mapping from session to stateful
service, each stateful service can returns its own context information.'''
        def end_getCurrentEventContext(self, _r):
            return _M_omero.api.StatefulServiceInterface._op_getCurrentEventContext.end(self, _r)

        '''To free clients from tracking the mapping from session to stateful
service, each stateful service can returns its own context information.'''
        def getCurrentEventContext_async(self, _cb, _ctx=None):
            return _M_omero.api.StatefulServiceInterface._op_getCurrentEventContext.invokeAsync(self, (_cb, (), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.api.StatefulServiceInterfacePrx.ice_checkedCast(proxy, '::omero::api::StatefulServiceInterface', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.api.StatefulServiceInterfacePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.api._t_StatefulServiceInterfacePrx = IcePy.defineProxy('::omero::api::StatefulServiceInterface', StatefulServiceInterfacePrx)

    _M_omero.api._t_StatefulServiceInterface = IcePy.defineClass('::omero::api::StatefulServiceInterface', StatefulServiceInterface, (), True, None, (_M_omero.api._t_ServiceInterface,), ())
    StatefulServiceInterface._ice_type = _M_omero.api._t_StatefulServiceInterface

    StatefulServiceInterface._op_passivate = IcePy.Operation('passivate', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (), (), None, (_M_omero._t_ServerError,))
    StatefulServiceInterface._op_activate = IcePy.Operation('activate', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (), (), None, (_M_omero._t_ServerError,))
    StatefulServiceInterface._op_close = IcePy.Operation('close', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, (), (), (), None, (_M_omero._t_ServerError,))
    StatefulServiceInterface._op_getCurrentEventContext = IcePy.Operation('getCurrentEventContext', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, (), (), (), _M_omero.sys._t_EventContext, (_M_omero._t_ServerError,))

    _M_omero.api.StatefulServiceInterface = StatefulServiceInterface
    del StatefulServiceInterface

    _M_omero.api.StatefulServiceInterfacePrx = StatefulServiceInterfacePrx
    del StatefulServiceInterfacePrx

if not _M_omero.api.__dict__.has_key('IAdmin'):
    _M_omero.api._t_IAdmin = IcePy.declareClass('::omero::api::IAdmin')
    _M_omero.api._t_IAdminPrx = IcePy.declareProxy('::omero::api::IAdmin')

if not _M_omero.api.__dict__.has_key('IConfig'):
    _M_omero.api._t_IConfig = IcePy.declareClass('::omero::api::IConfig')
    _M_omero.api._t_IConfigPrx = IcePy.declareProxy('::omero::api::IConfig')

if not _M_omero.api.__dict__.has_key('IContainer'):
    _M_omero.api._t_IContainer = IcePy.declareClass('::omero::api::IContainer')
    _M_omero.api._t_IContainerPrx = IcePy.declareProxy('::omero::api::IContainer')

if not _M_omero.api.__dict__.has_key('IDelete'):
    _M_omero.api._t_IDelete = IcePy.declareClass('::omero::api::IDelete')
    _M_omero.api._t_IDeletePrx = IcePy.declareProxy('::omero::api::IDelete')

if not _M_omero.api.__dict__.has_key('ILdap'):
    _M_omero.api._t_ILdap = IcePy.declareClass('::omero::api::ILdap')
    _M_omero.api._t_ILdapPrx = IcePy.declareProxy('::omero::api::ILdap')

if not _M_omero.api.__dict__.has_key('IMetadata'):
    _M_omero.api._t_IMetadata = IcePy.declareClass('::omero::api::IMetadata')
    _M_omero.api._t_IMetadataPrx = IcePy.declareProxy('::omero::api::IMetadata')

if not _M_omero.api.__dict__.has_key('IPixels'):
    _M_omero.api._t_IPixels = IcePy.declareClass('::omero::api::IPixels')
    _M_omero.api._t_IPixelsPrx = IcePy.declareProxy('::omero::api::IPixels')

if not _M_omero.api.__dict__.has_key('IProjection'):
    _M_omero.api._t_IProjection = IcePy.declareClass('::omero::api::IProjection')
    _M_omero.api._t_IProjectionPrx = IcePy.declareProxy('::omero::api::IProjection')

if not _M_omero.api.__dict__.has_key('IQuery'):
    _M_omero.api._t_IQuery = IcePy.declareClass('::omero::api::IQuery')
    _M_omero.api._t_IQueryPrx = IcePy.declareProxy('::omero::api::IQuery')

if not _M_omero.api.__dict__.has_key('IRoi'):
    _M_omero.api._t_IRoi = IcePy.declareClass('::omero::api::IRoi')
    _M_omero.api._t_IRoiPrx = IcePy.declareProxy('::omero::api::IRoi')

if not _M_omero.api.__dict__.has_key('IScript'):
    _M_omero.api._t_IScript = IcePy.declareClass('::omero::api::IScript')
    _M_omero.api._t_IScriptPrx = IcePy.declareProxy('::omero::api::IScript')

if not _M_omero.api.__dict__.has_key('ISession'):
    _M_omero.api._t_ISession = IcePy.declareClass('::omero::api::ISession')
    _M_omero.api._t_ISessionPrx = IcePy.declareProxy('::omero::api::ISession')

if not _M_omero.api.__dict__.has_key('IShare'):
    _M_omero.api._t_IShare = IcePy.declareClass('::omero::api::IShare')
    _M_omero.api._t_ISharePrx = IcePy.declareProxy('::omero::api::IShare')

if not _M_omero.api.__dict__.has_key('ITypes'):
    _M_omero.api._t_ITypes = IcePy.declareClass('::omero::api::ITypes')
    _M_omero.api._t_ITypesPrx = IcePy.declareProxy('::omero::api::ITypes')

if not _M_omero.api.__dict__.has_key('IUpdate'):
    _M_omero.api._t_IUpdate = IcePy.declareClass('::omero::api::IUpdate')
    _M_omero.api._t_IUpdatePrx = IcePy.declareProxy('::omero::api::IUpdate')

if not _M_omero.api.__dict__.has_key('IRenderingSettings'):
    _M_omero.api._t_IRenderingSettings = IcePy.declareClass('::omero::api::IRenderingSettings')
    _M_omero.api._t_IRenderingSettingsPrx = IcePy.declareProxy('::omero::api::IRenderingSettings')

if not _M_omero.api.__dict__.has_key('IRepositoryInfo'):
    _M_omero.api._t_IRepositoryInfo = IcePy.declareClass('::omero::api::IRepositoryInfo')
    _M_omero.api._t_IRepositoryInfoPrx = IcePy.declareProxy('::omero::api::IRepositoryInfo')

if not _M_omero.api.__dict__.has_key('ITimeline'):
    _M_omero.api._t_ITimeline = IcePy.declareClass('::omero::api::ITimeline')
    _M_omero.api._t_ITimelinePrx = IcePy.declareProxy('::omero::api::ITimeline')

if not _M_omero.api.__dict__.has_key('Exporter'):
    _M_omero.api._t_Exporter = IcePy.declareClass('::omero::api::Exporter')
    _M_omero.api._t_ExporterPrx = IcePy.declareProxy('::omero::api::Exporter')

if not _M_omero.api.__dict__.has_key('Gateway'):
    _M_omero.api._t_Gateway = IcePy.declareClass('::omero::api::Gateway')
    _M_omero.api._t_GatewayPrx = IcePy.declareProxy('::omero::api::Gateway')

if not _M_omero.api.__dict__.has_key('JobHandle'):
    _M_omero.api._t_JobHandle = IcePy.declareClass('::omero::api::JobHandle')
    _M_omero.api._t_JobHandlePrx = IcePy.declareProxy('::omero::api::JobHandle')

if not _M_omero.api.__dict__.has_key('RawFileStore'):
    _M_omero.api._t_RawFileStore = IcePy.declareClass('::omero::api::RawFileStore')
    _M_omero.api._t_RawFileStorePrx = IcePy.declareProxy('::omero::api::RawFileStore')

if not _M_omero.api.__dict__.has_key('RawPixelsStore'):
    _M_omero.api._t_RawPixelsStore = IcePy.declareClass('::omero::api::RawPixelsStore')
    _M_omero.api._t_RawPixelsStorePrx = IcePy.declareProxy('::omero::api::RawPixelsStore')

if not _M_omero.api.__dict__.has_key('RenderingEngine'):
    _M_omero.api._t_RenderingEngine = IcePy.declareClass('::omero::api::RenderingEngine')
    _M_omero.api._t_RenderingEnginePrx = IcePy.declareProxy('::omero::api::RenderingEngine')

if not _M_omero.api.__dict__.has_key('Search'):
    _M_omero.api._t_Search = IcePy.declareClass('::omero::api::Search')
    _M_omero.api._t_SearchPrx = IcePy.declareProxy('::omero::api::Search')

if not _M_omero.api.__dict__.has_key('ThumbnailStore'):
    _M_omero.api._t_ThumbnailStore = IcePy.declareClass('::omero::api::ThumbnailStore')
    _M_omero.api._t_ThumbnailStorePrx = IcePy.declareProxy('::omero::api::ThumbnailStore')

# End of module omero.api

__name__ = 'omero'

# Start of module omero.grid
_M_omero.grid = Ice.openModule('omero.grid')
__name__ = 'omero.grid'

if not _M_omero.grid.__dict__.has_key('ScriptProcessor'):
    _M_omero.grid._t_ScriptProcessor = IcePy.declareClass('::omero::grid::ScriptProcessor')
    _M_omero.grid._t_ScriptProcessorPrx = IcePy.declareProxy('::omero::grid::ScriptProcessor')

if not _M_omero.grid.__dict__.has_key('SharedResources'):
    _M_omero.grid._t_SharedResources = IcePy.declareClass('::omero::grid::SharedResources')
    _M_omero.grid._t_SharedResourcesPrx = IcePy.declareProxy('::omero::grid::SharedResources')

if not _M_omero.grid.__dict__.has_key('Table'):
    _M_omero.grid._t_Table = IcePy.declareClass('::omero::grid::Table')
    _M_omero.grid._t_TablePrx = IcePy.declareProxy('::omero::grid::Table')

# End of module omero.grid

__name__ = 'omero'

# End of module omero
