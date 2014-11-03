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
IceImport.load("omero_model_Roi_ice")
from omero.rtypes import rlong
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"
class RoiI(_omero_model.Roi):

      SHAPES =  "ome.model.roi.Roi_shapes"
      IMAGE =  "ome.model.roi.Roi_image"
      SOURCE =  "ome.model.roi.Roi_source"
      NAMESPACES =  "ome.model.roi.Roi_namespaces"
      KEYWORDS =  "ome.model.roi.Roi_keywords"
      ANNOTATIONLINKS =  "ome.model.roi.Roi_annotationLinks"
      DESCRIPTION =  "ome.model.roi.Roi_description"
      DETAILS =  "ome.model.roi.Roi_details"
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
          if load:
              self._shapesSeq = []
              self._shapesLoaded = True;
          else:
              self._shapesSeq = []
              self._shapesLoaded = False;

          if load:
              self._annotationLinksSeq = []
              self._annotationLinksLoaded = True;
          else:
              self._annotationLinksSeq = []
              self._annotationLinksLoaded = False;

          pass

      def __init__(self, id = None, loaded = True):
          super(RoiI, self).__init__()
          # Relying on omero.rtypes.rlong's error-handling
          self._id = rlong(id)
          self._loaded = loaded
          if self._loaded:
             self._details = _omero_model.DetailsI()
             self._toggleCollectionsLoaded(True)

      def unload(self, current = None):
          self._loaded = False
          self.unloadShapes( )
          self.unloadImage( )
          self.unloadSource( )
          self.unloadNamespaces( )
          self.unloadKeywords( )
          self.unloadAnnotationLinks( )
          self.unloadDescription( )
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
          return  True ;
      def isLink(self, current = None):
          return  False ;
      def shallowCopy(self, current = None):
            if not self._loaded: return self.proxy()
            copy = RoiI()
            copy._id = self._id;
            copy._version = self._version;
            copy._details = None  # Unloading for the moment.
            raise omero.ClientError("NYI")
      def proxy(self, current = None):
          if self._id is None: raise omero.ClientError("Proxies require an id")
          return RoiI( self._id.getValue(), False )

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

      def unloadShapes(self, current = None):
          self._shapesLoaded = False
          self._shapesSeq = None;

      def _getShapes(self, current = None):
          self.errorIfUnloaded()
          return self._shapesSeq

      def _setShapes(self, _shapes, current = None):
          self.errorIfUnloaded()
          self._shapesSeq = _shapes
          self.checkUnloadedProperty(_shapes,'shapesLoaded')

      def isShapesLoaded(self):
          return self._shapesLoaded

      def sizeOfShapes(self, current = None):
          self.errorIfUnloaded()
          if not self._shapesLoaded: return -1
          return len(self._shapesSeq)

      def copyShapes(self, current = None):
          self.errorIfUnloaded()
          if not self._shapesLoaded: self.throwNullCollectionException("shapesSeq")
          return list(self._shapesSeq)

      def iterateShapes(self):
          self.errorIfUnloaded()
          if not self._shapesLoaded: self.throwNullCollectionException("shapesSeq")
          return iter(self._shapesSeq)

      def addShape(self, target, current = None):
          self.errorIfUnloaded()
          if not self._shapesLoaded: self.throwNullCollectionException("shapesSeq")
          self._shapesSeq.append( target );
          target.setRoi( self )

      def addAllShapeSet(self, targets, current = None):
          self.errorIfUnloaded()
          if  not self._shapesLoaded: self.throwNullCollectionException("shapesSeq")
          self._shapesSeq.extend( targets )
          for target in targets:
              target.setRoi( self )

      def removeShape(self, target, current = None):
          self.errorIfUnloaded()
          if not self._shapesLoaded: self.throwNullCollectionException("shapesSeq")
          self._shapesSeq.remove( target )
          target.setRoi( None )

      def removeAllShapeSet(self, targets, current = None):
          self.errorIfUnloaded()
          if not self._shapesLoaded: self.throwNullCollectionException("shapesSeq")
          for elt in targets:
              elt.setRoi( None )
              self._shapesSeq.remove( elt )

      def clearShapes(self, current = None):
          self.errorIfUnloaded()
          if not self._shapesLoaded: self.throwNullCollectionException("shapesSeq")
          for elt in self._shapesSeq:
              elt.setRoi( None )
          self._shapesSeq = list()

      def reloadShapes(self, toCopy, current = None):
          self.errorIfUnloaded()
          if self._shapesLoaded:
              raise omero.ClientError("Cannot reload active collection: shapesSeq")
          if not toCopy:
              raise omero.ClientError("Argument cannot be null")
          if toCopy.getId().getValue() != self.getId().getValue():
             raise omero.ClientError("Argument must have the same id as this instance")
          if toCopy.getDetails().getUpdateEvent().getId().getValue() < self.getDetails().getUpdateEvent().getId().getValue():
             raise omero.ClientError("Argument may not be older than this instance")
          copy = toCopy.copyShapes() # May also throw
          for elt in copy:
              elt.setRoi( self )
          self._shapesSeq = copy
          toCopy.unloadShapes()
          self._shapesLoaded = True

      def getShape(self, index, current = None):
          self.errorIfUnloaded()
          if not self._shapesLoaded: self.throwNullCollectionException("shapesSeq")
          return self._shapesSeq[index]

      def setShape(self, index, element, current = None):
          self.errorIfUnloaded()
          if not self._shapesLoaded: self.throwNullCollectionException("shapesSeq")
          old = self._shapesSeq[index]
          self._shapesSeq[index] =  element
          if element is not None and element.isLoaded():
              element.setRoi( self )
          return old

      def getPrimaryShape(self, current = None):
          self.errorIfUnloaded()
          if not self._shapesLoaded: self.throwNullCollectionException("shapesSeq")
          return self._shapesSeq[0]

      def setPrimaryShape(self, element, current = None):
          self.errorIfUnloaded()
          if not self._shapesLoaded: self.throwNullCollectionException("shapesSeq")
          index = self._shapesSeq.index(element)
          old = self._shapesSeq[0]
          self._shapesSeq[index] = old
          self._shapesSeq[0] = element
          return old

      def unloadImage(self, ):
          self._imageLoaded = False
          self._image = None;

      def getImage(self, current = None):
          self.errorIfUnloaded()
          return self._image

      def setImage(self, _image, current = None):
          self.errorIfUnloaded()
          self._image = _image
          pass

      def unloadSource(self, ):
          self._sourceLoaded = False
          self._source = None;

      def getSource(self, current = None):
          self.errorIfUnloaded()
          return self._source

      def setSource(self, _source, current = None):
          self.errorIfUnloaded()
          self._source = _source
          pass

      def unloadNamespaces(self, ):
          self._namespacesLoaded = False
          self._namespaces = None;

      def getNamespaces(self, current = None):
          self.errorIfUnloaded()
          return self._namespaces

      def setNamespaces(self, _namespaces, current = None):
          self.errorIfUnloaded()
          self._namespaces = _namespaces
          pass

      def unloadKeywords(self, ):
          self._keywordsLoaded = False
          self._keywords = None;

      def getKeywords(self, current = None):
          self.errorIfUnloaded()
          return self._keywords

      def setKeywords(self, _keywords, current = None):
          self.errorIfUnloaded()
          self._keywords = _keywords
          pass

      def unloadAnnotationLinks(self, current = None):
          self._annotationLinksLoaded = False
          self._annotationLinksSeq = None;

      def _getAnnotationLinks(self, current = None):
          self.errorIfUnloaded()
          return self._annotationLinksSeq

      def _setAnnotationLinks(self, _annotationLinks, current = None):
          self.errorIfUnloaded()
          self._annotationLinksSeq = _annotationLinks
          self.checkUnloadedProperty(_annotationLinks,'annotationLinksLoaded')

      def isAnnotationLinksLoaded(self):
          return self._annotationLinksLoaded

      def sizeOfAnnotationLinks(self, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: return -1
          return len(self._annotationLinksSeq)

      def copyAnnotationLinks(self, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          return list(self._annotationLinksSeq)

      def iterateAnnotationLinks(self):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          return iter(self._annotationLinksSeq)

      def addRoiAnnotationLink(self, target, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.append( target );
          target.setParent( self )

      def addAllRoiAnnotationLinkSet(self, targets, current = None):
          self.errorIfUnloaded()
          if  not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.extend( targets )
          for target in targets:
              target.setParent( self )

      def removeRoiAnnotationLink(self, target, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.remove( target )
          target.setParent( None )

      def removeAllRoiAnnotationLinkSet(self, targets, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          for elt in targets:
              elt.setParent( None )
              self._annotationLinksSeq.remove( elt )

      def clearAnnotationLinks(self, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          for elt in self._annotationLinksSeq:
              elt.setParent( None )
          self._annotationLinksSeq = list()

      def reloadAnnotationLinks(self, toCopy, current = None):
          self.errorIfUnloaded()
          if self._annotationLinksLoaded:
              raise omero.ClientError("Cannot reload active collection: annotationLinksSeq")
          if not toCopy:
              raise omero.ClientError("Argument cannot be null")
          if toCopy.getId().getValue() != self.getId().getValue():
             raise omero.ClientError("Argument must have the same id as this instance")
          if toCopy.getDetails().getUpdateEvent().getId().getValue() < self.getDetails().getUpdateEvent().getId().getValue():
             raise omero.ClientError("Argument may not be older than this instance")
          copy = toCopy.copyAnnotationLinks() # May also throw
          for elt in copy:
              elt.setParent( self )
          self._annotationLinksSeq = copy
          toCopy.unloadAnnotationLinks()
          self._annotationLinksLoaded = True

      def getAnnotationLinksCountPerOwner(self, current = None):
          return self._annotationLinksCountPerOwner

      def linkAnnotation(self, addition, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          link = _omero_model.RoiAnnotationLinkI()
          link.link( self, addition );
          self.addRoiAnnotationLinkToBoth( link, True )
          return link

      def addRoiAnnotationLinkToBoth(self, link, bothSides):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.append( link )

      def findRoiAnnotationLink(self, removal, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          result = list()
          for link in self._annotationLinksSeq:
              if link.getChild() == removal: result.append(link)
          return result

      def unlinkAnnotation(self, removal, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          toRemove = self.findRoiAnnotationLink(removal)
          for next in toRemove:
              self.removeRoiAnnotationLinkFromBoth( next, True )

      def removeRoiAnnotationLinkFromBoth(self, link, bothSides, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.remove( link )

      def linkedAnnotationList(self, current = None):
          self.errorIfUnloaded()
          if not self.annotationLinksLoaded: self.throwNullCollectionException("AnnotationLinks")
          linked = []
          for link in self._annotationLinksSeq:
              linked.append( link.getChild() )
          return linked

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

_omero_model.RoiI = RoiI
