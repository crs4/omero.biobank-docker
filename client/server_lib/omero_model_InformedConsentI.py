"""
   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
"""
import Ice
import IceImport
import omero
IceImport.load("omero_model_DetailsI")
IceImport.load("omero_model_InformedConsent_ice")
from omero.rtypes import rlong
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"
class InformedConsentI(_omero_model.InformedConsent):

      VID =  "ome.model.vl.InformedConsent_vid"
      LABEL =  "ome.model.vl.InformedConsent_label"
      DESCRIPTION =  "ome.model.vl.InformedConsent_description"
      DOCUMENTPATH =  "ome.model.vl.InformedConsent_documentPath"
      DOCUMENTHASH =  "ome.model.vl.InformedConsent_documentHash"
      ANSWERSDATA =  "ome.model.vl.InformedConsent_answersData"
      REFSTUDY =  "ome.model.vl.InformedConsent_refStudy"
      AUTHORS =  "ome.model.vl.InformedConsent_authors"
      APPROVINGCOMMISSION =  "ome.model.vl.InformedConsent_approvingCommission"
      APPROVALDATE =  "ome.model.vl.InformedConsent_approvalDate"
      DETAILS =  "ome.model.vl.InformedConsent_details"
      def errorIfUnloaded(self):
          if not self._loaded:
              raise _omero.UnloadedEntityException("Object unloaded:"+str(self))

      def throwNullCollectionException(self,propertyName):
          raise _omero.UnloadedEntityException(""+
          "Error updating collection:" + propertyName +"\n"+
          "Collection is currently null. This can be seen\n" +
          "by testing \""+ propertyName +"Loaded\". This implies\n"+
          "that this collection was unloaded. Please refresh this object\n"+
          "in order to update this collection.\n")

      def _toggleCollectionsLoaded(self,load):
          pass

      def __init__(self, id = None, loaded = True):
          super(InformedConsentI, self).__init__()
          # Relying on omero.rtypes.rlong's error-handling
          self._id = rlong(id)
          self._loaded = loaded
          if self._loaded:
             self._details = _omero_model.DetailsI()
             self._toggleCollectionsLoaded(True)

      def unload(self, current = None):
          self._loaded = False
          self.unloadVid( )
          self.unloadLabel( )
          self.unloadDescription( )
          self.unloadDocumentPath( )
          self.unloadDocumentHash( )
          self.unloadAnswersData( )
          self.unloadRefStudy( )
          self.unloadAuthors( )
          self.unloadApprovingCommission( )
          self.unloadApprovalDate( )
          self.unloadDetails( )

      def isLoaded(self, current = None):
          return self._loaded
      def unloadCollections(self, current = None):
          self._toggleCollectionsLoaded( False )
      def isGlobal(self, current = None):
          return  False ;
      def isMutable(self, current = None):
          return  True ;
      def isAnnotated(self, current = None):
          return  False ;
      def isLink(self, current = None):
          return  False ;
      def shallowCopy(self, current = None):
            if not self._loaded: return self.proxy()
            copy = InformedConsentI()
            copy._id = self._id;
            copy._version = self._version;
            copy._details = None  # Unloading for the moment.
            raise omero.ClientError("NYI")
      def proxy(self, current = None):
          if self._id is None: raise omero.ClientError("Proxies require an id")
          return InformedConsentI( self._id.getValue(), False )

      def getDetails(self, current = None):
          self.errorIfUnloaded()
          return self._details

      def unloadDetails(self, current = None):
          self._details = None

      def getId(self, current = None):
          return self._id

      def setId(self, _id, current = None):
          self._id = _id

      def checkUnloadedProperty(self, value, loadedField):
          if value == None:
              self.__dict__[loadedField] = False
          else:
              self.__dict__[loadedField] = True

      def getVersion(self, current = None):
          self.errorIfUnloaded()
          return self._version

      def setVersion(self, version, current = None):
          self.errorIfUnloaded()
          self._version = version

      def unloadVid(self, ):
          self._vidLoaded = False
          self._vid = None;

      def getVid(self, current = None):
          self.errorIfUnloaded()
          return self._vid

      def setVid(self, _vid, current = None):
          self.errorIfUnloaded()
          self._vid = _vid
          pass

      def unloadLabel(self, ):
          self._labelLoaded = False
          self._label = None;

      def getLabel(self, current = None):
          self.errorIfUnloaded()
          return self._label

      def setLabel(self, _label, current = None):
          self.errorIfUnloaded()
          self._label = _label
          pass

      def unloadDescription(self, ):
          self._descriptionLoaded = False
          self._description = None;

      def getDescription(self, current = None):
          self.errorIfUnloaded()
          return self._description

      def setDescription(self, _description, current = None):
          self.errorIfUnloaded()
          self._description = _description
          pass

      def unloadDocumentPath(self, ):
          self._documentPathLoaded = False
          self._documentPath = None;

      def getDocumentPath(self, current = None):
          self.errorIfUnloaded()
          return self._documentPath

      def setDocumentPath(self, _documentPath, current = None):
          self.errorIfUnloaded()
          self._documentPath = _documentPath
          pass

      def unloadDocumentHash(self, ):
          self._documentHashLoaded = False
          self._documentHash = None;

      def getDocumentHash(self, current = None):
          self.errorIfUnloaded()
          return self._documentHash

      def setDocumentHash(self, _documentHash, current = None):
          self.errorIfUnloaded()
          self._documentHash = _documentHash
          pass

      def unloadAnswersData(self, ):
          self._answersDataLoaded = False
          self._answersData = None;

      def getAnswersData(self, current = None):
          self.errorIfUnloaded()
          return self._answersData

      def setAnswersData(self, _answersData, current = None):
          self.errorIfUnloaded()
          self._answersData = _answersData
          pass

      def unloadRefStudy(self, ):
          self._refStudyLoaded = False
          self._refStudy = None;

      def getRefStudy(self, current = None):
          self.errorIfUnloaded()
          return self._refStudy

      def setRefStudy(self, _refStudy, current = None):
          self.errorIfUnloaded()
          self._refStudy = _refStudy
          pass

      def unloadAuthors(self, ):
          self._authorsLoaded = False
          self._authors = None;

      def getAuthors(self, current = None):
          self.errorIfUnloaded()
          return self._authors

      def setAuthors(self, _authors, current = None):
          self.errorIfUnloaded()
          self._authors = _authors
          pass

      def unloadApprovingCommission(self, ):
          self._approvingCommissionLoaded = False
          self._approvingCommission = None;

      def getApprovingCommission(self, current = None):
          self.errorIfUnloaded()
          return self._approvingCommission

      def setApprovingCommission(self, _approvingCommission, current = None):
          self.errorIfUnloaded()
          self._approvingCommission = _approvingCommission
          pass

      def unloadApprovalDate(self, ):
          self._approvalDateLoaded = False
          self._approvalDate = None;

      def getApprovalDate(self, current = None):
          self.errorIfUnloaded()
          return self._approvalDate

      def setApprovalDate(self, _approvalDate, current = None):
          self.errorIfUnloaded()
          self._approvalDate = _approvalDate
          pass


      def ice_postUnmarshal(self):
          """
          Provides additional initialization once all data loaded
          """
          pass # Currently unused


      def ice_preMarshal(self):
          """
          Provides additional validation before data is sent
          """
          pass # Currently unused

      def __getattr__(self, name):
          import __builtin__
          """
          Reroutes all access to object.field through object.getField() or object.isField()
          """
          field  = "_" + name
          capitalized = name[0].capitalize() + name[1:]
          getter = "get" + capitalized
          questn = "is" + capitalized
          try:
              self.__dict__[field]
              if hasattr(self, getter):
                  method = getattr(self, getter)
                  return method()
              elif hasattr(self, questn):
                  method = getattr(self, questn)
                  return method()
          except:
              pass
          raise AttributeError("'%s' object has no attribute '%s' or '%s'" % (self.__class__.__name__, getter, questn))

      def __setattr__(self, name, value):
          """
          Reroutes all access to object.field through object.getField(), with the caveat
          that all sets on variables starting with "_" are permitted directly.
          """
          if name.startswith("_"):
              self.__dict__[name] = value
              return
          else:
              field  = "_" + name
              setter = "set" + name[0].capitalize() + name[1:]
              if hasattr(self, field) and hasattr(self, setter):
                  method = getattr(self, setter)
                  return method(value)
          raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, setter))

_omero_model.InformedConsentI = InformedConsentI